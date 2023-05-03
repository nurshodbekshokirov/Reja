
from django.contrib import admin
from django.urls import path, include
from asosiy.views import *
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _




urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', Rejaview.as_view()),
    path('reja/<int:son>/', Reja_ochir.as_view()),
    path('reja_edit/<int:son>/', Reja_update.as_view()),
    path('', Loginview.as_view()),
    path('logout/', Logoutview.as_view()),
    path('register/', Register.as_view()),
]
urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
)

