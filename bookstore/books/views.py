from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView

from .serializers import AuthorSerializer, BooksSerializers
from .models import Author, Books

# Create your views here.

"""----------------------Books Views--------------------------------"""

class Book_List(APIView):

    # def get_permissions(self):
    #     if self.request.method == 'POST':
    #         return [IsAdminUser(), IsAuthenticated()]
        
    #     return [AllowAny]

    permission_classes=[IsAuthenticated]

    def get(self, request):
        try:
            books = Books.objects.all()
        except Books.DoesNotExist:
            return Response({'error':'Database is Empty'}, status= status.HTTP_404_NOT_FOUND)
        else:
            serializers = BooksSerializers(books, many=True)
            return Response(serializers.data, status= status.HTTP_200_OK)
        
    def post(self, request):
        
        serializer = BooksSerializers(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status= status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status= status.HTTP_406_NOT_ACCEPTABLE)


class Book_Detail(APIView):

    # def get_permissions(self):
    #     if self.request.method in ['PUT','DELETE']:
    #         return [IsAdminUser(), IsAuthenticated()]
    #     elif self.request.method == 'PATCH':
    #         return [IsAuthenticated()]
    #     else:
    #         return [AllowAny()]
        
    def get(self, request, book_pk):
        try:
            book = Books.objects.get(pk=book_pk)
        except Books.DoesNotExist:
            return Response({'error':'Book does not exist'}, status= status.HTTP_404_NOT_FOUND)
        else:
            serializer = BooksSerializers(book)
            return Response(serializer.data, status= status.HTTP_200_OK)
    
    def put(self, request, book_pk):
        try:
            book = Books.objects.get(pk=book_pk)
        except Books.DoesNotExist:
            return Response({'error':'Book does not exist'}, status= status.HTTP_404_NOT_FOUND)
        else:
            serializer = BooksSerializers(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= status.HTTP_200_OK)
            else:
                return Response(serializer.error, status= status.HTTP_406_NOT_ACCEPTABLE)
    
    def patch(self, request, book_pk):
        try:
            book = Books.objects.get(pk=book_pk)
        except Books.DoesNotExist:
            return Response({'error':'Book does not exist'}, status= status.HTTP_404_NOT_FOUND)
        else:
            serializer = BooksSerializers(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= status.HTTP_200_OK)
            else:
                return Response(serializer.error, status= status.HTTP_406_NOT_ACCEPTABLE)
        
    def delete(self, request, book_pk):
        try:
            book = Books.objects.get(pk=book_pk)
        except Books.DoesNotExist:
            return Response({'error':'Book does not exist'}, status= status.HTTP_404_NOT_FOUND)
        else:
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


"""-----------------Author Views-----------------------------------"""

class Author_List(APIView):
    
    # def get_permissions(self):
    #     if self.request.method == 'POST':
    #         return [IsAdminUser]
    #     elif self.request.method == 'GET':
    #         return [AllowAny]
        
    def get(self, request):
        try:
            authors = Author.objects.all()
        except Author.DoesNotExist:
            return Response({'error':'Database is Empty'}, status= status.HTTP_404_NOT_FOUND)
        else:
            serializers = AuthorSerializer(authors, many=True)
            return Response(serializers.data, status= status.HTTP_200_OK)
        
    
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status= status.HTTP_406_NOT_ACCEPTABLE)
        


class Author_Detail(APIView):
    
    # def get_permissions(self):
    #     if self.request.method in ['PUT','PATCH','DELETE']:
    #         return [IsAdminUser()]
    #     else:
    #         return [AllowAny()]
        
    def get(self, request, author_pk):
        try:
            author =Author.objects.get(pk=author_pk)
        except Author.DoesNotExist:
            return Response({'error':'Author Does not Exist'}, status= status.HTTP_404_NOT_FOUND)
        else:
            serializer = AuthorSerializer(author)
            return Response(serializer.data, status= status.HTTP_200_OK)
        
    def put(self, request, author_pk):
        try:
            author = Author.objects.get(pk=author_pk)
        except Author.DoesNotExist:
            return Response({'error':'Author does not exist'}, status= status.HTTP_404_NOT_FOUND)
        else:
            serializer = AuthorSerializer(author, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
            
    def patch(self, request, author_pk):
        try:
            author = Author.objects.get(pk=author_pk)
        except Author.DoesNotExist:
            return Response({'error':'Author does not exist'}, status= status.HTTP_404_NOT_FOUND)
        else:
            serializer = AuthorSerializer(author, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
            
    def delete(self, request, author_pk):
        try:
            author = Author.objects.get(pk=author_pk)
        except Author.DoesNotExist:
            return Response({'error':'Author Does Not Exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            author.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        



        

