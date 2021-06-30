from django.db import models

from django.urls import reverse

# Create your models here.
class Beneficio(models.Model):
	name = models.TextField(unique=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('home')

class Paquete(models.Model):
	name = models.TextField()
	amount = models.FloatField(default=0.0)
	order = models.PositiveIntegerField()
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('home')


class BeneficioPaquete(models.Model):
	benefit = models.ForeignKey(Beneficio,related_name='beneficios',on_delete=models.PROTECT)
	package = models.ForeignKey(Paquete,related_name='paquetes',on_delete=models.PROTECT) 

	def get_absolute_url(self):
		return reverse('home')