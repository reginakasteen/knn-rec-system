from django.shortcuts import render
from account.models import User

def home_screen_view(request):
    context = {}
    users = User.objects.all()
    context['users'] = users
    return render(request, "personal/home.html", {})
