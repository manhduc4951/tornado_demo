from marshmallow import Schema, fields


class PaymentResponseSchema(Schema):
    status = fields.Str(required=True)
    fee = fields.Int(required=True)

    class Meta:
        strict = True
