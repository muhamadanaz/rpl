from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Book


def index(request):
  context = {
      'book_list' : Book.objects.all()
  }
  return render(request, "books/index.html", context)
    
def add(request):
    return render(request, "books/form.html")

def save(request):
    buku = Book(
        judul = request.POST['judul'],
        publish = request.POST['publish'],
    )
    buku.save()

    return HttpResponseRedirect("/books/")