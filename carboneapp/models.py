from django.db import models
from django.contrib.auth.models import User

class QuestionnaireEnergie(models.Model):
    organisation_loue = models.BooleanField(verbose_name="Est-ce que votre organisation loue le site à un tiers ?")
    achat_electricite = models.PositiveIntegerField(verbose_name="Achat d'électricité (KWh)")
    surface_climatisee = models.PositiveIntegerField(verbose_name="Surface climatisée (m²)")
    nombre_employes_dechet = models.PositiveIntegerField(verbose_name="Déchets (Renseigner le nombre total d'employes qui travaillent dans l'entite (ETP))")
    nombre_employes_eau = models.PositiveIntegerField(verbose_name="Eau (Renseigner le nombre total d'employes qui travaillent dans l'entite (ETP))")
    cout_renovation = models.PositiveIntegerField(null=True, blank=True, verbose_name="Coût total des travaux de rénovation")
    entite = models.OneToOneField(User, on_delete=models.CASCADE, related_name='QuestEnergy')

    def __str__(self):
        return f"Questionnaire Energie"

class DeplacementsProfessionnels(models.Model):
    cout_avion = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Coût déplacement avion")
    cout_taxi_voiture = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Coût déplacement taxi/voiture")
    cout_train = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Coût déplacement train")
    cout_bus_metro_tramway = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Coût déplacement bus/métro/tramway")
    cout_bateau = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Coût déplacement bateau")
    entite = models.OneToOneField(User, on_delete=models.CASCADE, related_name='DeplacementProfessionnel')
    def __str__(self):
        return "Déplacements professionnels"

class Vehicule(models.Model):
    site = models.CharField(max_length=255, verbose_name="Site")
    description = models.TextField(verbose_name="Description")
    type_motorisation = models.CharField(max_length=255, verbose_name="Type de motorisation")
    masse_vehicule = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Masse du véhicule (kg)")
    annee_immatriculation = models.PositiveIntegerField(verbose_name="Année d'immatriculation")
    distance_annuelle = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Distance annuelle (km)")
    type_carburant = models.CharField(max_length=255, verbose_name="Type de carburant")
    consommation_carburant = models.DecimalField(max_digits=10, decimal_places=2,
                                                 verbose_name="Consommation de carburant (l)")
    entite = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Vehicule')

    def __str__(self):
        return f"{self.type_motorisation} - {self.description}"

class TrajetDomicileTravail(models.Model):
    cout_voiture = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Coût trajet voiture")
    cout_train = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Coût trajet train")
    cout_bus_metro_tramway = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Coût trajet bus/métro/tramway")
    cout_autres = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Coût trajet autres")
    entite = models.OneToOneField(User, on_delete=models.CASCADE, related_name='TrajetDomicileTravail')
    def __str__(self):
        return "Trajet domicile-travail"
