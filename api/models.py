from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Category(models.Model):
    name = models.CharField(max_length=100)
    related_words = models.TextField(blank=True)
    user = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)


class Movement(models.Model):
    description = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.DateField()
    categories = models.ManyToManyField(Category)
    user = models.ForeignKey('auth.User', related_name='movements', on_delete=models.CASCADE)
