from django.db import models
from gym.training.models import *

class Trainer(models.Model):
    name = models.CharField(max_length=20)
    mail = models.EmailField(max_length=50)
    number = models.CharField(max_length=10)
    INN = models.CharField(max_length=20)
    experience = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Contract(models.Model):
    code_training = models.ForeignKey(Training, on_delete=models.CASCADE)
    id_trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Contract for {self.code_training} and trainer {self.id_trainer}"
