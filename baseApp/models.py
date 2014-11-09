from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movement(models.Model):
    description = models.CharField(max_length=150)
    amount = models.FloatField()
    balance = models.FloatField()
    date = models.DateField()
    user = models.ForeignKey(User)

    # def __unicode__(self):
    #     return self.description, self.amount, self.balance, self.date, self.user