from django.db import models

# Create your models here.

class UserAgents(models.Model):
    useragent = models.CharField(max_length=255)
    popularity = models.IntegerField()
    
