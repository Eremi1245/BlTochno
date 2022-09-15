from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()

class Category(models.Model):
    name=models.CharField(max_length=255)


    def __str__(self):
        return self.name

class Event(models.Model):
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(
        verbose_name='Название Ивента',
        max_length=255
        )
    dt=models.DateField(
        verbose_name='Дата Ивента',
        blank=False
    )
    tm=models.TimeField(
        verbose_name='Время Ивента'
    )
    desc = models.CharField(
        verbose_name='Подробное описание ивента'
        ,max_length=255)

    def __str__(self):
        return f'{self.name} {self.dt} {self.tm}'

class Habit(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(
        verbose_name='Привычка',
        max_length=255,
        )

    def __str__(self):
        return self.name

class Habits_Events(models.Model):
    habit_id=models.ForeignKey(Habit, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class HookaCategory(models.Model):
    name = models.CharField(
        verbose_name='Категория кальяна',
        max_length=255,
        )
    def __str__(self):
        return self.name
class HookaComponent(models.Model):
    name = models.CharField(
        verbose_name='Наименование компонента',
        max_length=255,
        )
    hook_category=models.ForeignKey(HookaCategory, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class HookaTobacco(models.Model):
    name = models.CharField(
        verbose_name='Наименование табака',
        max_length=255,
        )
    hook_category=models.ForeignKey(HookaComponent, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class HookaMixRecept(models.Model):
    name = models.CharField(
        verbose_name='Название Микса',
        max_length=255,
        )
    component=models.ForeignKey(HookaTobacco, on_delete=models.CASCADE)
    desc=models.CharField(
        verbose_name='Описание микса',
        max_length=255,
        )
    def __str__(self):
        return self.name