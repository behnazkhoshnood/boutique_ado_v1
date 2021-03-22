from django.http import HttpResponse


class stripeWH_Handler:
    """ Handle stripe webhooks """

    def __init__(self, request):
        self.request = request

    def Handle_event(self, event):
        """
        handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'webhook received : {event["type"]}',
            status=200)
