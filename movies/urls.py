from django.urls import path
from .views import *


urlpatterns = [
    path('', MoviesView.as_view(), name='home'),
    path('<slug:slug>', MovieDetailView.as_view(), name='detail_view'),
    path('review/<int:pk>', AddReview.as_view(), name='add_review'),
]