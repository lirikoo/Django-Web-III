from django.shortcuts import render, HttpResponse
from datetime import datetime

def registro_equipo(request):
    # 1. Corrección clave: Inicializar como diccionario
    contexto = {} 
    
    # Agregar la lista de integrantes
    contexto['integrantes'] = [
        'CRISTHIAN POMA RAMOS', 
        'GABRIEL ZEUS CUTILE LOPEZ', 
        'GARY ABEL CANAVIRI HUANCA', 
        'KEVIN OSCAR SANDOVAL', 
        'JHOJAN ALDAIR SANCHEZ LUIS'
    ] 
    
    if request.method == 'POST':
        # Obtener los datos del formulario
        nom_equipo = request.POST.get('nom_equipo')
        jefe = request.POST.get('jefe')
        membresia_str = request.POST.get('membresia')
        cantidad_str = request.POST.get('cantidad')

        try:
            # 2. Manejo de enteros y cálculo
            membresia = int(membresia_str or 0)
            cantidad = int(cantidad_str or 0)
            total = membresia * cantidad
            
            # Almacenar resultados para mostrar en el template
            contexto['nom_equipo'] = nom_equipo
            contexto['jefe'] = jefe
            contexto['membresia'] = membresia
            contexto['cantidad'] = cantidad
            contexto['total'] = total
            contexto['success'] = f'Cálculo realizado: {membresia} * {cantidad} = {total}'
        
        except ValueError:
            # 3. Manejo de errores de tipo de dato
            contexto['error'] = 'Asegúrate de ingresar números válidos para Membresía y Cantidad.'
            
            # Mantener los valores de texto no numéricos en caso de error
            contexto['nom_equipo'] = nom_equipo
            contexto['jefe'] = jefe

    # 4. Renderizado final: devuelve la respuesta con el contexto actualizado
    return render(request, 'formulario.html', contexto)