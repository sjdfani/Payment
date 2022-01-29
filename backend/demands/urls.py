from django.urls import path
from .views import DemandsCreate, DemandsDesUpRet, DemandsList

app_name = 'demands'

urlpatterns = [
    path('create/', DemandsCreate.as_view()),
    path('list/', DemandsList.as_view()),
    path('list/<int:pk>/', DemandsDesUpRet.as_view())
]
