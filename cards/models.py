from django.db import models

# Create your models here.


class WordCard(models.Model):
    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='card_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.word} - {self.translation}"