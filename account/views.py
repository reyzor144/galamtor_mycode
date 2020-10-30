from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            account = form.save()
            login(request, account, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        else:
            context['registration_form'] = form
            # context = {"registration_form": form}
    else:
        form = RegistrationForm()
        context['registration_form'] = form
        # context = {"registration_form": form}
    return render(request, 'account/register.html', context)


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect("home")
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'account/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def pers_acc_view(request):
    return render(request, 'account/account_manager.html', {})
