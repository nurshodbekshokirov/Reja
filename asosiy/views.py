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
def reja_update(request, son):
    if request.method == 'POST':
        if request.POST.get('ba') == 'on':

            qiymat = True
        else:
            qiymat = False
        Reja.objects.filter(id=son).update(
            sarlavha = request.POST.get('s'),
            vaqt = request.POST.get('v'),
            batafsil = request.POST.get('b'),
            holat = qiymat
        )
        return redirect('/')
    data = {
        'reja':Reja.objects.get(id=son)
    }
    return render(request, 'todo_edit.html', data)






# Create your views here.
