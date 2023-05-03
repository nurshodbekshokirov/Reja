from django.db import models
from django.contrib.auth.models import User
class Talaba(models.Model):
    ism = models.CharField(max_length=50)
    familyasi = models.CharField(max_length=50)
    st_raqam = models.CharField(max_length=50)
    kurs = models.PositiveSmallIntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.ism

class Reja(models.Model):
    sarlavha = models.CharField(max_length=60, blank=True, null=True)
    vaqt = models.TimeField()
    batafsil = models.TextField(blank=True, null=True)
    talaba = models.ForeignKey(Talaba, on_delete=models.SET_NULL, null=True)
    holat = models.BooleanField(blank=True, null=True)



