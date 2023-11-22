from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CensusForm.as_view(), name="census_list"),
    path("search/", views.CensusResultsView.as_view(), name="search_results"),

]
