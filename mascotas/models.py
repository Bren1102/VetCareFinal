from django.db import models
from django.contrib.auth.models import User

class Mascota(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100) # Perro, Gato, etc.
    breed = models.CharField(max_length=100)   # Raza
    age = models.IntegerField()
    weight = models.FloatField()
    furType = models.CharField(max_length=100) # Tipo de pelo
    furColor = models.CharField(max_length=100) # Color de pelo
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mascotas')
    
    def __str__(self):
        return f"{self.name} ({self.species})"

class Veterinaria(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Turno(models.Model):
    pet = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='turnos')
    veterinary = models.ForeignKey(Veterinaria, on_delete=models.CASCADE, related_name='turnos')
    dateTime = models.DateTimeField()
    reason = models.CharField(max_length=255)
    
    class Meta:
        unique_together = ['veterinary', 'dateTime']

    def __str__(self):
        return f"Turno: {self.pet.name} en {self.veterinary.name}"