# 🔗 API Contract

---

# 🇺🇸 English

> All endpoints must strictly follow this contract

---

## POST /api/stock/analyze

### Request Body

```json
{
  "stock_code": "string (Stock ticker)",
  "cost_price": "number (Buy/cost price)"
}
```

### Success Response

```json
{
  "stock_code": "string (Stock ticker)",
  "trend": "up | down | stable (Trend direction)",
  "suggestion": "string (Actionable advice)",
  "confidence": "number 0-1 (Confidence score)",
  "risk_note": "string (Risk warning)"
}
```

### Error Response

```json
{
  "detail": "string (Error message)"
}
```

---

## GET /api/stock/history

### Query Params

- `stock_code`: string (Required, stock ticker)

### Response

```json
{
  "items": [
    {
      "id": "integer (Primary key)",
      "stock_code": "string (Stock ticker)",
      "cost_price": "number (Cost price)",
      "trend": "string (Trend)",
      "suggestion": "string (Suggestion)",
      "confidence": "number (Confidence)",
      "risk_note": "string (Risk note)",
      "created_at": "datetime (Record time)"
    }
  ]
}
```

---

# 🇨🇳 中文

> 所有接口必须严格遵循此契约

---

## POST /api/stock/analyze

### 请求体

```json
{
  "stock_code": "string（股票代码）",
  "cost_price": "number（持仓成本价）"
}
```

### 成功响应

```json
{
  "stock_code": "string（股票代码）",
  "trend": "up | down | stable（趋势：上涨/下跌/震荡）",
  "suggestion": "string（操作建议）",
  "confidence": "number 0-1（置信度）",
  "risk_note": "string（风险提示）"
}
```

### 错误响应

```json
{
  "detail": "string（错误信息）"
}
```

---

## GET /api/stock/history

### 查询参数

- `stock_code`: string（必填，股票代码）

### 响应

```json
{
  "items": [
    {
      "id": "integer（主键）",
      "stock_code": "string（股票代码）",
      "cost_price": "number（成本价）",
      "trend": "string（趋势）",
      "suggestion": "string（建议）",
      "confidence": "number（置信度）",
      "risk_note": "string（风险提示）",
      "created_at": "datetime（创建时间）"
    }
  ]
}
```
