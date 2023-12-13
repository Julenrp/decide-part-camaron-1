from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from .views import GetUserView, VRegistro, cerrarSession


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('logout/', cerrarSession, name='logout'),
    path('getuser/', GetUserView.as_view(), name='getUser'),
    path('', VRegistro.as_view(), name="Autenticacion")

]
