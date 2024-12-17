from django.db import models
from django.contrib.auth.models import User
class Abonement(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    money = models.IntegerField()
    access = models.BooleanField(default=False)
    id_client = models.ForeignKey(User, on_delete=models.CASCADE)  
    trigger_log = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Abonement for {self.id_client} from {self.start_date} to {self.end_date}"
