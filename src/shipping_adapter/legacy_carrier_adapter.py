from .legacy_carrier import LegacyCarrier
from .shipping_quote_provider import ShippingQuoteProvider


class LegacyCarrierAdapter(ShippingQuoteProvider):
    def __init__(self, carrier: LegacyCarrier):
        self.carrier = carrier

    def quote(self, destination: str, weight_kg: float) -> float:
        weight_lb = weight_kg * 2.20462
        return self.carrier.get_price(destination, weight_lb)
