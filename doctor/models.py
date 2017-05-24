from django.db import models

# Create your models here.

class User(models.Model):
    brand_id = models.IntegerField()
    user_id = models.IntegerField()
    password = models.TextField(min_length=8)
    role = models.TextField(max_length=100)
    name = models.TextField(max_length=300)
    dOB = models.DateTimeField('date published')
    phone_Number = models.CharField(max_length=11)
    address = models.TextField(max_length=500)
    specialize = models.TextField(max_length=100)
    def __str__(self):
        return self.name