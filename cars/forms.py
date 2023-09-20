from django import forms
from .models import Maker

class MakerForm(forms.ModelForm):
    class Meta:
        model = Maker
        fields = ['name', 'number_of_cars']  # Customize the fields as needed
        labels = {
            'name': 'Maker Name',
            'number_of_cars': 'Number of Cars',
        }
