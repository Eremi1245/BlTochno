from django.shortcuts import render
from django.http import HttpResponse
from events.forms import AddCategoryForm
from django.shortcuts import redirect

def add_new_category(request):
    if request.method == 'POST':
        category_form = AddCategoryForm(request.POST or None)

        if category_form.is_valid():
            category = category_form.save(commit=False)
            category.save()

            return redirect('new_event')
        else:
            return HttpResponse(category_form.errors)
    else:
        category_form = AddCategoryForm()
    return render(request, 'calendar/category/new_category.html', {'category_form': category_form})
