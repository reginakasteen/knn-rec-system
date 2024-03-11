from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from .models import Booking
from history.models import ViewHistory
from store.models import Offer
import json
from django.http import JsonResponse
from django.contrib import messages


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
        messages.success(request, ("Product added to cart"))
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


def orders(request):
    if request.method == 'POST':
        items = json.loads(request.POST.get('items'))

        for item in items:
            offer_id = item['offer_id']
            checkin_date = item['checkin_date']
            checkout_date = item['checkout_date']
            cart = Cart(request)

            Booking.objects.create(
                offer_id=offer_id,
                user=request.user,
                checkin_date=checkin_date,
                checkout_date=checkout_date
            )
            cart.delete(offer=offer_id)

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})


def booking_page(request):
    orders = Booking.objects.filter(user=request.user)
    history = ViewHistory.objects.filter(user=request.user).order_by('-view_date')[:5]
    context = {
        'history': history,
        'orders': orders,
    }
    return render(request, 'cart/orders.html', context)