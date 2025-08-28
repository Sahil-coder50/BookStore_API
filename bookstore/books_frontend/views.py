from django.shortcuts import render, redirect

# Create your views here.

"""  Bookstore FrontEnd  """

import requests
from django.views import View

API_BASE_URL = "http://127.0.0.1:8000/api/users/"

class Register_View(View):
    def post(self, request):
        data = {
            "username":request.POST.get("username"),
            "password1":request.POST.get("password1"),
            "password2":request.POST.get("password2")
        }
        response = requests.post(f"{API_BASE_URL}register/",data=data)

        if response.status_code == 200:
            return redirect("books-list")
        else:
            return render(request, "signup.html",{"error":response.json()})
        
    def get(self, request):
        return render(request, "signup.html")

API_BOOKS_URL = "http://127.0.0.1:8000/api/books/"
class Books_List(View):
    def get(self, request):
        response = requests.get(f"{API_BOOKS_URL}")

        print("API Response:", response.status_code, response.text)

        if response.status_code == 200:
            return redirect("books-list")
        else:
            return render(request, "books_list.html",{"error":response.json()})
