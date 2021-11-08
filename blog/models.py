from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="titre")
    description = models.TextField(verbose_name="contenu")
    date = models.DateField(verbose_name="date de creation")
    published = models.BooleanField(verbose_name="publié")

    def __str__(self):
        return self.title