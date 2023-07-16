from django.urls import path
from . import views

urlpatterns = [
    path('/', views.search, name='search'),
    path('/search-autosuggest/', views.search_autosuggest, name='search_autosuggest'),
    path('/city_description/', views.city_description, name='city_description'),
    path('/country_description/', views.country_description, name='country_description'),
    path('/language_description/', views.language_description, name='language_description'),
]