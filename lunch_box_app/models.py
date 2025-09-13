from django.db import models
from django.contrib.auth.models import User


GENDER_CHOICES = [
    ('Female', 'Female'),
    ('Male', 'Male'),
    ('Other', 'Other'),
]
ALLERGY_CHOICES = [
    ('Nuts', 'Nuts'),
    ('Sesame', 'Sesame'),
    ('Diary', 'Diary product (milk)'),
    ('Eggs', 'Eggs'),
    ('Gluten', 'Gluten (containing Wheat, Rye etc)'),
    ('Soy', 'Soy'),
    ('Fish', 'Fish'),
    ('Shellfish', 'Shellfish'),
    ('Celery', 'Celery'),
    ('Mustard', 'Mustard'),
    ('Sulfur dioxide', 'Sulfur dioxide'),
    ('Other', 'Add your allergy'),
]

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DoB = models.DateField()
    sex = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,  
    )
    allergies = models.ManyToManyField('Allergy', blank=True)
    created_at = models.DateField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='images/profile_pics', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Allergy(models.Model):
    name = models.CharField(max_length=15, default=None, choices=ALLERGY_CHOICES)
    other_allergy = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.name}: {self.other_allergy}" if self.name=='Other' else f"{self.name}"


