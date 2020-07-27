from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from django.http import HttpResponseRedirect

from .forms import BlogCreateModelForm
from .models import Blog

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

USER = get_user_model()

# Create your views here.


# def landing_view(request):
#     return render(request, 'blogs/landing.html')

class Landing_View(TemplateView):
    template_name = 'blogs/landing.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/user/profile/')
        else:
            return super().get(request, *args, **kwargs)

class Create(CreateView):
    form_class = BlogCreateModelForm
    template_name = 'blogs/create.html'
    success_url = '/user/profile/'

    @method_decorator(login_required(login_url='/user/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        print(form.cleaned_data)
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.author_id = self.request.user.id
        self.object.save()
        return super().form_valid(form)
       

class BlogListView(ListView):
    template_name = 'blogs/blog.html'
    # model = Blog
    context_object_name = 'blogs'
    def get_queryset(self):
        return Blog.objects.all().order_by('-id')

class BlogUpdateView(UpdateView):
    form_class = BlogCreateModelForm
    success_url = '/user/profile/'
    model = Blog
    template_name = 'blogs/update.html'

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = '/user/profile/'

    def get_queryset(self):
        return Blog.objects.filter(author_id = self.request.user.id)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
