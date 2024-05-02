from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    calorie = models.PositiveIntegerField()
    image = models.ImageField(upload_to='food_images', blank=True, null=True)

    def __str__(self):
        return self.name

