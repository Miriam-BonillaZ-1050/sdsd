from django.db import models

class Pago(models.Model):
    Id_pago = models.CharField(primary_key=True, max_length=10)
    Fecha = models.DateField() 
    Monto = models.DecimalField(max_digits=10, decimal_places=2)
    Contraseña = models.CharField(max_length=50)
    Efectivo_o_Tarjeta = models.CharField(max_length=20)

    def __str__(self):
        return f'Pago {self.Id_pago} - Monto: {self.Monto} - Contraseña: {self.Contraseña} - Efectivo o Tarjeta: {self.Efectivo_o_Tarjeta}'

