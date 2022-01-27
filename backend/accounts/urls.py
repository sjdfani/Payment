from django.urls import path
from .views import CreateAccount, ListAccount, RetUpDelAccount,DeltaBetweenMonth

app_name = 'accounts'

urlpatterns = [
    path('create/', CreateAccount.as_view()),
    path('list/', ListAccount.as_view()),
    path('list/<int:pk>/', RetUpDelAccount.as_view()),
    path('test/', DeltaBetweenMonth.as_view()),
]
