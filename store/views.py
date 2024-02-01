from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Category, Offer, Review
from .review_form import ReviewForm
from django.db.models import Avg


def main_store(request):
    offers = Offer.objects.all()[:5]
    total_offers = Offer.objects.count
    for offer in offers:
        average_reviews = Review.objects.filter(offer=offer).aggregate(rating=Avg("rating_value"))
        average_rating = Review.objects.filter(offer=offer).aggregate(rating=Avg("rating_value"))
        offer.average_rating = average_reviews['rating'] if average_reviews['rating'] else 0
    context = {
        'offers': offers,
        'average_rating': average_rating,
        'total_offers': total_offers,
    }
    return render(request, 'store/store.html', context)

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def offer_detail(request, slug):
    offer = get_object_or_404(Offer, slug=slug, is_active=True)
    reviews = Review.objects.filter(offer=offer)

    # if request.method == 'POST':
    #     review_form = ReviewForm(request.POST)
    #     if review_form.is_valid():
    #         review = review_form.save(commit=False)
    #         review.offer = offer
    #         review.save()
    #         return redirect('store:offer_detail', slug=slug)

    if reviews.exists():
        average_rating = Review.objects.filter(offer=offer).aggregate(rating=Avg("rating_value"))
    else:
        average_rating = 0.0
    review_form = ReviewForm()
    context = {
        "reviews": reviews,
        "offer": offer,
        "average_rating": average_rating,
        "review_form": review_form,
    }
    return render(request, 'store/offers/detail.html', context)

def category_list_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    offers = Offer.objects.filter(category=category)
    return render(request, 'store/offers/category.html', {'category': category, 'offers': offers})

def ajax_add_review(request, id):
    offer = Offer.objects.get(pk=id)
    offer_slug = offer.slug
    user = request.user
    review = Review.objects.create(
        user=user,
        offer=offer,
        review_text=request.POST['review_text'],
        rating_value=request.POST['rating_value'],
    )
    context = {
        'user': user.username,
        'review_text': request.POST['review_text'],
        'rating_value': request.POST['rating_value'],
        'offer_slug': offer.slug,
    }
    if(Review.objects.filter(offer=offer).count == 0):
        average_reviews = 0.0
    else:
        average_reviews = Review.objects.filter(offer=offer).aggregate(rating=Avg("rating_value"))
    return JsonResponse(
        {
            'bool': True,
            'context': context,
            'average_reviews': average_reviews,
        }
    )
#def add_to_cart(request):

def load_more_data(request):
    offset=int(request.GET['offset'])
    limit=int(request.GET['limit'])
    data=Offer.objects.all()[offset:offset+limit]
    t=render_to_string('store/store.html', {'data':data})
    return JsonResponse({'data':t})





