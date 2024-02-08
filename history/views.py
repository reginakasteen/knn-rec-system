from django.shortcuts import render, redirect, get_object_or_404
from history.models import ViewHistory
from store.models import Offer

def history_view(request):
    if request.method == "POST":
        user = request.user
        offer_id = request.POST['id']
        offer = get_object_or_404(Offer, id=offer_id)
        history = ViewHistory(user=user, offer=offer)
        history.save()
        return redirect(f'../store/item/{offer.slug}')
    return render(request, 'history/history.html')
