from django.urls import path
from .views import signup_view, login_view, profile_view, logout_view
from .class_views import SignupView, Login_View, ProfileView, LogoutView, UpdateProfileView

app_name = 'user'

urlpatterns = [
    # path('signup/', signup_view),
    # path('login/', login_view),
    # path('profile/', profile_view),
    # path('logout/', logout_view),
    # path('update/<int:id>/', UpdateView.as_view()),

    path('signup/', SignupView.as_view()),
    path('login/', Login_View.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view()),

    path('update/<int:pk>/', UpdateProfileView.as_view())

]