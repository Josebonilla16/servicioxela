from django import forms
from .models import Cliente, Servicio, Carro

class CarroForm(forms.ModelForm):
#todos los campos de Pelicula
        class Meta:
            model = Carro
            fields = ('cliente', 'placa', 'marca','linea', 'modelo', 'color', 'servicios')

            def __init__ (self, *args, **kwargs):
                super(CarroForm, self).__init__(*args, **kwargs)
                self.fields["servicios"].widget = forms.widgets.CheckboxSelectMultiple()
                self.fields["servicios"].help_text = "Ingrese los Servicios que le aplico al Carro"
                self.fields["servicios"].queryset = Servicio.objects.all()
