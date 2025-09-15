from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy 
from lunch_box_app.models import Allergy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from .forms import UserRegistrationForm
from .models import UserProfile, Allergy

# Create your views here.
def index(request):

    return render(request, 'lunch_box_app/index.html', )


def my_lunch_box(request):
    allergies = Allergy.objects.all()
    allergies = get_list_or_404(Allergy)
    return render(request, 'lunch_box_app/my_lunch_box.html', {'allergies': allergies})

class UserLoginView(LoginView):
    pass
    
class RegistrationView(CreateView):
    # model = UserProfile# albo model albo form class bo to sie gryzie
    form_class = UserRegistrationForm
    # fields = [    💡 usuwam fields, bo uzywa, form_class
    #         'username', 
    #         'email', 
    #         'password1',
    #         'password2', 
    #         'DoB', 
    #         'sex', 
    #         'allergies', 
    #         'other_allergy', 
    #         'profile_picture'
    # ] 
    template_name = 'registration.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.email = form.cleaned_data['email']
        user.save()

        profile = UserProfile.objects.create(
            user=user,
            DoB=form.cleaned_data['DoB'],
            sex=form.cleaned_data['sex'],
            allergies=form.cleaned_data['allergies'],
            profile_picture=form.cleaned_data.get('profile_picture')
    )
        # Dodajemy alergie (ManyToMany)


        allergies = form.cleaned_data['allergies'] # pod 'allergies' jest QuerySet
        if allergies:
            profile.allergies.set(allergies)

            # jeśli użytkownik podał "other allergy"
            other = form.cleaned_data.get('other_allergy')
            if other:
                # utwórz nową alergię i dodaj do profilu
                other_obj, _ = Allergy.objects.get_or_create(name=other)
                profile.allergies.add(other_obj)    

        return super().form_valid(form)