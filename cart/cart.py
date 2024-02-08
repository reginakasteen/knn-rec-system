from store.models import Offer

class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart


    def add(self, offer, quantity):
        offer_id = str(offer.id)
        offer_qty = str(quantity)
        if offer_id in self.cart:
            pass
        else:
            #self.cart[offer_id] = {'price': str(offer.price)}
            self.cart[offer_id] = int(offer_qty)

        self.session.modified = True
    def __len__(self):
        return len(self.cart)

    def get_items(self):
        offer_ids = self.cart.keys()
        offers = Offer.objects.filter(id__in=offer_ids)
        return offers

    def get_quants(self):
        quantities = self.cart
        return quantities
    def update(self, offer, quantity):
        offer_id = str(offer)
        product_qty = int(quantity)

        outcart = self.cart
        outcart[offer_id] = product_qty

        self.session.modified = True

        thing = self.cart
        return thing

    def delete(self, offer):
        offer_id = str(offer)
        if offer_id in self.cart:
            del self.cart[offer_id]
        self.session.modified = True


    def cart_total(self):
        offer_ids = self.cart.keys()
        offers = Offer.objects.filter(id__in=offer_ids)
        quantities = self.cart
        total = 0
        for key, value in quantities.items():
            key = int(key)
            for offer in offers:
                if offer.id == key:
                    total = total + (offer.price * value)

        return total
