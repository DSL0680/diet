from django.db import models
from django.contrib.auth.models import User

class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    content = models.TextField()
    image = models.ImageField(upload_to='diary_images/', null=True, blank=True)

    def __str__(self):
        return f"Diary Entry for {self.date}"
