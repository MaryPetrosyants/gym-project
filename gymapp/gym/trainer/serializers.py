from rest_framework import serializers
from .models import Trainer

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['id', 'name', 'mail', 'number', 'INN', 'experience']



from .models import Contract

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'
