from django.urls import path
from . import views

urlpatterns = [
    path('', views.Register_View.as_view(), name='register'),
    # path('login/',views.Login_View.as_view() , name='login'),
    # path('logout/', views.Logout_View.as_view(), name='logout'),
    path('books/', views.Books_List.as_view(), name='books-list'),
]