from django.db import models


class Tree(models.Model):
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
