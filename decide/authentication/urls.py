from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from .views import GetUserView, VRegistro, cerrarSession


urlpatterns = [
    path('login/', obtain_auth_token,name='logear'),
    path('logout/', cerrarSession,name='cerrarSesion'),
    path('getuser/', GetUserView.as_view()),
    path('', VRegistro.as_view(), name="Autenticacion")
    # path('register/', RegisterView.as_view()),

]
