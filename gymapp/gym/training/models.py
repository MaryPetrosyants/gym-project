from django.db import models
from django.contrib.auth.models import User

class Training(models.Model):
    data_training = models.DateField()
    plan = models.CharField(max_length=20)
    time = models.TimeField()

    def __str__(self):
        return f"Training {self.plan} on {self.data_training}"
    
class SignUpForTraining(models.Model):
    code_training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name='signupfortraining')
    id_client = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='user_signups')  

    def __str__(self):
        return f"SignUp for {self.code_training} by {self.id_client}"