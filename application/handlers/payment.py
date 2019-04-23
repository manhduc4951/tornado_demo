from tornado.web import RequestHandler
from application.schemas.requests.payment import PaymentRequestSchema
from webargs.tornadoparser import use_args
from application.controllers.payment import process_payment
from application.schemas.responses.payment import PaymentResponseSchema


class PaymentHandler(RequestHandler):
    @use_args(PaymentRequestSchema)
    def post(self, payment_request):
        # Need to call controller to do some logic
        process_payment(payment_request)

        # Need to response something back
        result = PaymentResponseSchema().dump({
            "status": "success",
            "fee": 1
        }).data
        self.write(result)
