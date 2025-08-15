from django.urls import path
from . import views
urlpatterns = [
    path('', views.Book_List.as_view(), name='books-list'),
    path('<int:book_pk>/book-detail/', views.Book_Detail.as_view(), name='book-detail'),
    path('authors/', views.Author_List.as_view(), name='authors-list'),
    path('<int:author_pk>/author-detail/', views.Author_Detail.as_view(), name='author-detail'),
]