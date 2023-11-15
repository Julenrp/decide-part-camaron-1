from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.CensusView.as_view()),
    path("search/", views.CensusResultsView.as_view(), name="search_results"),

]
