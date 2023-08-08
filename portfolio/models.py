from django.db import models

# Create your models here.
class MessageInfo(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=150)
    msg = models.TextField(max_length=350)