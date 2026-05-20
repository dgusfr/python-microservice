from datetime import datetime, timezone
from enum import Enum

from sqlalchemy import DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

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

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    customer_email: Mapped[str] = mapped_column(String(128), nullable=False)
    order_id: Mapped[str | None] = mapped_column(String(64), nullable=True)
    payment_id: Mapped[str | None] = mapped_column(String(64), nullable=True)
    total_amount: Mapped[float] = mapped_column(Float, nullable=False)
    status: Mapped[str] = mapped_column(
        String, nullable=False, default=CheckoutStatus.PENDING.value
    )
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
