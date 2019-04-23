from application.handlers.payment import PaymentHandler


routing_table = [
    (r"/payment", PaymentHandler),
]
