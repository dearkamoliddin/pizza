from django import forms
from reservations.models import ReservationModel


class ReservationForm(forms.ModelForm):
    class Meta:
        model = ReservationModel
        fields = '__all__'
