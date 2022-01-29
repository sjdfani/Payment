from django.urls import path
from .views import DemandsCreate, DemandsDesUpRet, DemandsList, DeltaMonthAndPrice_debtor, DeltaMonthAndPrice_credit, DeltaMonthAndPrice_total

app_name = 'demands'

urlpatterns = [
    path('create/', DemandsCreate.as_view()),
    path('list/', DemandsList.as_view()),
    path('list/<int:pk>/', DemandsDesUpRet.as_view()),
    path('delta-time-debtor/', DeltaMonthAndPrice_debtor.as_view()),
    path('delta-time-credit/', DeltaMonthAndPrice_credit.as_view()),
    path('delta-time-total/', DeltaMonthAndPrice_total.as_view()),
]
