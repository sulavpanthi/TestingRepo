from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import get_object_or_404
from django import forms

from .forms import SignUpForm, LoginForm

from blogs.models import Blog

USER = get_user_model()

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = USER(first_name = form.cleaned_data['first_name'],
            last_name = form.cleaned_data['last_name'],
            username = form.cleaned_data['username'],
            email = form.cleaned_data['email'],
            profile_pic = form.cleaned_data['profile_pic'],
            )

            if form.cleaned_data['password'] != form.cleaned_data['confirm_password']:
                raise forms.ValidationError('Password and confirm password do not match')

            user.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/user/login/')

    else:
        if request.user.is_authenticated:
            return render(request, 'user/profile.html')
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(email = form.cleaned_data['email'],
            password = form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect('/user/profile/')
    else:
        if request.user.is_authenticated:
            return redirect('/user/profile/')
        form = LoginForm()

    return render(request, 'user/login.html', {'form': form})

@login_required(login_url='/user/login/')
def profile_view(request):
    if request.user.is_authenticated:
        blog_list = Blog.objects.filter(author_id = request.user.id)
        return render(request, 'user/profile.html', {'blogs':blog_list})
    else:
        return HttpResponse("Invalid user", status = 404)

@login_required(login_url='/user/login/')
def logout_view(request):
    logout(request)
    return redirect('/user/login/')

# class UpdateView(View):
#     template_name = 'user/update.html'

#     @method_decorator(login_required(login_url='/user/login/'))
#     def get(self, request, id=None):
#         user_object = get_object_or_404(USER, id = request.user.id) 
#         form = SignUpForm(instance=user_object)
#         return render(request, 'user/update.html', {'form': form})

#     @method_decorator(login_required(login_url='/user/login/'))
#     def post(self, request, id=None):
#         user_object = get_object_or_404(USER, id = request.user.id) 
#         form = SignUpForm(request.POST, request.FILES, instance=user_object)

#         if form.is_valid():
#             user_object.set_password(form.cleaned_data['password'])
#             form.save()

#             return redirect('/user/profile')
#         else:
#             print("Error")

#             return redirect('/users/update')

            