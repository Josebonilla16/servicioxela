from django import forms
from .models import Servicio

class ServicioForm(forms.ModelForm):
#todos los campos de Pelicula
        class Meta:
            model = Servicio
            fields = ('nombre',)
