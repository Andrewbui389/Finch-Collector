from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)


class Blade(models.Model):
    producer = models.CharField(max_length=100)
    length = models.IntegerField()

    def __str__(self):
        return self.producer

    def get_absolute_url(self):
        return reverse('blade_details', kwargs={'pk': self.id})

# Create your models here.
class Finches(models.Model):
    name = models.CharField(max_length=100)
    speed = models.IntegerField()
    description = models.TextField(max_length=2500)
    color = models.CharField(max_length=50)
    age = models.IntegerField()
    blade = models.ManyToManyField(Blade)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id':self.id})

class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    finch = models.ForeignKey(Finches, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    