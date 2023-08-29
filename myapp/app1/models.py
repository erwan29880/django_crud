from django.db import models


# créer table masculin féminin
class Genre(models.Model):
    genre = models.fields.CharField(max_length=1, default="M")

    def __str__(self):
        return f"{self.genre}"
    
 
# créer table avec nom, prénom, téléphone et masculin/féminin par relationnel
class Adresses(models.Model):
    prenom = models.fields.CharField(max_length=50)
    nom = models.fields.CharField(max_length=50)
    tel = models.fields.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return f'{self.prenom}'