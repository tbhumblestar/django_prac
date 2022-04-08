from tkinter import CASCADE
from django.db import models

# Create your models here.
class Drinks(models.Model):
    # id = models.AutoField(primary_key=True)#자동추가
    korean_name = models.CharField(max_length=50)
    english_name = models.CharField(max_length=50)
    description = models.TextField()
    category_id = models.ForeignKey("Category",on_delete=models.CASCADE)

    class Meta:
        db_table = 'drinks'

class Images(models.Model):
    image_url = models.URLField()
    drink_id = models.OneToOneField('Drinks',on_delete=models.CASCADE)


class Nutrition(models.Model):
    one_serving_kca = models.DecimalField(max_digits=10,decimal_places=2)
    sodium_mg = models.DecimalField(max_digits=10,decimal_places=2)
    saturated_fat_g = models.DecimalField(max_digits=10,decimal_places=2)
    sugars_g = models.DecimalField(max_digits=10,decimal_places=2)
    protein_G = models.DecimalField(max_digits=10,decimal_places=2)
    caffeine_mg = models.DecimalField(max_digits=10,decimal_places=2)
    drink_id = models.OneToOneField('Drinks',on_delete=models.CASCADE)
    size_id = models.ForeignKey('Sizes',on_delete=models.CASCADE)
    

    class Meta:
        db_table = 'Nutrition'
    # size_id = models.ForeignKey('size',on_delete=models.CASCADE)

class Sizes(models.Model):
    name = models.CharField(max_length=100)
    size_ml = models.CharField(max_length=100)
    size_fluid_ounce = models.CharField(max_length=100)


class menu(models.Model):
    name = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100)
    menu_id = models.ForeignKey('menu',on_delete=models.CASCADE)


class Allergy(models.Model):
    name = models.CharField(max_length=100)
    drinks = models.ManyToManyField(Drinks,related_name='allergies')


