from django.shortcuts import render, get_object_or_404
from .models import Category, Offer

def main_store(request):
    offers = Offer.objects.all()
    return render(request, 'store/store.html', {'offers': offers})

def categories(request):
    return {
        'categories': Category.objects.all()
    }
def offer_detail(request, slug):
    offer = get_object_or_404(Offer, slug=slug, is_active=True)
    return render(request, 'store/offers/detail.html', {'offer': offer})
