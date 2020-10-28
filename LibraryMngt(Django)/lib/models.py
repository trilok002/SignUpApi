from django.db import models

# Create your models here.
class Books(models.Model):
    bname=models.CharField(max_length=40)
    bauthor=models.CharField(max_length=20)
    genres =models.CharField(max_length=20,null=True)
    bimage=models.FileField(null=True)
    bdetail=models.TextField(null=True)
    def __str__(self):
        return self.bname

class Students(models.Model):
    enroll=models.CharField(max_length=15)
    name=models.CharField(max_length=30)
    branch=models.CharField(max_length=5)
    college=models.CharField(max_length=10)
    mobile=models.IntegerField(max_length=11)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=15)
    def __str__(self):
        return self.enroll

class Brecord(models.Model):
    stdenroll=models.CharField(max_length=15)
    apbid=models.IntegerField()
    issued=models.BooleanField(null=True)
    issuedate=models.DateField(null=True)
    returndate=models.DateField(null=True)

