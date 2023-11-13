import json
from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import (
        HTTP_201_CREATED as ST_201,
        HTTP_204_NO_CONTENT as ST_204,
        HTTP_400_BAD_REQUEST as ST_400,
        HTTP_401_UNAUTHORIZED as ST_401,
        HTTP_409_CONFLICT as ST_409
)

from base import mods
from base.perms import UserIsStaff

class HomeView(TemplateView):
    template_name = 'home.html'

class HomeViewEsp(TemplateView):
    template_name = 'homeesp.html'

class HomeViewAlm(TemplateView):
    template_name = 'homeale.html'



    