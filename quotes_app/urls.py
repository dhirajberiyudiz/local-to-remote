from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add-quotes/', views.addQuotes, name="add-quotes"),
    path('authors/', views.authors, name="authors"),
    path('categories/', views.categories, name="categories"),
    path('quote-of-the-day/', views.quote_of_the_day, name="quote_of_the_day"),
]
