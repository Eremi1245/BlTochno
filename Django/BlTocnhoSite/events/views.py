from datetime import date, datetime, timedelta

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from events.forms import AddEventForm, AddCategoryForm,EditCategoryForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from events.models import Event, Category, Habit, Habits_Events
from events.view.event import get_all_events
from secret import home_url

