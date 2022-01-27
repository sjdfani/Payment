from datetime import datetime
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .models import AccountModel
from .serializer import AccountSerializer
from django.db.models.aggregates import Sum
from django.db.models import FloatField, Q
from django.db.models.functions import Cast


class CreateAccount(APIView):

    def post(self, request):
        data = request.data
        data['user'] = request.user
        acc = AccountModel.objects.create(**data)
        AccSerializer = AccountSerializer(acc)
        return Response(AccSerializer.data, status=status.HTTP_201_CREATED)


class ListAccount(ListAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return AccountModel.objects.filter(user=self.request.user)


class RetUpDelAccount(RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializer

    def get_queryset(self):
        return AccountModel.objects.filter(user=self.request.user)


class DeltaMonthAndTotalPrice(APIView):

    def post(self, request):
        msg = dict()
        month_data = request.data['month']
        year_data = request.data['year']
        month_number = datetime.strptime(month_data, '%b').month

        lookup = Q(user=request.user) & Q(
            created__month=month_number) & Q(created__year=year_data)

        price = AccountModel.objects.filter(lookup).annotate(
            price_float=Cast('price', FloatField())
        ).aggregate(Sum('price_float'))['price_float__sum']
        accounts = AccountModel.objects.filter(lookup)
        AccSeri = AccountSerializer(accounts, many=True)
        msg['accounts'] = AccSeri.data
        msg['total_price'] = price
        return Response(msg, status=status.HTTP_200_OK)
