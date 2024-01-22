from django.shortcuts import render
from .models import Category, Offer

def main_store(request):
    offers = Offer.objects.all()
    return render(request, 'store/store.html', {'offers': offers})

def categories(request):
    return {
        'categories': Category.objects.all()
    }

