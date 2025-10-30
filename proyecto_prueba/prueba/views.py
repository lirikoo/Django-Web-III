from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.shortcuts import render
from .form import ClienteForm

# Create your views here.
def saludo(request):
    return HttpResponse("Hola Mundo Django - Primer proyecto")

def info_usuario(request):
    nombre = "Alan Brito"
    edad = 28
    return HttpResponse(f"Hola soy {nombre} y mi edad es {edad}")

def saludo_mejorado(request, nombre, edad):
    return HttpResponse(f"Hola soy {nombre} y mi edad es {edad}")

def tabla_multiplicacion(request):
    numero = 5
    resultado = ""
    for i in range(1, 11):
        resultado += f"{numero} x {i} = {numero * i}<br>"
    return HttpResponse(resultado)

def saludo2(request):
    datos = {
        'nombre': 'Alan Brito',
        'edad': 28,
    }
    return render(request, 'saludo.html', datos)

def info (request):
    return render (request, 'informacion.html')

def nuevo_saludo (request, nombre, edad):
    return render (request, 'nuevoSaludo.html', {'nombre': nombre, 'edad': edad})

#tabla de multiplicaion con parametro
def tabla_produto (request, numero):
    lista = []
    for i in range (1,11):
        res = f"{numero} * {i} = {numero * i}"
        lista.append (res)
    return render (request, 'tabla_multiplicaion.html', {'lista': lista, 'numero': numero})

def formulario_cliente(request):
    datos = None
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo') 
        año_nacimiento = request.POST.get('año_nacimiento')
        edad = datetime.now().year - int(año_nacimiento) 
        pais = request.POST.get('pais')
        
        datos = {
            'nombre': nombre,
            'correo': correo, 
            'edad': año_nacimiento,
            'año_nacimiento': año_nacimiento,
            'pais': pais,   
        }
    return render(request, 'formulario.html', {'datos':datos})

