# API Contract

## POST /api/stock/analyze

### Request

```json
{
  "stock_code": "string",
  "cost_price": "number"
}
```

### Response

```json
{
  "stock_code": "string",
  "trend": "up | down | stable",
  "suggestion": "string",
  "confidence": "number (0-1)",
  "risk_note": "string"
}
```

### Error Response

```json
{
  "detail": "string"
}
```

---

## GET /api/stock/history

### Query Params

- `stock_code`: string (required)

### Response

```json
{
  "items": [
    {
      "id": "integer",
      "stock_code": "string",
      "cost_price": "number",
      "trend": "string",
      "suggestion": "string",
      "confidence": "number",
      "created_at": "datetime"
    }
  ]
}
```

---

# API 契约（中文版）

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
      "created_at": "datetime（创建时间）"
    }
  ]
}
```
