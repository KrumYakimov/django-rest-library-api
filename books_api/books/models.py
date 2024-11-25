from django.db import models

from books_api.books.choices import BookGenreChoices


class Book(models.Model):
    title = models.CharField(max_length=250)
    pages = models.IntegerField(default=0)
    description = models.TextField(default="")
    author = models.ManyToManyField(to="Author", related_name="books")
    genre = models.CharField(
        max_length=50,
        choices=BookGenreChoices.choices,
        default=BookGenreChoices.FICTION,
    )
    published_date = models.DateField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.get_genre_display()})"


class Author(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(
        max_length=100,
    )

    established_year = models.PositiveIntegerField()

    location = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    description = models.TextField()

    book = models.ForeignKey(
        to=Book,
        on_delete=models.CASCADE,
    )
