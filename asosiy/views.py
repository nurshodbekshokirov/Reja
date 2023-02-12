from django.shortcuts import render, redirect
from .models import *
from .forms import *

def reja(request):
    if request.method == 'POST':
        form = RejaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    data = {
        'reja': Reja.objects.all(),
        'forma':RejaForm
    }
    return render(request, 'todo (2).html', data)

def reja_ochir(request, son):
    rejaa = Reja.objects.get(id=son)
    rejaa.delete()
    return redirect('/')







# Create your views here.
