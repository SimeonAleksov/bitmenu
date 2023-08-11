from django.db import models


class Menu(models.Model):
    name = models.CharField(blank=True, max_length=255)
