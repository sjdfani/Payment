from django.urls import path
from .views import CreateAccount, ListAccount, RetUpDelAccount, DeltaMonthAndTotalPrice_IN, DeltaMonthAndTotalPrice_OUT,DeltaMonthAndTotalPrice_Total

app_name = 'accounts'

urlpatterns = [
    path('create/', CreateAccount.as_view()),
    path('list/', ListAccount.as_view()),
    path('list/<int:pk>/', RetUpDelAccount.as_view()),
    path('delta-time-deposit/', DeltaMonthAndTotalPrice_IN.as_view()),
    path('delta-time-withdraw/', DeltaMonthAndTotalPrice_OUT.as_view()),
    path('delta-time-total/', DeltaMonthAndTotalPrice_Total.as_view()),
]
