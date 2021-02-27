from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


 #Create your models here.
class author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    details=models.TextField()

    def __str__(self):
        return self.name.username

    

class post(models.Model):
    post_author =models.ForeignKey(author, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=120)
    content= models.TextField()
    image = models.ImageField(blank=True)
    create_time=models.DateTimeField(auto_now=False, auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title



class Comment(models.Model):
    Post = models.ForeignKey(post,on_delete=models.CASCADE,related_name='comments',default=None)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=False,auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
    







