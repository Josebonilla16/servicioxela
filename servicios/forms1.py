from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
#todos los campos de Pelicula
        class Meta:
            model = Cliente
            fields = ('cliente', 'telefono')
