from django import forms

class FormularioContactos(forms.Form):

    asunto = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField()