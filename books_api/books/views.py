from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from books_api.books.models import Book
from books_api.books.serializers import BookSerializer
from books_api.utils.decoradors import generate_schema
from books_api.utils.helpers import get_object, serializer_valid


@extend_schema_view(
    get=generate_schema(BookSerializer, many=True, description="Retrieve a list of all books"),
    post=generate_schema(BookSerializer, description="Create a new book"),
)
class ListBookView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        return serializer_valid(serializer)


@extend_schema_view(
    get=generate_schema(BookSerializer, description="Retrieve a specific book by ID"),
    put=generate_schema(BookSerializer, description="Update an existing book"),
    delete=extend_schema(
        responses={204: None},
        description="Delete a book by ID (No Content)",
    ),
)
class DetailBookView(APIView):
    def get(self, request, pk):
        book = get_object(Book, pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        book = get_object(Book, pk)
        serializer = BookSerializer(book, data=request.data)
        return serializer_valid(serializer)

    def delete(self, request, pk):
        book = get_object(Book, pk)
        book.delete()
        return Response(status=status.HTTP_200_OK)





