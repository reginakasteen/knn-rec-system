from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Category, Offer, Review
from .review_form import ReviewForm
from django.urls import reverse
from django.db.models import Avg
from django.template.loader import render_to_string
from django.core.serializers import serialize
from django.core.paginator import Paginator
from django.views.generic import ListView


def main_store(request):
    offers = Offer.objects.all()
    paginator = Paginator(offers, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    is_paginated = True if paginator.num_pages > 1 else False

    for offer in page_obj:
        average_reviews = Review.objects.filter(offer=offer).aggregate(rating=Avg("rating_value"))
        average_rating = Review.objects.filter(offer=offer).aggregate(rating=Avg("rating_value"))
        offer.average_rating = average_reviews['rating'] if average_reviews['rating'] else 0
    context = {
        'average_rating': average_rating,
        'page_obj': page_obj,
        'is_paginated': is_paginated,
    }
    return render(request, 'store/store.html', context)

def category_list_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    offers = Offer.objects.filter(category=category)
    paginator = Paginator(offers, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    is_paginated = True if paginator.num_pages > 1 else False
    for offer in page_obj:
        average_reviews = Review.objects.filter(offer=offer).aggregate(rating=Avg("rating_value"))
        average_rating = Review.objects.filter(offer=offer).aggregate(rating=Avg("rating_value"))
        offer.average_rating = average_reviews['rating'] if average_reviews['rating'] else 0
    context = {
        'average_rating': average_rating,
        'page_obj': page_obj,
        'is_paginated': is_paginated,
    }
    return render(request, 'store/category.html', context)

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def offer_detail(request, slug):
    offer = get_object_or_404(Offer, slug=slug, is_active=True)
    reviews = Review.objects.filter(offer=offer)
    if reviews.exists():
        average_rating = Review.objects.filter(offer=offer).aggregate(rating=Avg("rating_value"))
    else:
        average_rating = 0.0
    review_form = ReviewForm()

    if request.user.is_authenticated:
        user = request.user
        existing_review = Review.objects.filter(user=user, offer=offer).exists()
    else:
        existing_review = False

    context = {
        "reviews": reviews,
        "offer": offer,
        "average_rating": average_rating,
        "review_form": review_form,
        "existing_review": existing_review,
    }
    print(average_rating)

    return render(request, 'store/offers/detail.html', context)



def ajax_add_review(request, id):
    offer = Offer.objects.get(pk=id)
    user = request.user
    existing_review = Review.objects.filter(user=user, offer=offer).first()
    if existing_review:
        return JsonResponse({'success': False, 'message': 'You have already left a review for this product.'})
    else:
        review = Review.objects.create(
            user=user,
            offer=offer,
            review_text=request.POST['review_text'],
            rating_value=request.POST['rating_value'],
        )
        context = {
            'user': user.username,
            'review_text': review.review_text,
            'rating_value': review.rating_value,
            'created': review.created_date.strftime('%Y-%m-%d %H:%M:%S'),
        }
        average_reviews = Review.objects.filter(offer=offer).aggregate(rating=Avg("rating_value"))['rating']
        redirect_url = reverse('store:offer_detail', kwargs={'slug': offer.slug})
        return JsonResponse(
            {
                'success': True,
                'redirect_url': redirect_url,
                'average_rating': average_reviews,
            }
        )
#def add_to_cart(request):




# def load_more_data(request):
#     offset = int(request.GET.get('offset', 0))
#     limit = int(request.GET.get('limit', 5))
#     data = Offer.objects.all()[offset:offset + limit]
#     serialized_data = serialize('json', data)
#     return JsonResponse({'data': serialized_data})

