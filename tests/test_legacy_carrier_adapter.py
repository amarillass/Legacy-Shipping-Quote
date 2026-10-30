from shipping_adapter.checkout import Checkout
from shipping_adapter.legacy_carrier import LegacyCarrier
from shipping_adapter.legacy_carrier_adapter import LegacyCarrierAdapter


def test_checkout_uses_legacy_carrier_through_shipping_quote_provider():
    checkout = Checkout(LegacyCarrierAdapter(LegacyCarrier()))

    price = checkout.shipping_quote("45000", 10.0)

    assert price == 33.56
