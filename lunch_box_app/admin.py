from django.contrib import admin

# Register your models here.
from .models import UserProfile, User, Allergy

admin.site.register(Allergy)