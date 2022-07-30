from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import requests

def addQuotes(request):
    # add 100 quotes
    url = "https://api.quotable.io/random?maxLength=150"

    for i in range(100):
        r = requests.get(url).json()
        quote = r["content"]
        author = r["author"]
        tags = r["tags"]

        # push this quote and author into Quote 
        quoteObj = Quote(category=tags[0], author=author, body=quote)
        quoteObj.save()

    return redirect(home)

def home(request):
    # search query
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    quotes = Quote.objects.filter(
        Q(body__icontains=search_query) |
        Q(author__icontains=search_query)
    )

    # pagination
    page = request.GET.get('page')
    results = 10
    paginator = Paginator(quotes, results)
    try:
        quotes = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        quotes = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        quotes = paginator.page(page)

    left_index = (int(page) - 4)
    if left_index < 1:
        left_index = 1

    right_index = (int(page) + 5)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages

    custom_range = range(left_index, right_index)

    context = {'quotes': quotes, 'search_query': search_query, 'paginator': paginator, 'custom_range': custom_range}

    # clean db
    # Quote.objects.all().delete()

    return render(request, 'home.html', context)

def authors(request):
    # search query
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    # handling author request
    if request.GET.get('author'):
        author = request.GET.get('author')
        quotes = Quote.objects.filter(author=author)
        context = {"quotes": quotes}
        return render(request, 'home.html', context=context)
    
    quotes = Quote.objects.filter(author__icontains=search_query)

    authors = set()
    for quote in quotes:
        authors.add(quote.author)

    context = {"authors": authors, "search_query": search_query}
    return render(request, 'authors.html', context)

def categories(request):
    # search query
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    # handling category request
    if request.GET.get('category'):
        category = request.GET.get('category')
        quotes = Quote.objects.filter(category=category)
        context = {"quotes": quotes}
        return render(request, 'home.html', context=context)

    quotes = Quote.objects.filter(category__icontains=search_query)

    categories = set()
    for quote in quotes:
        categories.add(quote.category)

    context = {"categories": categories, "search_query": search_query}
    return render(request, 'categories.html', context)

def quote_of_the_day(request):
    url = "https://api.quotable.io/random?maxLength=150"
    r = requests.get(url).json()
    quote = r["content"]
    author = r["author"]
    tags = r["tags"]

    quotes = Quote.objects.all()[:10]
    context = {'quotes':quotes, 'quote': quote, 'author':author, 'tag':tags[0]}
    return render(request, 'quote_of_the_day.html', context)