from django.db import models
from gym.training.models import *

class Equipment(models.Model):
    model = models.IntegerField()
    date_appearance = models.DateField()
    weight = models.IntegerField()
    code_training = models.ForeignKey(Training, on_delete=models.CASCADE)

    def __str__(self):
        return f"Equipment {self.model}"