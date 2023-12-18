from django.urls import path
from .views import VisualizerView, listarVotacion


urlpatterns = [
    path('<int:voting_id>/', VisualizerView.as_view(), name="Visualizar"),
    path('verVotaciones/',listarVotacion,name="VerVotaciones")
]
