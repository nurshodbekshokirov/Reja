
from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', reja),
    path('reja/<int:son>/', reja_ochir),
]
