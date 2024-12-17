from rest_framework import viewsets
from .models import Training
from .serializers import TrainingSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import SignUpForTraining
from .serializers import SignUpForTrainingSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
from rest_framework import filters
from gym.permissions import IsAdminOrReadOnly 

class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['data_training', 'time']
    permission_classes = [IsAdminOrReadOnly] 
    
    @action(detail=False, methods=['get'], url_path='my-trainings' , permission_classes=[IsAuthenticated])
    def my_trainings(self, request):
        user = request.user
        trainings = Training.objects.filter(signupfortraining__id_client=user)
        serializer = self.get_serializer(trainings, many=True)
        return Response(serializer.data)
    

from .models import SignUpForTraining
from .serializers import SignUpForTrainingSerializer

class SignUpForTrainingViewSet(viewsets.ModelViewSet):
    queryset = SignUpForTraining.objects.all()
    serializer_class = SignUpForTrainingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
       
        if SignUpForTraining.objects.filter(
            id_client=user, 
            code_training=self.request.data.get('code_training')
        ).exists():
            raise ValidationError("Вы уже записаны на эту тренировку.")
      
        serializer.save(id_client=user)
    
    
