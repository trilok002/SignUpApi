from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    cat = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100,null=True)
    short_des = models.TextField(null=True)
    long_des = models.TextField(null=True)
    image = models.FileField(null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.title + '--' +self.cat.name +'--' + self.user.username

class likecomment(models.Model):
    post_data=models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    usr=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    like=models.BooleanField(default=False)
    comment=models.TextField(null=True,blank=True)
    date= models.DateField(null=True)

    def __str__(self):
        return self.post_data.title

class userdetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    image = models.FileField(null=True)