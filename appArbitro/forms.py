from django.forms import ModelForm
from appArbitro.models import arbitro


class ArbitroForm(ModelForm):
    nombre = ModelForm.CharField(min_length= 3, max_length=100)
    apellido = ModelForm.CharField(min_length= 3, max_length=100)
    class Meta:
        model = arbitro 
        fields = '__all__'

    