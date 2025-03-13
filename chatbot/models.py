from django.db import models

class Fichier(models.Model):
    nom = models.CharField(max_length=100)
    fichier = models.FileField(upload_to='documents/')
    date_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom