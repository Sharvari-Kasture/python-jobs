from django import forms
from .models import Maker

class MakerForm(forms.ModelForm):
    class Meta:
        model = Maker
        fields = ['name', 'number_of_cars']  # Include only the editable fields in the form

    updated_at = forms.DateTimeField(
        label='Updated At',
        required=False,  # Make it non-required
        widget=forms.TextInput(attrs={'readonly': 'readonly'})  # Make it read-only
    )
