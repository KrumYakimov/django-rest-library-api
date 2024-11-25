from rest_framework.routers import DefaultRouter

from .import views
from django.urls import path, include

# router = DefaultRouter()
# router.register('', PublisherViewSet)
#
# urlpatterns = [
#     path("books/", views.ListBookView.as_view(), name="list-books"),
#     path("books/<int:pk>/", views.DetailBookView.as_view(), name="detail-book"),
#     path('publisher-links/', views.PublisherHyperlinkView.as_view(), name='publisher-link'),
#     path('publishers/', include(router.urls))
#
# ]

router = DefaultRouter()
router.register(r'books', views.BookViewSet, basename='books')
router.register(r'publishers', views.PublisherViewSet, basename='publishers')

urlpatterns = [
    path('', include(router.urls)),  # Includes routes from the router
    path('publisher-links/', views.PublisherHyperlinkView.as_view(), name='publisher-link'),
]