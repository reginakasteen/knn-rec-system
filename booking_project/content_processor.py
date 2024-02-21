from store.models import Offer, Owner, Category, Review
from django.db.models import Max, Min, Count


def default(request):
    categories = Category.objects.all()
    owners = Owner.objects.all()

    min_max_price = Offer.objects.aggregate(Min("price"), Max("price"))

    context = {
        'categories': categories,
        'owners': owners,
        'min_max_price': min_max_price,
    }
    return context