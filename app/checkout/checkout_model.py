from datetime import datetime, timezone
from enum import Enum

from sqlalchemy import Column, DateTime, Float, Integer, String

from app.infra.database import Base


class CheckoutStatus(Enum):
    """Enum representing the different states of a checkout process."""

    PENDING = "pending"
    SUCCESS = "success"
    PROCESSING_PAYMENT = "processing_payment"
    PROCESSING_INVENTORY = "processing_inventory"
    CREATING_ORDER = "creating_order"
    FAILED = "failed"


class Checkout(Base):
    __tablename__ = "checkouts"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    customer_email: str = Column(String(128), nullable=False)
    created_at: datetime = Column(
        DateTime(timezone=True), default=datetime.now(timezone.utc), nullable=False
    )
    payment_id: str | None = Column(String(64), nullable=True)
    order_id: str | None = Column(String(64), nullable=True)
    status: str = Column(String(24), default=CheckoutStatus.PENDING.value, nullable=False)
    error: str | None = Column(String, nullable=True)
    total_amount: float = Column(Float, nullable=False)
