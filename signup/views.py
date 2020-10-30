from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm

def signup_view(request, *args, **kwargs):
    form = RegistrationForm()

    if (request.method == 'POST'):
        form = RegistrationForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('signup_complete')

    context = {"form": form}
    return render(request,'signup.html', context)

def signup_complete_view(request, *args, **kwargs):
    return render(request, 'signup_complete.html', {})