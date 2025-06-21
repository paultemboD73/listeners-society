from django.db import models

# Create your models here.
class Match(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    volunteer = models.ForeignKey('volunteers.Volunteer', on_delete=models.CASCADE)
    matched_at = models.DateTimeField(auto_now_add=True)
    ended = models.BooleanField(default=False)