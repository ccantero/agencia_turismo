from django.shortcuts import render

from django.views import generic
from paquete import forms
from paquete.models import Beneficio, Paquete, BeneficioPaquete

# Create your views here.
class CreateBeneficio(generic.CreateView):
	form_class = forms.BeneficioForm
	model = Beneficio

	def get_context_data(self, **kwargs):
	 	context = super().get_context_data(**kwargs)
	 	return context

class CreatePaquete(generic.CreateView):
	form_class = forms.PaqueteForm
	model = Paquete

	def get_context_data(self, **kwargs):
	 	context = super().get_context_data(**kwargs)
	 	return context	 	

class CreateBeneficioPaquete(generic.CreateView):
	form_class = forms.BeneficioPaqueteForm
	model = BeneficioPaquete

	def get_context_data(self, **kwargs):
	 	context = super().get_context_data(**kwargs)
	 	return context	 	

class ListBeneficio(generic.ListView):
	model = Beneficio

class ListPaquete(generic.ListView):
	model = Paquete	

class ListBeneficioPaquete(generic.ListView):
	model = BeneficioPaquete		