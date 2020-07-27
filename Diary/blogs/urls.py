from django.urls import path
from .views import Create, BlogListView, BlogUpdateView, BlogDeleteView

app_name = 'blogs'

urlpatterns = [
    path('create/', Create.as_view(), name = 'create'),
    path('list/', BlogListView.as_view(), name = 'list'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name = 'update'),

    path('delete/<int:pk>/', BlogDeleteView.as_view(), name = 'delete')
]