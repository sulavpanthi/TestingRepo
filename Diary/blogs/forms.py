from django import forms  
from .models import Blog

class BlogCreateModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content'] 
        # author removed