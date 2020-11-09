from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=25)
    def __str__(self):
        return self.name
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=25)
    image=models.FileField(null=True)
    description=models.TextField(null=True)
    price=models.DecimalField(decimal_places=2,max_digits=8)
    available=models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Cart(models.Model):
    products=models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
        return self.products.name