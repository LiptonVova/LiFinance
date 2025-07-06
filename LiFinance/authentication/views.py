from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("authentication:login"))


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]        
            User.objects.create_user(username=username, password=password)            
            return HttpResponseRedirect(reverse("authentication:login"))
    
    else:
        form = UserCreationForm()
        
    return render(request, "registration/register.html", {"form": form}) 