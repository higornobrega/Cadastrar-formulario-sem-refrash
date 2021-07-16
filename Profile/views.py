from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
# Create your views here.
def index (request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        bio = request.POST['bio']
        new_profile = Profile(nome=nome, email=email, bio=bio)
        new_profile.save()
        success = 'User '+nome+' created successfully'
        return HttpResponse(success)