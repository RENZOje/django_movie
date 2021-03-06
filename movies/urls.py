from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('', MoviesView.as_view(), name='home'),
    path('filter/', FilterMoviesView.as_view(), name='filter'),
    path('json-filter/', JsonFilterMoviesView.as_view(), name='json_filter'),
    path('add-rating/', AddStarRating.as_view(), name='add_rating'),
    path('<slug:slug>', MovieDetailView.as_view(), name='detail_view'),
    path('review/<int:pk>', AddReview.as_view(), name='add_review'),
    path('actor/<str:slug>', ActorView.as_view(), name='detail_actor')
]
