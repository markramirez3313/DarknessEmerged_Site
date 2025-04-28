from django.shortcuts import render
from .models import Member

# Create your views here.
def members_list(request):
    members = Member.objects.all()
    return render(request, 'members_list.html', { 'members' : members})