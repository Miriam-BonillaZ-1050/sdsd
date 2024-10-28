from django.shortcuts import render
from .models import Pago
# Create your views here.
def inicio_vista(request):
    # Obtener todos los registros de la tabla Materia
    Listadopagos=Pago.objects.all()
    return render(request, "pagos.html",{"lospagos":Listadopagos})
    