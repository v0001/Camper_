from django.urls import path
from .views import signup
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
   
    path('signup/',signup, name="signup" ),
    path('signin/',LoginView.as_view(), name="signin" ),
    path('signout/',LogoutView.as_view(), name="signout" ),
]
