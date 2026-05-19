from typing import Optional

import httpx

from app.config import INVENTORY_SERVICE_URL, ORDER_SERVICE_URL, PAYMENT_SERVICE_URL


class ClientManager:
    def __init__(self):
        self._payment_client: Optional[httpx.AsyncClient] = None
        self._inventory_client: Optional[httpx.AsyncClient] = None
        self._order_client: Optional[httpx.AsyncClient] = None

    async def startup(self):
        self._payment_client = httpx.AsyncClient(base_url=PAYMENT_SERVICE_URL, timeout=10.0)
        self._inventory_client = httpx.AsyncClient(base_url=INVENTORY_SERVICE_URL, timeout=30.0)
        self._order_client = httpx.AsyncClient(base_url=ORDER_SERVICE_URL, timeout=15.0)

    async def shutdown(self):
        if self._payment_client:
            await self._payment_client.aclose()
        if self._inventory_client:
            await self._inventory_client.aclose()
        if self._order_client:
            await self._order_client.aclose()

    @property
    def payment_client(self) -> httpx.AsyncClient:
        if not self._payment_client:
            raise RuntimeError("Payment client not initialized")
        return self._payment_client

    @property
    def inventory_client(self) -> httpx.AsyncClient:
        if not self._inventory_client:
            raise RuntimeError("Inventory client not initialized")
        return self._inventory_client

    @property
    def order_client(self) -> httpx.AsyncClient:
        if not self._order_client:
            raise RuntimeError("Order client not initialized")
        return self._order_client


client_manager = ClientManager()
