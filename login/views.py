from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
# Create your views here.

def login_view(request, *args, **kwargs):
    form = AuthenticationForm()

    if (request.method == 'POST'):
        form = AuthenticationForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('home')

    context = {"form": form}
    return render(request,'login.html', context)
    # return HttpResponse()