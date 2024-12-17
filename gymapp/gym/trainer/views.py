from rest_framework import viewsets
from .models import Trainer
from .serializers import TrainerSerializer
from rest_framework import filters
from gym.permissions import IsAdminOrReadOnly 
class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'mail']
    permission_classes = [IsAdminOrReadOnly] 

from .models import Contract
from .serializers import ContractSerializer

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer