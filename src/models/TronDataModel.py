import datetime
from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from src.db import Base

class WalletInfo(Base):
    __tablename__ = "wallet_infos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    address: Mapped[str] = mapped_column(index=True)
    balance: Mapped[float]
    bandwidth: Mapped[int]
    energy: Mapped[int]

    created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
