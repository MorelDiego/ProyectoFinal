from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Reviews(models.Model):
    title = models.CharField(max_length=40)
    film = models.CharField(max_length=40)
    body = HTMLField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='images/reviews', null=True, blank=True)
    date = models.DateField(default=now)

    def __str__(self):
        return f'Title: {self.title}, Film: {self.film}, Body: {self.body}, Author: {self.author}, Date: {self.date}'

class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=90)
    message = models.CharField(max_length=250)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/avatars', null=True, blank=True)

    def __str__(self):
        return f'User: {self.user}, Image: {self.image}'