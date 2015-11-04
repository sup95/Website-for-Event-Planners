from django.db import models


class Caterers(models.Model):

    caterer_id = models.AutoField(primary_key=True)
    caterer_name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    cost = models.IntegerField()    

    def __str__(self):
        return self.caterer_name
