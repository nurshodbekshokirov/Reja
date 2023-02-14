
from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', reja),
    path('reja/<int:son>/', reja_ochir),
    path('reja_edit/<int:son>/', reja_update),
    path('', loginview),
    path('logout/', logoutview),
    path('register/', register),


]
