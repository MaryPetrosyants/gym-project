from django.contrib import admin
from gym.abonement.models import Abonement
from gym.equipment.models import Equipment
from gym.trainer.models import Contract, Trainer
from gym.training.models import Training, SignUpForTraining
# Register your models here.

admin.site.register(Training)
admin.site.register(SignUpForTraining)
admin.site.register(Trainer)
admin.site.register(Contract)
admin.site.register(Equipment)
admin.site.register(Abonement)
