from rest_framework import serializers
from .models import Abonement

class AbonementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonement
        fields = '__all__'
