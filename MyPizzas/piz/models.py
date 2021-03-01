from djongo import models

# Create your models here.
class Pizza(models.Model):
    type=models.CharField(max_length=20,null=True)
    size=models.CharField(max_length=50,null=True)
    toppings=models.TextField(null=True)