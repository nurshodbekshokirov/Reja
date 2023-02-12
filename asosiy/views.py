from django.shortcuts import render, redirect
from .models import *

def reja(request):
    data = {
        'reja': Reja.objects.all()
    }
    return render(request, 'todo (2).html', data)

def reja_ochir(request, son):
    rejaa = Reja.objects.get(id=son)
    rejaa.delete()
    return redirect('/')


def reja_qosh(request):
    if request.method == 'POST':
        form = RejaForm(request.POST)
        if form.is_valid():
            form.save()


# Create your views here.
