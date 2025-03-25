from django.db import models
from django.utils.timezone import now

class Auteur(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    age = models.IntegerField()
    #articles = models.ForeignKey(Article ...)
    def __str__(self):
        return self.prenom

class Article(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField() # Text long
    date_publication = models.DateTimeField(default=now)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.titre
