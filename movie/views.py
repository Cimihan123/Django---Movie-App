from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator ,EmptyPage,PageNotAnInteger
from django.db.models import Q
from django.views.generic.list import ListView
from django.http import HttpResponse

from django.views.generic.dates import YearArchiveView

# Create your views here.



def index(request):
    template_name = 'index.html'
    if request.method == 'GET':
        query_list = Movie.objects.filter()
        query = request.GET.get('search')
        if query:
            query_list  = Movie.objects.filter(
              Q(name__icontains=query )| Q(description__icontains=query)
                 )
   

    paginator = Paginator(query_list,3)
    page = request.GET.get('page')

    try:
        queries = paginator.page(page)
    
    except PageNotAnInteger:
        queries = paginator.page(1)
    
    except EmptyPage:
        queries = paginator.page(paginator.num_pages)

    context = {
        
       
        'movies' : queries,
       
        

    }
    return render(request,template_name,context)   



def detail(request,pk):  
    template_name = 'detail.html'
    movies = Movie.objects.get(pk=pk)
    context = {
        'movies' : movies       

    }
    return render(request,template_name,context)    


def genreView(request,genre):
  
    movies = Movie.objects.filter(genre=genre)
    paginator = Paginator(movies,3)
    page = request.GET.get('page')
    try:
        queries = paginator.page(page)
    
    except PageNotAnInteger:
        queries = paginator.page(1)
    
    except EmptyPage:
        queries = paginator.page(paginator.num_pages)
    context = {
        'movie_category' : queries,
        'movies' : queries    

    }
    return render(request, "genre.html", context)



def languageView(request,language):

    template_name = 'language.html'
    movies = Movie.objects.filter(language=language)
    paginator = Paginator(movies,3)
    page = request.GET.get('page')
    try:
        queries = paginator.page(page)
    
    except PageNotAnInteger:
        queries = paginator.page(1)
    
    except EmptyPage:
        queries = paginator.page(paginator.num_pages)
    context = {
        'movie_language' : queries,
        'movies' : queries
        

    }
    return render(request,template_name,context)   

class MovieArchiveView(YearArchiveView):

    paginate_by = 3
 
    queryset = Movie.objects.all()

    print(queryset)
    date_field = "release_date"
    make_object_list = True
    allow_future = True

