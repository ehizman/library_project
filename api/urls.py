from django.urls import path

from books.views import BookAPIView

urlpatterns = [
    path('', BookAPIView.as_view())
]