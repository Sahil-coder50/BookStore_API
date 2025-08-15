from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login_User.as_view(), name='login-user'),
    # path('logout/', views.Logout_User.as_view(), name='logout-user'),
    path('register/', views.Register_User.as_view(), name='register'),
    path('profile-view/', views.Profile_View.as_view(), name='profile-view')
]