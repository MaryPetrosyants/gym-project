from rest_framework import serializers
from .models import Training
from gym.trainer.serializers import TrainerSerializer 
from gym.equipment.serializers import EquipmentSerializer
class TrainingSerializer(serializers.ModelSerializer):
    trainer = TrainerSerializer(source='contract_set.first.id_trainer', read_only=True)
    equipment = EquipmentSerializer(source='equipment_set', many=True, read_only=True)

    class Meta:
        model = Training
        fields = ['id', 'data_training', 'plan', 'time', 'trainer', 'equipment']
        
from .models import SignUpForTraining

class SignUpForTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUpForTraining
        fields = ['id', 'id_client', 'code_training']
        read_only_fields = ['id_client']
