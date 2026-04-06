"""
Stock analysis service.

Uses a rule-based mock AI engine for demo purposes.
Replace `_analyze` with a real LLM call (e.g. OpenAI / Claude API) in production.
"""

import random


def analyze_stock(stock_code: str, cost_price: float) -> dict:
    """Analyze a stock and return structured advice matching AI_OUTPUT_CONTRACT."""
    return _analyze(stock_code, cost_price)


def _analyze(stock_code: str, cost_price: float) -> dict:
    """
    Rule-based demo analysis.
    In production, replace this with an actual LLM API call.
    """
    # Simulate a simple trend decision based on price range
    if cost_price < 50:
        trend = "up"
        suggestion = "Good entry point. Consider building a position gradually."
        confidence = round(random.uniform(0.60, 0.85), 2)
    elif cost_price < 200:
        trend = "stable"
        suggestion = "Hold current position. Monitor for breakout signals."
        confidence = round(random.uniform(0.50, 0.75), 2)
    else:
        trend = "down"
        suggestion = "Consider reducing position to manage risk."
        confidence = round(random.uniform(0.55, 0.80), 2)

    risk_note = (
        f"This is an AI-generated analysis for {stock_code}. "
        "It does not constitute financial advice. Always do your own research."
    )

    return {
        "trend": trend,
        "suggestion": suggestion,
        "confidence": confidence,
        "risk_note": risk_note,
    }
