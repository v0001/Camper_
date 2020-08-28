from django.urls import path, include
from .views import signup, render_mypage, create_mypage
from django.contrib.auth.views import LoginView, LogoutView
# import loginapp.views

urlpatterns = [
    # path('', index, name="index"),
    path('signup/', signup, name="signup"),
    path('signin/', LoginView.as_view(), name="signin"),
    path('signout/', LogoutView.as_view(), name="signout"),
    path('mypage/<int:mp>', render_mypage, name="mypage"),
    path('accounts/', include('allauth.urls')),
    path('create_mypage/', create_mypage, name="create_mypage")
]
