from django.conf import settings
import stripe
from django.conf import settings
from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from user.models import *
stripe.api_key = 'sk_test_51Q6avVP03nsNhqhuze5BjUZaT4Iyd5JEmUZAvpOKlbAeQTxAbdnO6Iwm8SKQV7LQ6x5lcABuwepMKNyBvj62TlLj00npSXJgpw'


class StripeWebhookView(APIView):
    def post(self, request):
        payload = request.body
        sig_header = request.META['HTTP_STRIPE_SIGNATURE']
        endpoint_secret = 'whsec_2W7rB3uyImA1N3erJrfdWP6zom7LKEaj'

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret
            )
        except ValueError as e:
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError as e:
            return HttpResponse(status=400)

        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            print("User.objects.get(pk=5)")

        return HttpResponse(status=200)
class StripeCheckoutView(APIView):
    def check_payment(self,id,time):
        user = User.objects.get(pk=id)
        user.is_member = True
        print(time)
        user.member_time = date.today()
        user.member_duration = time
        user.save()
        return f'http://localhost:5173/addproperty/{user.id}'

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
                            'unit_amount': unit_amount,
                            'recurring': {
                                'interval': 'day',
                            },
                        },
                        'quantity': 1,
                    },
                ],
                mode='subscription',
                success_url= self.check_payment(id,request.data.get('time_duration')),
                cancel_url='http://localhost:5173/?canceled=true',
                metadata={
                    'user_name': user.user_name
                }
            )

            return Response({'url': checkout_session.url})

        except Exception as e:
            return Response({'error': f'Something went wrong: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
