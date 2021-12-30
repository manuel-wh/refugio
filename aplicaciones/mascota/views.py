# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import reset_queries

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.utils.translation import templatize
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from aplicaciones.mascota.forms import MascotaForm
from aplicaciones.mascota.models import Mascota
# Create your views here.

def index(request):
    return render(request, 'mascota/index.html')


def mascota_create(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listarFunction')
    else:
        form = MascotaForm()
    return render(request, 'mascota/mascota_form.html', {'form': form})

def mascota_list(request):
    mascota = Mascota.objects.all().order_by('id')
    contexto = {'mascotas': mascota}
    return render(request, 'mascota/mascota_list_fun.html', contexto)

def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id = id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else: 
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listarFunction')
    return render(request, 'mascota/mascota_form.html', {'form': form})

def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id = id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota:mascota_listarFunction')
    return render(request, 'mascota/mascota_delete_fun.html', {'mascota': mascota})

class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/mascota_list.html'

class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_listar' )

class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_listar' )

class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'mascota/mascota_delete.html'
    success_url = reverse_lazy('mascota:mascota_listar')