from django.urls import path

from . import views

urlpatterns = [
  # /books/
  path('', views.index, name='books.index'),
  # /books/add/
  path('add/', views.add, name='books.add'),
  # /books/save/
  path('save/', views.save, name='books.save'),
]