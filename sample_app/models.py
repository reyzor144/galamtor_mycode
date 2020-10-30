from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    active = models.TextField(default='It it inactive I suppose')