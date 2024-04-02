from django.shortcuts import render
from django.views.generic import ListView
from testapp.models import Book
# Create your views here.
class BookListView(ListView):
    model = Book
    #template File:book_list.html
    #conetext object: book_list
    


