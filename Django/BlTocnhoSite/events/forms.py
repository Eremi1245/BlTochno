from django import forms

from events.models import Event,Category,Habit


class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class EditCategoryForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = '__all__'