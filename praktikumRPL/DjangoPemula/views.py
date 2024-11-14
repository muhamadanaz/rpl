from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  context = {
    'title' : 'Daftar Buku',
    'all_buku' : [
      [
        "belajar pemrograman python",
        2015
      ],
      [
        "html untuk pemula",
        2014
      ],
      [
        "membuat aplikasi dengan framework django",
        2020
      ],
    ]
  }
  return render(request, 'index.html', context)