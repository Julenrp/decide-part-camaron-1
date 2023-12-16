import json
from django.views.generic import TemplateView
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
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

from django.http import HttpResponse
import csv
import json



from django.shortcuts import render, redirect
from .forms import FormularioPeticion
from django.core.mail import EmailMessage



class CensusCreate(generics.ListCreateAPIView):
    permission_classes = (UserIsStaff,)

    def create(self, request, *args, **kwargs):
        voting_id = request.data.get('voting_id')
        voters = request.data.get('voters')
        try:
            for voter in voters:
                census = Census(voting_id=voting_id, voter_id=voter)
                census.save()
        except IntegrityError:
            return Response('Error try to create census', status=ST_409)
        return Response('Census created', status=ST_201)

    def list(self, request, *args, **kwargs):
        voting_id = request.GET.get('voting_id')
        voters = Census.objects.filter(voting_id=voting_id).values_list('voter_id', flat=True)
        return Response({'voters': voters})


class CensusDetail(generics.RetrieveDestroyAPIView):

    def destroy(self, request, voting_id, *args, **kwargs):
        voters = request.data.get('voters')
        census = Census.objects.filter(voting_id=voting_id, voter_id__in=voters)
        census.delete()
        return Response('Voters deleted from census', status=ST_204)

    def retrieve(self, request, voting_id, *args, **kwargs):
        voter = request.GET.get('voter_id')
        try:
            Census.objects.get(voting_id=voting_id, voter_id=voter)
        except ObjectDoesNotExist:
            return Response('Invalid voter', status=ST_401)
        return Response('Valid voter')

class ExportCensusCsv(View):
    def get(self, request):
        census_data = Census.objects.all()
        response = self.export_csv(census_data)
        return response
    
    def export_csv(self, census_data):
        if not census_data:
            return HttpResponse('No data to export CSV')
        
        counter = self.request.session.get('download_counter_csv', 1)
        filename = f"censusv{counter}.csv"
        self.request.session['download_counter_csv'] = counter + 1

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        writer = csv.writer(response)
        writer.writerow(['name', 'users', 'has_voted'])

        for data in census_data:
            # Convierte el objeto relacionado a una lista de valores
            users_list = list(data.users.values_list('username', flat=True)) if data.users.exists() else []
            writer.writerow([data.name, ', '.join(users_list), data.has_voted])

        return response
    
class ExportCensusJson(View):
    def get(self, request):
        census_data = Census.objects.all()
        response = self.export_json(census_data)
        return response
    
    def export_json(self, census_data):
        if not census_data:
            return HttpResponse('No data to export JSON')
        
        data = []
        for c in census_data:
            # Convierte el objeto ManyRelatedManager a una lista de valores
            users_list = list(c.users.values_list('username', flat=True)) if c.users.exists() else []
            data.append({'name': c.name, 'users': users_list,'has_voted': c.has_voted})
        data_json = json.dumps(data, indent=2)  # indent=2 para una salida JSON más legible
        counter = self.request.session.get('download_counter', 1)
        filename = f"censusv{counter}.json"
        self.request.session['download_counter'] = counter + 1

        response = HttpResponse(data_json, content_type='application/json; charset=utf-8')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        return response

        



def peticionCenso(request):
    formulario_Peticion = FormularioPeticion()

    if request.method == "POST":
        formulario_Peticion = FormularioPeticion(data=request.POST)
        if formulario_Peticion.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            email2 = EmailMessage("Peticion de censo","El usuario con nombre {} y correo {} solicita:\n\n{}"
                                  .format(nombre, email, contenido),"",["nanomotors33@gmail.com"],reply_to=[email])
            try:
                email2.send()
                return redirect("http://127.0.0.1:8000/census/peticion/?valido")
            except:
                return redirect("http://127.0.0.1:8000/census/peticion/?novalido")

    return render(request, "peticion/peticion.html", {"miFormulario":formulario_Peticion})

    
class CensusView(TemplateView):
    template_name = 'census.html'