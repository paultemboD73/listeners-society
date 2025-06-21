from django.db import models

# gender constraint
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]

# volunteer expertise constraints
VOLUNTEER_EXPERTISE = [
    (1, 'depression'), (2, 'anxiety'),
    (3, 'stress management'),
    (4, 'grief & loss'),
    (5, 'self-esteem issues'),
    (6, 'relationship problems'),
    (7, 'family issues'),
    (8, 'loneliness'),
    (9, 'academic pressure'),
    (10, 'addiction support'),
    (11, 'anger management'),
    (12, 'workplace stress'),
    (13, ''),
]

# volunteer roles constraints
VOLUNTEER_ROLES_CHOICES = [
    ('Volunteer Approver', 'Volunteer Approver'),
    ('User Support Manager', 'User Support Manager'),
    ('System Monitor', 'System Monitor'),
]

#volunteer models

class Volunteer(models.Model):
    volunteer_id = models.AutoField(primary_key = True)
    volunteer_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50, unique = True)
    phone = models.CharField(max_length = 12)
    password = models.CharField(max_length = 128)
    gender = models.CharField(choices= GENDER_CHOICES)
    date_joined = models.DateTimeField(auto_now_add = True)
    last_login = models.DateTimeField(null= True, blank = True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default = 0.0)
    bio = models.CharField(max_length=225, blank = True)
    #expertise should have the option to have more than 1
    expertise = models.CharField(choices= VOLUNTEER_EXPERTISE)
    # a self referential fk
    approved_by = models.ForeignKey('self', on_delete=models.CASCADE )
    approved_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.volunteer_name