from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    refferal_code = models.CharField(max_length=20 , blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    