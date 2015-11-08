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


class Entertainment(models.Model):

    e_id = models.AutoField(primary_key=True)
    entertainers_name = models.CharField(max_length=100)
    entertainers_type = models.CharField(max_length=100)
    entertainment_cost = models.IntegerField()    

    def __str__(self):
        return self.entertainers_name


class Themes(models.Model):

    theme_id = models.AutoField(primary_key=True)
    theme_type = models.CharField(max_length=100) 
    theme_name = models.CharField(max_length=100)  

    def __str__(self):
        return self.theme_name



