from datetime import datetime

from pydantic import BaseModel, Field


class StockAnalyzeRequest(BaseModel):
    stock_code: str = Field(..., min_length=1, max_length=20, examples=["AAPL"])
    cost_price: float = Field(..., gt=0, examples=[180.0])


class StockAnalyzeResponse(BaseModel):
    stock_code: str
    trend: str
    suggestion: str
    confidence: float
    risk_note: str


class StockHistoryItem(BaseModel):
    id: int
    stock_code: str
    cost_price: float
    trend: str
    suggestion: str
    confidence: float
    risk_note: str | None
    created_at: datetime

    model_config = {"from_attributes": True}


class StockHistoryResponse(BaseModel):
    items: list[StockHistoryItem]
