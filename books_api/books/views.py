from rest_framework import status
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from books_api.books.models import Book, Publisher
from books_api.books.serializers import BookSerializer, PublisherSerializer, PublisherHyperlinkSerializer
from books_api.utils.helpers import serializer_valid


class BookViewSet(ModelViewSet):
    queryset = Book.objects.prefetch_related('author').all()
    serializer_class = BookSerializer

# class ListBookView(GenericAPIView, ListModelMixin):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     def get(self, request, *args, **kwargs):
#         """
#         Handles the GET request for listing books.
#         """
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         """
#         Handles the POST request for creating a new book.
#         """
#         serializer = self.get_serializer(data=request.data)
#         return serializer_valid(serializer)
#
#
# class DetailBookView(GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     def get(self, request, pk, *args, **kwargs):
#         """
#         Handles the GET request for retrieving a specific book.
#         """
#         book = self.get_object()
#         serializer = self.get_serializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk, *args, **kwargs):
#         """
#         Handles the PUT request for updating a book.
#         """
#         book = self.get_object()
#         serializer = self.get_serializer(book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, pk, *args, **kwargs):
#         """
#         Handles the DELETE request for deleting a book.
#         """
#         book = self.get_object()
#         book.delete()
#         return Response(
#             {"detail": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT
#         )
#
# class DetailBookView(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherHyperlinkView(ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherHyperlinkSerializer
