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
    """Model representing a checkout process."""

    __tablename__ = "checkouts"

    id = Column(Integer, primary_key=True, index=True)
    customer_email = Column(String(128), nullable=False)
    order_id = Column(String(64), nullable=True)
    payment_id = Column(String(64), nullable=True)
    total_amount = Column(Float, nullable=False)
    status = Column(String, nullable=False, default=CheckoutStatus.PENDING.value)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
