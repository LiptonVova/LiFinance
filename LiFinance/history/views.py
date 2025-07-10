from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

@login_required(login_url=reverse_lazy("authentication:login"))
def history(request):
    return HttpResponseRedirect(reverse("main:index"))
