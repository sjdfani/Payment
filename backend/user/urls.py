from django.urls import path
from .views import Login

app_name = 'user'

urlpatterns = [
    path('login/', Login.as_view()),
]
