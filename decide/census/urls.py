from django.urls import path, include
from . import views
from .views import *



urlpatterns = [
    path('', views.CensusList.as_view(), name="census_list"),
    path("search/", views.CensusResultsView.as_view(), name="search_results"),
    #path('', views.CensusCreate.as_view(), name='census_create'),
    path('<int:voting_id>/', views.CensusDetail.as_view(), name='census_detail'),
    path('export_csv/', ExportCensusCsv.as_view(), name='export_census_csv'),
    path('export_json/', ExportCensusJson.as_view(), name='export_census_json'),
    path('export_detail_csv/<int:census_id>/', ExportCensusDetailCsv.as_view(), name='export_census_detail_csv'),
    path('export_detail_json/<int:census_id>/', ExportCensusDetailJson.as_view(), name='export_census_detail_json'),
    path('peticion/', views.peticionCenso, name="peticion"),

]
