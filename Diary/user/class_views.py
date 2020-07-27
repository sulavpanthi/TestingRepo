from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views import View
# from django.contrib.auth.views import LoginView

from .forms import SignUpForm, LoginForm, UpdateUserForm, UpdatePictureForm
from blogs.models import Blog

USER = get_user_model()

class SignupView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/user/profile/')
        form = SignUpForm()
        return render(request, 'user/signup.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = USER(
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                email = form.cleaned_data['email'],
                username = form.cleaned_data['username'],
                profile_pic = form.cleaned_data['profile_pic']
            )
            user.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/user/login/')

        else:
            messages.error(request, 'Invalid data input. Check your inputs.')
            return HttpResponse('Invalid form data', status=400)


class Login_View(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'user/login.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect('/blogs/list/')
            else:
                messages.error(request, 'Login credentials do not match.')
                return HttpResponseBadRequest('Auth credentials do not match')

@method_decorator(login_required(login_url='/user/login/'), name = 'get')
class ProfileView(View):
    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.filter(author_id = request.user.id)
        return render(request, 'user/profile.html', {'blogs':blogs})

@method_decorator(login_required(login_url='/user/login/'), name = 'get')
class LogoutView(View):
    def get(self, request, *args, **kwargs):

        logout(request)
        messages.success(request, 'Logged out successfully')
        return redirect('/user/login/')

@method_decorator(login_required(login_url='/user/login/'), name = 'get')
class UpdateProfileView(View):
    def get(self, request, *args, **kwargs):
        user_object = get_object_or_404(USER, id = request.user.id)
        user_form = UpdateUserForm(instance = user_object)
        picture_form = UpdatePictureForm(instance = user_object)
        context = {
            'user_form': user_form,
            'picture_form': picture_form
        }
        return render(request, 'user/update.html', context)

    def post(self, request, *args, **kwargs):
        user_object = get_object_or_404(USER, id = request.user.id)
        user_form = UpdateUserForm(request.POST, instance = user_object)
        picture_form = UpdatePictureForm(
            request.POST,
            request.FILES, instance = user_object)
        
        if user_form.is_valid() and picture_form.is_valid():
            user_form.save()
            picture_form.save()
            print('Updated successfully')
            messages.success(request, 'Profile updated successfully')
            return redirect('/user/profile/')

        else:
            return HttpResponseBadRequest('Invalid data')
