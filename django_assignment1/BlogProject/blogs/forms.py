from django.forms import ModelForm
from .models import Blog, Author

class BlogCreateModelForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'author']

class AuthorCreateModelForm(ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'dob']

