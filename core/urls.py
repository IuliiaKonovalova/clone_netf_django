from django.urls import path
from .views import (
    HomeView,
    ProfileListView,
    ProfileCreate,
    WatchView,
    ShowMovieDetailView,
    ShowMovieView,
)


app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profile/', ProfileListView.as_view(), name='profile_list'),
    path('profile/create/', ProfileCreate.as_view(), name='profile_create'),
    path('watch/<str:profile_id>/', WatchView.as_view(), name='movie_list'),
    path(
        'movie/<str:movie_id>/',
        ShowMovieDetailView.as_view(),
        name='movie_detail'
    ),
    path('movie/detail/<str:movie_id>/',ShowMovieDetailView.as_view(),name='show_detail'),
    path('movie/play/<str:movie_id>/',ShowMovieView.as_view(),name='show_movie')
    
]