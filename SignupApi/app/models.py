from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Users(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    is_teacher=models.BooleanField(default=False)