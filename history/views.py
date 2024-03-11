from django.shortcuts import render, redirect, get_object_or_404
from history.models import ViewHistory
from django.db.models import Avg, F
from store.models import Offer, Review
from django.core.paginator import Paginator
from collections import OrderedDict


def history_view(request):
    if request.method == "POST":
        user = request.user
        offer_id = request.POST['id']
        offer = get_object_or_404(Offer, id=offer_id)
        history = ViewHistory(user=user, offer=offer)
        history.save()
        return redirect(f'../store/item/{offer.slug}')
    return render(request, 'history/history.html')


def all_history(request):
    view_history_entries = ViewHistory.objects.filter(user=request.user).order_by('-view_date')

    viewed_products_dict = OrderedDict()

    for entry in view_history_entries:
        viewed_products_dict[entry.offer] = None

    offers = list(viewed_products_dict.keys())
    print(offers)

    paginator = Paginator(offers, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    is_paginated = paginator.num_pages > 1

    average_rating = []

    if len(offers) != 0:
        for offer in page_obj:
            average_reviews = Review.objects.filter(offer=offer).aggregate(rating=Avg("rating_value"))
            average_rating = average_reviews['rating'] if average_reviews['rating'] else 0
            offer.average_rating = average_rating

    context = {
        'average_rating': average_rating,
        'page_obj': page_obj,
        'is_paginated': is_paginated,
    }

    return render(request, 'history/history.html', context)



