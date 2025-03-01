from django.shortcuts import render
from .models import Show

# Create your views here.
def shows_list(request):
    shows = Show.objects.all()
    return render(request, 'shows_list.html', { 'shows' : shows})
