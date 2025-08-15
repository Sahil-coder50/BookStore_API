from django.contrib import admin
from .models import Author, Books

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id','name','biography']
    list_display_links = ['name']

class BooksAdmin(admin.ModelAdmin):
    list_display = ['id','title','author','published_date','price','stock']
    list_display_links = ['title']

admin.site.register(Author,AuthorAdmin)
admin.site.register(Books,BooksAdmin)
