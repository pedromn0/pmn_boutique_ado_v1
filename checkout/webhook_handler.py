from django.http import HttpResponse


class StripeWH_handler:
    """ Handler Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_envet(self, event):
        """
        Handle a generic/unknown/unexpectede webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
