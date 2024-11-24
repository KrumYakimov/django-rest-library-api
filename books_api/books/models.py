from django.db import models

from books_api.books.choices import BookGenreChoices


class Book(models.Model):
    title = models.CharField(max_length=250)
    pages = models.IntegerField(default=0)
    description = models.TextField(default="")
    author = models.CharField(max_length=20)
    genre = models.CharField(
        max_length=50,
        choices=BookGenreChoices.choices,
        default=BookGenreChoices.FICTION
    )
    published_date = models.DateField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.get_genre_display()})"
