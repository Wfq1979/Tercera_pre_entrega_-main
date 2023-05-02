from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    edad = forms.CharField(max_length=10)


class VehiculoForm(forms.Form):
    marca = forms.CharField(max_length=50)
    version = forms.CharField(max_length=50)
    kilometraje = forms.CharField(max_length=10)

class MascotaForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    tipo = forms.CharField(max_length=10) # Perro, Gato, Ave...
    raza = forms.CharField(max_length=50)
    edad = forms.CharField(max_length=10)

class BuscarPersonasForm(forms.Form):
    criterio_nombre = forms.CharField(max_length=100)

class BuscarVehiculosForm(forms.Form):
    criterio_marca = forms.CharField(max_length=100)

class BuscarMascotasForm(forms.Form):
    criterio_tipo = forms.CharField(max_length=100)