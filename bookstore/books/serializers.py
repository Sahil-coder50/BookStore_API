from rest_framework import serializers
from .models import Author, Books

class AuthorSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Author
        fields = '__all__'

class BooksSerializers(serializers.ModelSerializer):

    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Books
        fields = '__all__'



