from rest_framework import viewsets
from .models import Equipment
from .serializers import EquipmentSerializer
from rest_framework import filters
from gym.permissions import IsAdminOrReadOnly 

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['model', 'weight']
    permission_classes = [IsAdminOrReadOnly] 
