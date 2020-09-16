from django.db import models

# Create your models here.


class Machine(models.Model):
    title = models.CharField(max_length=10, blank=True, null=True)
    types = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    is_water = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title


class Pod(models.Model):
    title = models.CharField(max_length=10, blank=True, null=True)
    types = models.CharField(max_length=50, blank=True, null=True)
    flavor = models.CharField(max_length=50, blank=True, null=True)
    size = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.title
