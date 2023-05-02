from django.shortcuts import render
from herencia_HTML.models import Persona, Vehiculo, Mascota
from herencia_HTML.forms import PersonaForm, MascotaForm, VehiculoForm, BuscarPersonasForm, BuscarVehiculosForm, BuscarMascotasForm
from django.views.generic import ListView

def index(request):
    return render(request, "herencia_HTML/index.html")

def mostrar_personas(request):
    persona = Persona.objects.all()
    context = {
        "Personas": persona,
        "Formulario": PersonaForm(),
    }

    return render(request, "herencia_HTML/persona.html", context)

def mostrar_mascotas(request):
    mascota = Mascota.objects.all()
    context = {
        "Mascotas": mascota, 
        "Formulario": MascotaForm()
    }
    return render(request, "herencia_HTML/mascota.html", context)

def mostrar_vehiculo(request):
    vehiculo = Vehiculo.objects.all()
    return render(request, "herencia_HTML/vehiculo.html", {"Vehiculos": vehiculo, "Formulario": VehiculoForm()})

def cargar_persona(request):
    f = PersonaForm(request.POST)

    context = {
        "Formulario": f
    }

    if f.is_valid():
        Persona(nombre=f.data['nombre'], apellido=f.data['apellido'], edad=f.data['edad']).save()
        
    f = PersonaForm(request.POST)

    persona = Persona.objects.all()
    context = {
        "Personas": persona,
        "Formulario": f,
    }
    context['Formulario'] = PersonaForm()
    return render(request, "herencia_HTML/persona.html", context)

class BuscarPersonas(ListView):
    model = Persona
    context_object_name = "Personas"

    def get_queryset(self):
        f = BuscarPersonasForm(self.request.GET)
        if f.is_valid():
            return Persona.objects.filter(nombre__icontains=f.data["criterio_nombre"]).all()
        return Persona.objects.none()

def cargar_vehiculo(request):
    f = VehiculoForm(request.POST)

    context = {
        "Formulario": f
    }

    if f.is_valid():
        Vehiculo(marca=f.data['marca'], version=f.data['version'], kilometraje=f.data['kilometraje']).save()
        
    f = VehiculoForm(request.POST)

    vehiculo = Vehiculo.objects.all()
    context = {
        "Vehiculos": vehiculo,
        "Formulario": f,
    }
    context['Formulario'] = VehiculoForm()
    return render(request, "herencia_HTML/vehiculo.html", context)

class BuscarVehiculo(ListView):
    model = Vehiculo
    context_object_name = "Vehiculos"

    def get_queryset(self):
        f = BuscarVehiculosForm(self.request.GET)
        if f.is_valid():
            return Vehiculo.objects.filter(marca__icontains=f.data["criterio_marca"]).all()
        return Vehiculo.objects.none()
    
def cargar_mascota(request):
    f = MascotaForm(request.POST)

    context = {
        "Formulario": f
    }

    if f.is_valid():
        Mascota(nombre=f.data['nombre'], tipo=f.data['tipo'], raza=f.data['raza'], edad=f.data['edad']).save()
        
    f = MascotaForm(request.POST)

    mascota = Mascota.objects.all()
    context = {
        "Mascotas": mascota,
        "Formulario": f,
    }
    context['Formulario'] = MascotaForm()
    return render(request, "herencia_HTML/mascota.html", context)

class BuscarMascota(ListView):
    model = Mascota
    context_object_name = "Mascotas"

    def get_queryset(self):
        f = BuscarMascotasForm(self.request.GET)
        if f.is_valid():
            return Mascota.objects.filter(tipo__icontains=f.data["criterio_tipo"]).all()
        return Mascota.objects.none()