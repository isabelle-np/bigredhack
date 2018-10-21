from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    housing = models.CharField(max_length=6)
    h_type = models.CharField(max_length=7, default='modest')
    vehicle = models.BooleanField(default=False)
    ent_val = models.IntegerField(validators=[MaxValueValidator(3), MinValueValidator(0)])
    din_out = models.IntegerField(validators=[MaxValueValidator(21), MinValueValidator(0)])
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    city_new = models.CharField(max_length=11)
