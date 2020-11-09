from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.ForeignKey(User,models.CASCADE)
    dob=models.DateField(blank=True,null=True)
    image=models.FileField(null=True)
