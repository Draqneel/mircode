from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework_jwt import authentication

from .models import Author, Book
from .serializers import BookSerializer, PurchaseRequestSerializer, AuthorSerializer


class AuthorsListAPIView(ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BooksListAPIView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class PurchaseRequestCreateAPIView(CreateAPIView):
    serializer_class = PurchaseRequestSerializer

