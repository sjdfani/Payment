from django.urls import path
from .views import CreateAccount, ListAccount, RetUpDelAccount

app_name = 'accounts'

urlpatterns = [
    path('create/', CreateAccount.as_view()),
    path('list/', ListAccount.as_view()),
    path('list/<int:pk>/', RetUpDelAccount.as_view()),
]
