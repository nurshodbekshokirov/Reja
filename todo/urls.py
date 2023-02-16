
from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', Rejaview.as_view()),
    path('reja/<int:son>/', Reja_ochir.as_view()),
    path('reja_edit/<int:son>/', Reja_update.as_view()),
    path('', Loginview.as_view()),
    path('logout/', Logoutview.as_view()),
    path('register/', Register.as_view()),


]
