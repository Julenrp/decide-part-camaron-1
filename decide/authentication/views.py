from rest_framework.response import Response
from rest_framework.status import (
        HTTP_201_CREATED,
        HTTP_400_BAD_REQUEST,
        HTTP_401_UNAUTHORIZED
)
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from .forms import CustomUserCreationForm
from .serializers import UserSerializer
from django.contrib import messages


class GetUserView(APIView):
    def post(self, request):
        key = request.data.get('token', '')
        tk = get_object_or_404(Token, key=key)
        return Response(UserSerializer(tk.user, many=False).data)


# class LogoutView(APIView):
#     def post(self, request):
#         key = request.data.get('token', '')
#         try:
#             tk = Token.objects.get(key=key)
#             tk.delete()
#         except ObjectDoesNotExist:
#             pass

#         return Response({})

class VRegistro(View):
    def get(self, request):
        form=CustomUserCreationForm()
        return render(request, "autentication/registro.html", {"form":form})
    
    def post(self, request):
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)
            return redirect('/')
        else:
            for mensaje in form.error_messages:
                messages.error(request, form.error_messages[mensaje])
            return render(request, "autentication/registro.html", {"form":form})

def cerrarSession(request):
    logout(request)
    return redirect('Home')

# class RegisterView(APIView):
#     def post(self, request):
#         key = request.data.get('token', '')
#         tk = get_object_or_404(Token, key=key)
#         if not tk.user.is_superuser:
#             return Response({}, status=HTTP_401_UNAUTHORIZED)

#         username = request.data.get('username', '')
#         pwd = request.data.get('password', '')
#         if not username or not pwd:
#             return Response({}, status=HTTP_400_BAD_REQUEST)

#         try:
#             user = User(username=username)
#             user.set_password(pwd)
#             user.save()
#             token, _ = Token.objects.get_or_create(user=user)
#         except IntegrityError:
#             return Response({}, status=HTTP_400_BAD_REQUEST)
#         return Response({'user_pk': user.pk, 'token': token.key}, HTTP_201_CREATED)
