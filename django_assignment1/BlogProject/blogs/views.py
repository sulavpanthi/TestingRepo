from django.shortcuts import render, redirect
from .models import Blog, Author
from .forms import BlogCreateModelForm, AuthorCreateModelForm

# Create your views here.

def blog_view(request):

    blogs = Blog.objects.all()
    return render(request, 'blogs/blog.html', {'blogs':blogs})

def landing_view(request):
    return render(request, 'blogs/landing.html')

def blog_create(request):
    if request.method == 'POST':
        form = BlogCreateModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('/blogs/blog/')
    else:
        form = BlogCreateModelForm()
    return render(request, 'blogs/create.html', {'form' : form})

def create_author(request):

    if request.method == 'POST':
        form = AuthorCreateModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('/blogs/create/')
    else:
        form = AuthorCreateModelForm()
    return render(request, 'blogs/create-author.html', {'form': form})