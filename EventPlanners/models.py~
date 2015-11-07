from django.db import models


class Caterers(models.Model):

    caterer_id = models.AutoField(primary_key=True)
    caterer_name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    cost = models.IntegerField()    

    def __str__(self):
        return self.caterer_name


class Photographers(models.Model):

    photographer_id = models.AutoField(primary_key=True)
    photographer_name = models.CharField(max_length=100)
    photography_type = models.CharField(max_length=100)
    videography = models.CharField(max_length=20)
    photo_cost = models.IntegerField()    

    def __str__(self):
        return self.photographer_name
