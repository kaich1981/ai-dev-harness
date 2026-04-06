# 🤖 AI Output Contract

---

# 🇺🇸 English

> AI service must return a JSON object with the following structure

---

## Output Format

```json
{
  "trend": "up | down | stable (Trend direction)",
  "suggestion": "string (Actionable advice)",
  "confidence": "number 0-1 (Confidence score)",
  "risk_note": "string (Risk warning)"
}
```

---

## Rules

- `trend` must be one of: `up`, `down`, `stable`
- `confidence` must be between 0 and 1
- `suggestion` must be a concise, actionable sentence
- `risk_note` must always be present (can be generic disclaimer)
- If AI fails to produce valid JSON, fallback to default response

---

# 🇨🇳 中文

> AI 服务必须返回以下 JSON 结构

---

## 输出格式

```json
{
  "trend": "up | down | stable（趋势判断）",
  "suggestion": "string（可执行的操作建议）",
  "confidence": "number 0-1（置信度）",
  "risk_note": "string（风险提示）"
}
```

---

## 规则

- `trend` 必须是以下之一：`up`（上涨）、`down`（下跌）、`stable`（震荡）
- `confidence` 必须在 0 到 1 之间
- `suggestion` 必须是简洁、可执行的建议
- `risk_note` 必须始终存在（可以是通用免责声明）
- 如果 AI 无法生成有效 JSON，使用默认兜底响应
