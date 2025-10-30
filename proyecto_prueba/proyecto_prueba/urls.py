"""
URL configuration for proyecto_prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py corregido

from django.contrib import admin
from django.urls import path
from prueba import views as views_prueba
from Participacion import views as views_part

urlpatterns = [
    path('admin/', admin.site.urls),
    # Vistas de 'prueba'
    path('saludo/', views_prueba.saludo),
    path('info_usuario/', views_prueba.info_usuario),
    path('saludov2/<str:nombre>/<int:edad>/', views_prueba.saludo_mejorado),
    path('tabla_mul/', views_prueba.tabla_multiplicacion),
    path('saludo2/', views_prueba.saludo2, name='saludo2'),
    path('informacion/', views_prueba.info, name='informacion'),
    path('nuevo-saludo/<str:nombre>/<int:edad>/', views_prueba.nuevo_saludo, name='nuevo_saludo'),
    path('tabla_multi/<int:numero>/', views_prueba.tabla_produto, name='tabla_producto'),
    path('formulario/', views_prueba.formulario_cliente, name='formulario'),
    path('nuevo/', views_prueba.formulario_cliente, name='crear_cliente'),
    path('participacion/', views_part.registro_equipo, name='registro_equipo'), 
]