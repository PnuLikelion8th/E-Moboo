from django.db import models

# Create your models here.
class ReviewData(models.Model):
    coursename = models.CharField(max_length=100)
    prof = models.CharField(max_length=50)
    star = models.DecimalField(max_digits=5, decimal_places=2)