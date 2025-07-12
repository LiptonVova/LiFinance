from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import RangeDateForm
from main.models import Operation

@login_required(login_url=reverse_lazy("authentication:login"))
def history_view(request):
    if request.method == "POST":
        first_session = False
        form = RangeDateForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data["start_date"]
            end_date = form.cleaned_data["end_date"]    
            
            operations = (Operation.objects.filter(user=request.user) 
                        & Operation.objects.filter(date__lte=end_date) 
                        & Operation.objects.filter(date__gte=start_date))
            
            cheques = dict()
            for operation in operations:
                if operation.date in cheques:
                    cheques[operation.date].append(operation)
                else:
                    cheques[operation.date] = [operation]
            

    else:    
        cheques = []
        form = RangeDateForm()
        first_session = True
        
    context = {
        "form": form, 
        "cheques_dict": cheques,
        "first_session": first_session,
    }
    return render(request, "history/history.html", context=context)
