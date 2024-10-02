from django.db import models
from django.db.models import CASCADE
# Create your models here.
class Ads(models.Model):
    id = models.AutoField(primary_key=True)
    duration = models.IntegerField()
    ratio = models.DecimalField(max_digits=4, decimal_places=3)

