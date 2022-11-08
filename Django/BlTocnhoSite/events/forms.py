from django import forms

from events.models import Event,Category,Habit,Habits_Events


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


class Habits_EventsForm(forms.ModelForm):
    class Meta:
        model = Habits_Events
        fields = ['habit_id','event_id']

