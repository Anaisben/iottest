from django.db import models

class Lead(models.Model):
    value1 = models.IntegerField()
    action = models.CharField(max_length=300)
    value2 = models.IntegerField()
    result = models.IntegerField()