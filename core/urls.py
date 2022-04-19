from django.urls import path
from .views import HomeView, ProfileListView, ProfileCreate


app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profile/', ProfileListView.as_view(), name='profile_list'),
    path('profile/create/', ProfileCreate.as_view(), name='profile_create'),
]