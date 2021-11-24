from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from rest_framework.generics import ListAPIView

from api.serializers import BookSerializer
from books.models import Book


class BookListView(ListView):
    template_name = 'book_list.html'
    queryset = Book.objects.all()
    context_object_name = 'books'


class BookAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
