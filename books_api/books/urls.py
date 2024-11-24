from .import views
from django.urls import path

urlpatterns = [
    path("books/", views.ListBookView.as_view(), name="list-books"),
    path("books/<int:pk>/", views.DetailBookView.as_view(), name="detail-book")
]