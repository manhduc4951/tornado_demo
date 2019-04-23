from marshmallow import Schema, fields


class PaymentRequestSchema(Schema):
    company = fields.Str(required=True)
    amount = fields.Int(required=True)

    class Meta:
        strict = True
