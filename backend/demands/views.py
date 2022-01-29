from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import DemandsSerializer
from .models import Demands


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
