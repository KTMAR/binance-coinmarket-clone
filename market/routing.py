from django.urls import path
from .consumers import MarketConsumer

ws_url = [
    path('ws/coins/', MarketConsumer.as_asgi())
]