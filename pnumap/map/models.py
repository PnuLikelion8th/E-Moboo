from django.db import models
from django.utils import timezone

# Create your models here.
class ReviewData(models.Model):
    coursename = models.CharField(max_length=100)
    prof = models.CharField(max_length=50)
    star = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.coursename

class Blog(models.Model):
    title = models.TextField(max_length=200)
    body = models.TextField()
    date = models.DateField(default = timezone.now)

    def __str__(self):
        return self.title