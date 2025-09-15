from datetime import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Allergy

GENDER_CHOICES = [      # tak, jest dwa razy - i tutaj i w models
    ('Female', 'Female'),
    ('Male', 'Male'),
    ('Other', 'Other'),
]

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=50, 
        required=True,
        label='Your email address'
)
    allergies = forms.ModelMultipleChoiceField(
        queryset=Allergy.objects.none(),
        widget=forms.SelectMultiple,
        required=True
)
    sex = forms.ChoiceField(
        choices=GENDER_CHOICES,
        required=True
)
    other_allergy = forms.CharField(
    max_length=50,
    required=False,
    label="Other allergy (if not listed)"
)

    DoB=forms.DateField(
        required=True,
        widget=forms.SelectDateWidget(years=range(1900, datetime.now().year + 1)) # bo range() w Pythonie nie obejmuje ostatniego elementu.
)

    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'password1',
            'password2', 
            ] 

# wyjasnienie dlaczego dwa razy zrobilam sex = gender_choices
# uwaga: w formularzu UserRegistrationForm nie jest ModelForm dla UserProfile, 
# tylko dla User.
# Dlatego jeśli chce zebrać sex podczas rejestracji, 
# trzeba je dodać ręcznie do formularza lub zrobić osobny UserProfileForm,
# bo inaczej Django nie widzi tego pola przy form.save().