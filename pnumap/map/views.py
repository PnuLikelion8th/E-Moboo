from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm
from .models import Blog

# Create your views here.
def main(request):
    return render(request, "main.html")



def search(request):
    return redner(request,"main.html")

def index(request):
    buildings = Blog.objects.all()
    return render(request, 'index.html', {'buildings':buildings})

def write(request):
    blogform = BlogForm(request.POST)
    if blogform.is_valid():
        blogform.save()
        return redirect('index')
    blogform = BlogForm()
    return render(request, 'write.html', {'blogform':blogform})

def detail(request, building_id):
    building = get_object_or_404(Blog, id=building_id)
    return render(request, 'detail.html', {'building':building})

def update(request, building_id):
    building_update = get_object_or_404(Blog, id=building_id)
    if request.method == "POST":
        blogform = BlogForm(request.POST, instance=building_update)
        if blogform.is_valid():
            blogform.save()
            return redirect('index')
    blogform = BlogForm(instance=building_update)
    return render(request, 'write.html', {'blogform':blogform})

def delete(request,building_id):
    building_delete = get_object_or_404(Blog, id=building_id)
    building_delete.delete()
    return redirect('index')
