from django import forms

from events.models import Event,Category


class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
