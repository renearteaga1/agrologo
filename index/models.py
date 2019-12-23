import statistics

from django.db import models
from django.db.models import Avg

from django.contrib.auth.models import User

# Create your models here.

class RateQuerySet(models.QuerySet):
    def rate_avg(self):
        prods = self.filter()
        if prods:
            i = 0
            for x in prods:
                i = i + x.rate
        return prods.aggregate(Avg('rate')).get('rate__avg')

class RateManager(models.Manager):
    def get_queryset(self):
        return RateQuerySet(self.model, using=self._db)


class Categoria(models.Model):
    categoria = models.CharField(max_length=110)

    def __str__(self):
        return self.categoria

class Producto(models.Model):
    name = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    tags = models.CharField(max_length=110, blank=True, null=True)
    categoria = models.ManyToManyField(Categoria)

    #objects = models.Manager()
    #produg = RateManager()


    def __str__(self):
        return self.name

class Rate(models.Model):
    product = models.ForeignKey(Producto, on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=3, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #objects = RateManager()
    objects = RateQuerySet.as_manager()

    def __str__(self):
        return self.product.name
