from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class group(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"


class staff(models.Model):
    name = models.CharField(max_length=64)
    uni_id = models.IntegerField(validators=[
            MinValueValidator(2200000),
            MaxValueValidator(2399999)
        ]) 
    group = models.ManyToManyField(group)

    def __str__(self):
        return f"{self.name}"

    