from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.CensusCreate.as_view(), name='census_create'),
    path('<int:voting_id>/', views.CensusDetail.as_view(), name='census_detail'),
    path('peticion/', views.peticionCenso, name="peticion"),
    path('census/', CensusView.as_view()),
    
]
