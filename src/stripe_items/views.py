import stripe

from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, JsonResponse

from .models import Item
from items.settings import STRIPE_SECRET_KEY
#from django.db.models import Manager
# Create your views here
#
# .

def buy(request: HttpRequest, pk: int) -> HttpResponse:
    item = get_object_or_404(Item, pk=pk)
    uri = request.build_absolute_uri()
    uri = uri.replace('buy', 'items')
    stripe.api_key = STRIPE_SECRET_KEY
    stripe_session = stripe.checkout.Session.create(
        success_url=uri,
        cancel_url=uri,
        mode='payment',
        line_items=[
            {
                'quantity': 1,
                'price_data': {
                    'unit_amount': int(item.price * 100),
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                        'description': item.description
                    }
                },
            }
        ]
    )
    try:
        session_id = stripe_session.id
        return JsonResponse({'session_id': session_id})
    except Exception as err:
        return JsonResponse({'err': str(err)})


def get_item(request: HttpRequest, pk: int) -> HttpResponse:
    item = get_object_or_404(Item, pk=pk)

    return render(request, 'home.html',context=item.to_dict())
