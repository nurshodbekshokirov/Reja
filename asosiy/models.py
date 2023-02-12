from django.db import models

class Reja(models.Model):
    sarlavha = models.CharField(max_length=60)
    vaqt = models.TimeField()
    batafsil = models.TextField()
    holat = models.BooleanField()

    def __str__(self):
        return self.sarlavha