from django.db import models
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    title = models.TextField(max_length=200)
    body = models.TextField()
    date = models.DateField(default = timezone.now)

    def __str__(self):
        return self.title

class Building(models.Model):
    num = models.IntegerField() #건물번호

class Major(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    major = models.CharField(max_length=50) #학과

class Professor(models.Model):
    name = models.CharField(max_length=10) #교수이름
    major = models.ForeignKey(Major, on_delete=models.CASCADE) #전공
    status = models.CharField(max_length=10) #직위?직책

class Course(models.Model):
    prof = models.ForeignKey(Professor, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)

class ReviewData(models.Model):
    coursename = models.ForeignKey(Course, on_delete=models.CASCADE)
    star = models.DecimalField(max_digits=5, decimal_places=2)
    review = models.TextField(max_length=300, null=True)
    
    def __str__(self):
        return self.coursename