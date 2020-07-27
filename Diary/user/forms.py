from django import forms  
from .models import User


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    profile_pic = forms.ImageField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=200, widget=forms.PasswordInput())

    def clean_email(self):
        if User.objects.filter(email = self.cleaned_data['email']).exists():
            raise forms.ValidationError('This email is already taken.')
        return self.cleaned_data['email']

    # def clean_confirm_password(self):
    #     if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
    #         raise forms.ValidationError('Password and confirm password do not match.')

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password != confirm_password:
            raise forms.ValidationError('Password and confirm password do not match.')

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())

    def clean(self):
        pass

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

class UpdatePictureForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_pic']

        
