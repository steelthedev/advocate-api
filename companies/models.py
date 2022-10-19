from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Company(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField()
    email = models.EmailField()
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name




