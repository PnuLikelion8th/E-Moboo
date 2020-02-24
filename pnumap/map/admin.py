from django.contrib import admin
from .models import Blog, Building, Major, Professor, Course, ReviewData

# Register your models here.
admin.site.register(Blog)
admin.site.register(Building)
admin.site.register(Major)
admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(ReviewData)