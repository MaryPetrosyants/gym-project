from rest_framework import viewsets
from .models import Abonement
from .serializers import AbonementSerializer

class AbonementViewSet(viewsets.ModelViewSet):
    queryset = Abonement.objects.all()
    serializer_class = AbonementSerializer
