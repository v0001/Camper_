from django.urls import path, include
from .views import signup, profile
from django.contrib.auth.views import LoginView, LogoutView
# import loginapp.views

urlpatterns = [
    path('signup/', signup, name="signup"),
    path('signin/', LoginView.as_view(), name="signin"),
    path('signout/', LogoutView.as_view(), name="signout"),
    path('profile/<int:pk>', profile, name="profile"),
    path('accounts/', include('allauth.urls')),
]
