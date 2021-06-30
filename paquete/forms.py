from django import forms

from paquete.models import Beneficio, Paquete, BeneficioPaquete

class BeneficioForm(forms.ModelForm):
    class Meta:
        model = Beneficio
        fields = ('name', )

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)


class PaqueteForm(forms.ModelForm):
    class Meta:
        model = Paquete
        fields = ('name', 'amount', 'order', 'active')

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

class BeneficioPaqueteForm(forms.ModelForm):
    class Meta:
        model = BeneficioPaquete
        fields = ('package', 'benefit')

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)