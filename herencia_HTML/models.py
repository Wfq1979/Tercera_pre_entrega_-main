from django.db import models

class Persona(models.Model):
    nombre = models.TextField(max_length=100)
    apellido = models.TextField(max_length=100)
    edad = models.TextField(max_length=10)

    def __str__(self):
        return f"{self.id} -\t{self.nombre} -\t{self.apellido}"
    
class Vehiculo(models.Model):
    marca = models.TextField(max_length=50)
    version = models.TextField(max_length=50)
    kilometraje = models.TextField(max_length=10)


    def __str__(self):
        return f"\t{self.id} -\t{self.marca} -\t{self.version}"

class Mascota(models.Model):
    nombre = models.TextField(max_length=50)
    tipo = models.TextField(max_length=10) # Perro, Gato, Ave...
    raza = models.TextField(max_length=50)
    edad = models.TextField(max_length=10)

    def __str__(self):
        return f"{self.id} -\t{self.nombre} -\t{self.raza} -\t {self.edad} años"
    

