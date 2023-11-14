from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views.generic import TemplateView
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
from .models import Census


class CensusView(TemplateView):
    template_name = 'census/index.html'
    permission_classes = (UserIsStaff,)

    def list(self, request):
        print('Hola maricon')
        census_list = Census.objects.all()
        context = {'census_list': census_list}
        print(context)

        if request.method == "POST":
            census_id = request.POST.get('census_id')
            voters = Census.objects.filter(id=census_id)
            context['users_in_census'] = voters
        return render(request, "census/index.html", context=context)

