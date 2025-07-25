from django.db import models


class Tree(models.Model):
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)
		    
    class Meta:
        verbose_name = "Árvore"
        verbose_name_plural = "Árvores"

    def __str__(self):
        return self.name
