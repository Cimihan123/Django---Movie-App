
from django.urls import path, include
from . import views
from .views import MovieArchiveView

app_name = 'try'

urlpatterns = [
   path('', views.index, name='index'),
   path('detail/<str:pk>', views.detail, name='detail'),
   path('genre/<str:genre>', views.genreView, name='genre'),
   path('language/<str:language>', views.languageView, name='language'),
   path('year/<int:year>', MovieArchiveView.as_view(), name='year'),
]
