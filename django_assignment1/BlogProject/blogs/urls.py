from django.urls import path
from .views import blog_view, blog_create, create_author

app_name = 'blogs'

urlpatterns = [
    path('blog/', blog_view, name = 'blog'),
    path('create/', blog_create, name = 'create'),
    path('create-author/', create_author, name= 'create-author')

]