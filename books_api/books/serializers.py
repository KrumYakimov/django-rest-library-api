from rest_framework import serializers, status
from rest_framework.response import Response

from books_api.books.models import Book, Author, Publisher
from books_api.utils.helpers import get_object


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name"]


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"

    def create(self, validated_data):
        authors = validated_data.pop("author")

        authors_objects = self._get_or_create_authors(authors)

        book = Book.objects.create(**validated_data)
        book.author.add(*authors_objects)

        return book

    def update(self, instance, validated_data):
        authors = validated_data.pop("author", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if authors is not None:
            authors_objects = self._get_or_create_authors(authors)
            instance.author.set(authors_objects)

        instance.save()
        return instance

    @staticmethod
    def _get_or_create_authors(authors):
        """
        Handles creating or retrieving authors and returning the objects.
        """
        authors_names = [a["name"] for a in authors]

        existing_authors = Author.objects.filter(name__in=authors_names)
        existing_authors_names = set(existing_authors.values_list("name", flat=True))

        new_authors_names = set(authors_names) - existing_authors_names
        new_authors = [Author(name=name) for name in new_authors_names]

        created_authors = Author.objects.bulk_create(new_authors)

        return list(existing_authors) + list(created_authors)

    def delete(self, request, pk):
        book = get_object(Book, pk=pk)
        book.delete()
        return Response(
            {"detail": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"


class PublisherHyperlinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"
