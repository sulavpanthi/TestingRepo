from django.shortcuts import render, redirect

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Blog, Author
from .forms import BlogCreateModelForm, AuthorCreateModelForm

# Create your views here.

def blog_view(request):

    blogs = Blog.objects.all()
    
    # pagination implementation start

    paginator = Paginator(blogs, 5)
    page = request.GET.get('page', 1)
    try:
        blogs_list = paginator.get_page(page)
    except PageNotAnInteger:
        blogs_list = paginator.get_page(1)
    except EmptyPage:
        blogs_list = paginator.get_page(paginator.num_pages)

    # pagination implementation end

    # remaining pagination implementation in blogs/blog.html

    return render(request, 'blogs/blog.html', {'blogs':blogs_list})

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