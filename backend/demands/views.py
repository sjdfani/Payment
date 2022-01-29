from datetime import datetime
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import DemandsSerializer
from .models import Demands
from django.db.models.aggregates import Sum
from django.db.models.functions import Cast
from django.db.models import FloatField, Q


class DemandsCreate(APIView):
    permission_class = [IsAdminUser]

    def post(self, request):
        data = request.data
        data['user'] = request.user.id
        serializer = DemandsSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class DemandsList(ListAPIView):
    serializer_class = DemandsSerializer

    def get_queryset(self):
        return Demands.objects.filter(user=self.request.user)


class DemandsDesUpRet(RetrieveUpdateDestroyAPIView):
    serializer_class = DemandsSerializer
    permission_class = [IsAdminUser]

    def get_queryset(self):
        return Demands.objects.filter(user=self.request.user)


class DeltaMonthAndPrice_debtor(APIView):

    def post(self, request):
        msg = dict()
        month_data = request.data['month']
        month_data = month_data.lower().capitalize()
        year_data = request.data['year']
        month_number = datetime.strptime(month_data, '%b').month
        lookup = Q(user=request.user) & Q(
            date__month=month_number) & Q(date__year=year_data) & Q(state='debtor')
        price = Demands.objects.filter(lookup).annotate(
            price_float=Cast('price', FloatField())
        ).aggregate(Sum('price_float'))['price_float__sum']
        demands = Demands.objects.filter(lookup)
        DemandSeri = DemandsSerializer(demands, many=True)
        msg['demands'] = DemandSeri.data
        msg['total_price'] = price
        return Response(msg, status=status.HTTP_200_OK)


class DeltaMonthAndPrice_credit(APIView):
    def post(self, request):
        msg = dict()
        month_data = request.data['month']
        month_data = month_data.lower().capitalize()
        year_data = request.data['year']
        month_number = datetime.strptime(month_data, '%b').month
        lookup = Q(user=request.user) & Q(
            date__month=month_number) & Q(date__year=year_data) & Q(state='credit')
        price = Demands.objects.filter(lookup).annotate(
            price_float=Cast('price', FloatField())
        ).aggregate(Sum('price_float'))['price_float__sum']
        demands = Demands.objects.filter(lookup)
        DemandSeri = DemandsSerializer(demands, many=True)
        msg['demands'] = DemandSeri.data
        msg['total_price'] = price
        return Response(msg, status=status.HTTP_200_OK)


class DeltaMonthAndPrice_total(APIView):
    def post(self, request):
        msg = dict()
        month_data = request.data['month']
        month_data = month_data.lower().capitalize()
        year_data = request.data['year']
        month_number = datetime.strptime(month_data, '%b').month
        lookup = Q(user=request.user) & Q(
            date__month=month_number) & Q(date__year=year_data)
        demands = Demands.objects.filter(lookup)
        DemandSeri = DemandsSerializer(demands, many=True)
        msg['demands'] = DemandSeri.data
        return Response(msg, status=status.HTTP_200_OK)
