from django.urls import path
from . import views

urlpatterns = [
    path('getmovies',views.GetMovies.as_view())
]