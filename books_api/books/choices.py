from django.db import models


class BookGenreChoices(models.TextChoices):
    FICTION = "FI", "Fiction"
    NON_FICTION = "NF", "Non-Fiction"
    MYSTERY = "MY", "Mystery"
    SCIENCE_FICTION = "SF", "Science Fiction"
    FANTASY = "FA", "Fantasy"
    ROMANCE = "RO", "Romance"
    HORROR = "HO", "Horror"
    BIOGRAPHY = "BI", "Biography"
    HISTORY = "HI", "History"
    POETRY = "PO", "Poetry"
