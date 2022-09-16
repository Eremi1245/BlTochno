from django.contrib import admin

from .models import Category, Event, Habit, Habits_Events,HookaCategory,HookaComponent,HookaTobacco,HookaMixRecept

admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Habit)
admin.site.register(Habits_Events)
admin.site.register(HookaCategory)
admin.site.register(HookaComponent)
admin.site.register(HookaTobacco)
admin.site.register(HookaMixRecept)

