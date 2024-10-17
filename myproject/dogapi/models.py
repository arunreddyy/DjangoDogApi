from django.db import models

class Breed(models.Model):
    TINY = 'Tiny'
    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'Large'
    
    SIZE_CHOICES = [
        (TINY, 'Tiny'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    ]
    
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    friendliness = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    trainability = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    sheddingamount = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    exerciseneeds = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    color = models.CharField(max_length=100)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=100)
