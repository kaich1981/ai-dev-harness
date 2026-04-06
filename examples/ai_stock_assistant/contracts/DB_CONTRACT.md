# 🗄️ Database Contract

---

# 🇺🇸 English

> No contract, no code

---

## Table: `stock_analysis`

| Field        | Type           | Constraint         | Comment              |
| ------------ | -------------- | ------------------ | -------------------- |
| id           | INTEGER        | PK, AUTO           | Primary key          |
| stock_code   | VARCHAR(20)    | NOT NULL           | Stock ticker         |
| cost_price   | DECIMAL(10,2)  | NOT NULL           | Buy/cost price       |
| trend        | VARCHAR(20)    | NOT NULL           | Trend: up / down / stable |
| suggestion   | TEXT           | NOT NULL           | AI suggestion        |
| confidence   | DECIMAL(3,2)   | NOT NULL           | Confidence: 0.00 - 1.00 |
| risk_note    | TEXT           |                    | Risk warning         |
| created_at   | DATETIME       | DEFAULT NOW        | Record time          |

---

# 🇨🇳 中文

> 没有契约，不写代码

---

## 表：`stock_analysis`

| 字段         | 类型           | 约束               | 说明                 |
| ------------ | -------------- | ------------------ | -------------------- |
| id           | INTEGER        | 主键, 自增          | 主键                 |
| stock_code   | VARCHAR(20)    | NOT NULL           | 股票代码             |
| cost_price   | DECIMAL(10,2)  | NOT NULL           | 持仓成本价           |
| trend        | VARCHAR(20)    | NOT NULL           | 趋势：up / down / stable |
| suggestion   | TEXT           | NOT NULL           | AI 操作建议          |
| confidence   | DECIMAL(3,2)   | NOT NULL           | 置信度：0.00 - 1.00  |
| risk_note    | TEXT           |                    | 风险提示             |
| created_at   | DATETIME       | 默认当前时间        | 记录创建时间         |
