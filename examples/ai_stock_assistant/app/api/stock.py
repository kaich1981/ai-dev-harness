from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.models.database import get_db
from app.models.stock import StockAnalysis
from app.schemas.stock import (
    StockAnalyzeRequest,
    StockAnalyzeResponse,
    StockHistoryItem,
    StockHistoryResponse,
)
from app.service.stock_service import analyze_stock

router = APIRouter(prefix="/api/stock", tags=["stock"])


@router.post("/analyze", response_model=StockAnalyzeResponse)
def analyze(req: StockAnalyzeRequest, db: Session = Depends(get_db)):
    result = analyze_stock(req.stock_code, req.cost_price)

    record = StockAnalysis(
        stock_code=req.stock_code,
        cost_price=req.cost_price,
        **result,
    )
    db.add(record)
    db.commit()
    db.refresh(record)

    return StockAnalyzeResponse(stock_code=req.stock_code, **result)


@router.get("/history", response_model=StockHistoryResponse)
def history(stock_code: str = Query(..., min_length=1), db: Session = Depends(get_db)):
    rows = (
        db.query(StockAnalysis)
        .filter(StockAnalysis.stock_code == stock_code)
        .order_by(StockAnalysis.created_at.desc())
        .limit(50)
        .all()
    )
    return StockHistoryResponse(items=[StockHistoryItem.model_validate(r) for r in rows])
