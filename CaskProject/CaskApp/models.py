from django.db import models

class Cliente(models.Model):
    idCliente = models.CharField(max_length= 100)
    nombre = models.CharField(max_length= 100)
    apellido = models.CharField(max_length= 100)
    direccion = models.CharField(max_length= 100)
    email = models.EmailField(max_length= 100)

    def __str__(self):
        return f"Cliente id: {self.idCliente} - {self.nombre}, {self.apellido}"

class Producto(models.Model):
    nombre = models.CharField(max_length= 100)
    codigo = models.CharField(max_length= 100)
    es_blend = models.BooleanField()
    edad = models.PositiveBigIntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.codigo}"

class Cata(models.Model):
    nombre = models.CharField(max_length= 100)
    fechaInicio = models.DateField()
    presencial = models.BooleanField()
    enVivo = models.BooleanField()

    def __str__(self):
        return f"{self.nombre}, {self.fechaInicio}"

class Compra(models.Model):
    idCompra = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f"Compra id: {self.idCompra} del cliente {self.cliente}"

