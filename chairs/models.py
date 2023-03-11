from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Chairs(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    wheels = models.IntegerField(default=0)
    backrest = models.BooleanField(default=False)
    owner_idowner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

