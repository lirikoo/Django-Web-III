from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    correo = forms.EmailField(label='Correo Electrónico')
    año_nacimiento = forms.IntegerField(label='Año de Nacimiento')
    pais = forms.CharField(label='País', max_length=100)