from datetime import datetime

from sqlalchemy import Integer, String, Text, DateTime, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.models.database import Base


class StockAnalysis(Base):
    __tablename__ = "stock_analysis"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    stock_code: Mapped[str] = mapped_column(String(20), nullable=False)
    cost_price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    trend: Mapped[str] = mapped_column(String(20), nullable=False)
    suggestion: Mapped[str] = mapped_column(Text, nullable=False)
    confidence: Mapped[float] = mapped_column(Numeric(3, 2), nullable=False)
    risk_note: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
