"""pnumap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from map import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name="main"),
    path('search/',views.search, name="search"),
    path('score/<str:flag>',views.score, name="score"),
    path('write/', views.write, name="write"),
    path('index/', views.index, name="index"),
    path('detail/<int:building_id>', views.detail, name="detail"),
    path('update/<int:building_id>', views.update, name="update"),
    path('delete/<int:building_id>', views.delete, name="delete"),
<<<<<<< HEAD
    path('reviewparse/', views.reviewdata, name="reviewdata")
    path('courseparse/', views.coursedata, name="coursedata")
=======
    path('building/<int:building_id>', views.building_info, name="building"),
    # path('parse/', views.reviewdata, name="reviewdata")
>>>>>>> 0f8ed8062cc4bc3adeffd9dec3f351fe876e47c2
]
