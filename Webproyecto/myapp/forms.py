from django import forms
from .models import PreguntaNoRespondida

class PreguntaForm(forms.ModelForm):
    class Meta:
        model = PreguntaNoRespondida
        fields = ['correo', 'pregunta']
