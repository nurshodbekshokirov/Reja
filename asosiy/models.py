from django.db import models
from django.contrib.auth.models import User

class Reja(models.Model):
    sarlavha = models.CharField(max_length=60)
    vaqt = models.TimeField()
    batafsil = models.TextField()
    foydalanuvchi = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    holat = models.BooleanField()

    def __str__(self):
        return self.sarlavha