from fastapi import FastAPI

from app.api.stock import router as stock_router
from app.models.database import Base, engine

# Auto-create tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Stock Assistant",
    description="MVP stock analysis powered by AI — built with ai-dev-harness SOP",
    version="0.1.0",
)

app.include_router(stock_router)


@app.get("/health")
def health():
    return {"status": "ok"}
