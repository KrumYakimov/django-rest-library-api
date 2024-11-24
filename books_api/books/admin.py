from django.contrib import admin
from django.contrib.admin import ModelAdmin

from books_api.books.models import Book


@admin.register(Book)
class BookAdmin(ModelAdmin):
    pass
