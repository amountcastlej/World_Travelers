from django.db import models
from RegLoginApp.models import User

class Trip(models.Model):
    location = models.CharField(max_length=30)
    date = models.DateField()
    traveler = models.ForeignKey(User, related_name="pastTrips", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)