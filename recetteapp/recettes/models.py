from django.db import models

from django.db import models

class Recette(models.Model):
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    immatriculation = models.CharField(max_length=20)
    nom_chauffeur = models.CharField(max_length=100)
    note = models.TextField(blank=True, null=True)
    date_recette = models.DateField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Recette de {self.nom_chauffeur} - {self.montant}"