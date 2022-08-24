from django.db import models

class Homepage(models.Model):
    fName = models.CharField(max_length=10)
    lName = models.CharField(max_length=10)