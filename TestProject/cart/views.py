from django.views.generic.base import TemplateView
from django.http.response import JsonResponse
from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import get_object_or_404, render, redirect

from .models import Item
from TestProject import settings

import stripe


class IndexPage(TemplateView):
    template_name = 'index.html'


@requires_csrf_token
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config)


@requires_csrf_token
def buy_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'GET':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        domain_url = 'http://127.0.0.1:8000/'
        try:
            checkout_session = stripe.checkout.Session.create(
                mode='payment',
                success_url=domain_url + 'session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': 2000,
                        'product_data': {
                            'name': item.name,
                            'description': item.description,
                        },
                    },
                    'quantity': 1,
                }]
            )
            # return redirect(stripe.redirectToCheckout(sessionId=checkout_session['id']))
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as err:
            return JsonResponse({'error': str(err)})

@requires_csrf_token
def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    template = 'item_detail.html'
    context = {
        'item': item,
    }
    return render(request, template, context)

