from django.db import models

# Create your models here.
class Link(models.Model):
    # link info e.g. github
    name = models.CharField(
        max_length=32,
        unique=True,
    )
    value = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )

class Statement(models.Model):
    # long statement for website page e.g. about
    name = models.CharField(
        max_length=32,
        unique=True,
    )
    value = models.TextField(
        null=True,
        blank=True,
    )
