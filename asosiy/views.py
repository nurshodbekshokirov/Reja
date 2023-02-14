from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login,logout

def reja(request):
    if request.user.is_authenticated:
        if request.method == 'POST':

            form = RejaForm(request.POST)
            if form.is_valid():
                animal = form.save(commit=False)
                animal.foydalanuvchi = request.user
                animal.save()
                return redirect('/todo/')
        data = {
            'reja': Reja.objects.filter(foydalanuvchi=request.user),
            'forma':RejaForm
        }
        return render(request, 'todo (2).html', data)
    return redirect('/')

def reja_ochir(request, son):
    rejaa = Reja.objects.get(id=son)
    rejaa.delete()
    return redirect('todo/')
def reja_update(request, son):
    if request.user.is_authenticated:
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
            return redirect('todo/')
        data = {
            'reja':Reja.objects.get(id=son)
        }
        return render(request, 'todo_edit.html', data)



def loginview(request):
    if request.method == 'POST':
        user = authenticate(username = request.POST.get('l'),
                     password = request.POST.get('p'))
        if user is None:
            return redirect("/")
        login(request, user)
        return redirect('/todo/')

    return render(request, 'login.html')

def logoutview(request):
    logout(request)
    return redirect('/')






# Create your views here.
