from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import RangeDateForm
from main.models import Operation

@login_required(login_url=reverse_lazy("authentication:login"))
def history_view(request):
    cheques = []
    if request.method == "POST":
        form = RangeDateForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data["start_date"]
            end_date = form.cleaned_data["end_date"]    
            
            cheques = (Operation.objects.filter(user=request.user) 
                        & Operation.objects.filter(date__lte=end_date) 
                        & Operation.objects.filter(date__gte=start_date))

    else:    
        form = RangeDateForm()
    context = {
        "form": form, 
        "cheques": cheques,
    }
    return render(request, "history/history.html", context=context)
