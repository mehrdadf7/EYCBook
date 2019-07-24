from django import forms
from .models import *


class FavoriteEquipmentForm(forms.ModelForm):
    class Meta:
        model = FavoriteEquipment
        fields = ['title', 'image']