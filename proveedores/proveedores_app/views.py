from django.shortcuts import render
from .models import Proveedores

# Create your views here.

def inicio_vista(request):
    # Obtener todos los registros de la tabla Materia
    ListaProveedores=Proveedores.objects.all()
    return render(request,"gestionarProveedor.html",{"proveedores":ListaProveedores})