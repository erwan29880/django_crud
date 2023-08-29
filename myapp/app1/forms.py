from django import forms
from app1.models import Adresses

# formulaire pour création, mise à jour d'une entrée
class GensForm(forms.ModelForm):
   class Meta:
      model = Adresses
      fields = '__all__'