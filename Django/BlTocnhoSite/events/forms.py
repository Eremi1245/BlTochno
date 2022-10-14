from django import forms

from events.models import Event


class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

