# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.shortcuts import redirect, render, render_to_response
from django.http import HttpResponse
from django.urls import reverse_lazy
# Create your views here.

# Importar modelos
from aplicaciones.adopcion.models import Solicitud, Persona

# Importar forms
from aplicaciones.adopcion.forms import PersonaForm, SolicitudForm

def index_adopcion(request):
    return HttpResponse("Index Adopcion") 

def solicitud_listar(request):
    solicitud = Solicitud.objects.all()
    contexto = {"solicitudes": solicitud}
    return render(request, 'adopcion/solicitud_list_fun.html', contexto)

def solicitud_crear(request):
    form = SolicitudForm()
    form2 = PersonaForm()

    if request.method == "POST":
        form = SolicitudForm(request.POST)
        form2 = PersonaForm(request.POST)

        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit = False)
            solicitud.persona = form2.save()
            solicitud.save()
        return redirect('adopcion:solicitud_listarFuncion')
    context = { "form": form, "form2": form2 }
    return render(request, 'adopcion/solicitud_form.html', context=context)

class SolicitudList(ListView):
    model = Solicitud
    template_name = 'adopcion/solicitud_list.html'

class SolicitudCreate(CreateView):
    model = Solicitud
    template_name = 'adopcion/solicitud_form.html'
    form_class = SolicitudForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('adopcion:solicitud_listar')

    def get_context_data(self, **kwargs ):
        contexto = super(SolicitudCreate, self).get_context_data(**kwargs)
        if 'form' not in contexto:
            contexto['form'] = self.form_class(self.request.GET)
        if 'form2' not in contexto:
            contexto['form2'] = self.second_form_class(self.request.GET)  
        return contexto

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit = False)
            solicitud.persona = form2.save()
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else: 
            return self.render_to_response(self.get_context_data(form=form, form2=form2))