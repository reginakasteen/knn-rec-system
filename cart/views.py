from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Offer
from django.http import JsonResponse


def cart_summary(request):
    cart = Cart(request)
    cart_items = cart.get_items
    quantities = cart.get_quants
    totals = cart.cart_total()

    context = {
        'cart_items': cart_items,
        'quantities': quantities,
        'totals': totals,
    }
    return render(request, "cart/cart_summary.html", context)

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        offer_id = int(request.POST.get('offer_id'))
        offer_qty = int(request.POST.get('offer_qty'))
        offer = get_object_or_404(Offer, id=offer_id)
        cart.add(offer=offer, quantity=offer_qty)
        cart_count = cart.__len__()
        response = JsonResponse({
            'count': cart_count,
        })
        return response



def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        offer_id = int(request.POST.get('offer_id'))
        cart.delete(offer=offer_id)
        response = JsonResponse({
                'offer': offer_id
            })
        return response
def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        offer_id = int(request.POST.get('offer_id'))
        offer_qty = int(request.POST.get('offer_qty'))

        cart.update(offer=offer_id, quantity=offer_qty)
    response = JsonResponse({
        'count': offer_qty
    })
    return response

