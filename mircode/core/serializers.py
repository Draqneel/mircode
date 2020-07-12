from .models import *
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class AuthorSerializer(ModelSerializer):
    author_name = serializers.SerializerMethodField()
    author_books = serializers.SerializerMethodField()
    author_books_count = serializers.SerializerMethodField()

    def get_author_books_count(self, obj):
        return len(self.get_author_books(obj))

    def get_author_books(self, obj):
        qs = Book.objects.filter(author=obj)
        return BookSerializer(qs, many=True).data

    def get_author_name(self, obj):
        return obj.get_full_name()

    class Meta:
        model = Author
        fields = ['author_name', 'author_books', 'author_books_count']


class BookSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class PurchaseRequestSerializer(ModelSerializer):
    comment = serializers.CharField(allow_blank=True, allow_null=True, default='', max_length=255)

    class Meta:
        model = PurchaseRequest
        fields = ('book', 'user', 'phone', 'comment')
