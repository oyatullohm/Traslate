from django.db import models

# Create your models here.


class Trans(models.Model):
    en = models.TextField()
    uz = models.TextField()
    ru = models.TextField()