from django.shortcuts import render
from initial.models import Initial
from django.contrib.auth.decorators import login_required


def list_initial(request):
    all_initial = Initial.objects.all()
    print(all_initial)
    context = {
        'initials':all_initial,        
    }
    return render(request, 'index.html', context=context)
