from django.shortcuts import render, redirect
from django.views import View

from .models import *
from .forms import *
from django.contrib.auth import authenticate, login,logout

class Rejaview(View):

    def get(self,request):
        if request.user.is_authenticated:
            data = {
                'reja': Reja.objects.filter(foydalanuvchi=request.user),
                'forma': RejaForm
            }
            return render(request, 'todo (2).html', data)
        return redirect('/')

    def post(self, request):
        if request.user.is_authenticated:


            form = RejaForm(request.POST)
            if form.is_valid():
                animal = form.save(commit=False)
                animal.foydalanuvchi = request.user
                animal.save()
                return redirect('/todo/')
        return redirect('/')



class Reja_ochir(View):
    def get(self,request, son):
        rejaa = Reja.objects.get(id=son)

        if rejaa.foydalanuvchi == request.user:

            rejaa.delete()
            return redirect('/todo/')
class Reja_update(View):
    def get(self,request, son):
        plan = Reja.objects.get(id=son).foydalanuvchi
        if plan == request.user:

            if request.user.is_authenticated:
                data = {
                    'reja': Reja.objects.get(id=son)
                }
                return render(request, 'todo_edit.html', data)
    def post(self, request, son):
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
                return redirect('/todo/')




class Loginview(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        user = authenticate(username = request.POST.get('l'),
                     password = request.POST.get('p'))
        if user is None:
            return redirect("/")
        login(request, user)
        return redirect('/todo/')



class Logoutview(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class Register(View):
    def get(self, request):
        return render(request, 'register.html')
    def post(self, request):


        if request.POST.get('p') == request.POST.get('cp'):

            User.objects.create_user(
                username = request.POST.get('l'),
                password =  request.POST.get('p')

            )
            return redirect('/')







# Create your views here.
