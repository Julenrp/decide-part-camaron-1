from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django.shortcuts import render
from django.contrib import sessions
from django.views.generic import TemplateView,ListView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import (
        HTTP_201_CREATED as ST_201,
        HTTP_204_NO_CONTENT as ST_204,
        HTTP_400_BAD_REQUEST as ST_400,
        HTTP_401_UNAUTHORIZED as ST_401,
        HTTP_409_CONFLICT as ST_409
)

from base.perms import UserIsStaff
from django.contrib.auth.models import User
from .models import Census
from voting.models import Voting
from .forms import FormularioPeticion

class FormularioPeticion(ListView):
    model = Census

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        censo = Census.objects.all()
        context['name'] = sorted(censo, key=lambda obj: obj.name.lower())
        return context

class CensusResultsView(ListView):
    model = Census
    template_name = 'census/results.html'

    def get_context_data(self,*args,**kwargs):  # new
        query = self.request.GET.get("census_id")
        census = Census.objects.get(id=query)
        object_list = census.users.all()
        voting_list = Voting.objects.filter(census=query)
        context = super(CensusResultsView, self).get_context_data(*args,**kwargs)
        context['object_list'] = object_list
        context['voting_list'] = voting_list
        context['censo_id'] = query
        print(context)
        return context
