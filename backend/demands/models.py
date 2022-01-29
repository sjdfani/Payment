from django.db import models
from user.models import CustomUser


class DemandsManager(models.Manager):
    def all(self):
        return self.get_queryset().filter(status=True)


class Demands(models.Model):
    STATE_DEMANDS = [
        ('debtor', 'Debtor'),
        ('credit', 'Credit')
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    state = models.CharField(max_length=8, choices=STATE_DEMANDS)
    who = models.CharField(max_length=250)
    price = models.CharField(max_length=50)
    subject = models.CharField(max_length=250)
    description = models.TextField()
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    objects = DemandsManager()

    class Meta:
        ordering = ['-date']
        verbose_name = 'demand'

    def __str__(self) -> str:
        return self.subject
