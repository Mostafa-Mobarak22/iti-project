from django.conf import settings
import stripe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  
from user.models import *
stripe.api_key = 'sk_test_51Q6avVP03nsNhqhuze5BjUZaT4Iyd5JEmUZAvpOKlbAeQTxAbdnO6Iwm8SKQV7LQ6x5lcABuwepMKNyBvj62TlLj00npSXJgpw'

class StripeCheckoutView(APIView):
    def post(self, request):
        try:
            id = request.data.get('id')
            unit_amount = request.data.get('unit_amount')
            user = User.objects.get(pk=id)
            if not user.id or not user.user_name or not unit_amount:
                return Response({'error': 'Email, Username, and Unit Amount are required'}, status=status.HTTP_400_BAD_REQUEST)

            # Create a new customer in Stripe
            customer = stripe.Customer.create(
                email=user.email,
                name=user.user_name
            )

            # Create a Stripe session using price_data with recurring settings
            checkout_session = stripe.checkout.Session.create(
                customer=customer.id,
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': 'Account Pro Subscription',
                                'description': f'Subscription for {user.user_name}',
                            },
                            'unit_amount': unit_amount,  # price in cents (e.g., 300 for $3.00)
                            'recurring': {
                                'interval': 'year',
                            },
                        },
                        'quantity': 1,
                    },
                ],
                mode='subscription',
                success_url= f'http://localhost:5173/addproperty/{user.id}',
                cancel_url='http://localhost:5173/?canceled=true',
                metadata={
                    'user_name': user.user_name
                }
            )

            return Response({'url': checkout_session.url})

        except Exception as e:
            return Response({'error': f'Something went wrong: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
