from django.db import models
from user.models import CustomUser


class AccountModel(models.Model):
    STATE_MONEY = [
        ('deposit', 'Deposit'),
        ('withdraw', 'Withdraw')
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=8, choices=STATE_MONEY, default=None)
    subject = models.CharField(max_length=250)
    price = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name = 'Account'

    def __str__(self) -> str:
        return self.subject
