from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

#gender constraint
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]

# user models
class CustomUser(AbstractUser):
    #id field
    #user name
    #email field - unique required
    email = models.EmailField(unique=True)
    #gender
    gender = models.CharField(max_length=1, choices = GENDER_CHOICES)
    #bio field - optional text about user
    bio = models.CharField(max_length= 255, blank=True)
    #status field - active = true, inactive = false
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.username

#python manage.py makemigrations 
# python manage.py migrate