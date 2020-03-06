from django.shortcuts import render
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):
  if request.method == 'POST':
    form = ListForm(request.POST or None)

    if form.is_valid():
      form.save()
      all_items = List.objects.all
      messages.success(request, ('Item has been added to list!'))
      return render(request, 'home.html', {'all_items': all_items})

  else:
    all_items = List.objects.all
    return render(request, 'home.html', {'all_items': all_items})

def about(request):
  # also can define a dictionary (usually named context) here and refer to it in render()
  my_name = 'Na Hyung Choi'
  number = 2 + 2
  return render(request, 'about.html', {'name': my_name, 'age': number})