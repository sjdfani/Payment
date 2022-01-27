from datetime import datetime
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .models import AccountModel
from .serializer import AccountSerializer
from django.db.models.aggregates import Sum
from django.db.models import FloatField
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


class DeltaBetweenMonth(APIView):

    def post(self, request):
        msg = dict()
        data = request.data['month']
        month_number = datetime.strptime(data, '%b').month
        acc = AccountModel.objects.filter(created__month=month_number).annotate(
            price_float=Cast('price', FloatField())
        ).aggregate(Sum('price_float'))['price_float__sum']
        print(acc)
        # acc = AccountSerializer(acc,many=True)
        return Response({'total': acc})


