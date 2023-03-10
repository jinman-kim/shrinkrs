from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.


class PayPlan(models.Model):
    name = models.CharField(max_length = 20)
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Users(AbstractUser):
    user = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING)

class UserDetail(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    pay_plan = models.ForeignKey(PayPlan, on_delete = models.DO_NOTHING)