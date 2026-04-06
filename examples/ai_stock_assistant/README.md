# 📈 AI Stock Assistant (Example Project)

> Example project built with ai-dev-harness

---

# 🎯 项目目标

一个最小可用的 AI 股票助手：

* 输入股票信息
* 返回建议
* 提供风险提示

---

# 🧠 为什么做这个例子？

让你看到：

> 如何用 SOP 从 0 → 可运行项目

---

# 🧩 功能范围（MVP）

✅ 股票分析
✅ 风险建议

❌ 不做实时行情
❌ 不做复杂策略

---

# 🏗️ 架构

```
Frontend (可选)
 ↓
FastAPI
 ↓
AI Service
 ↓
Database
```

---

# 📄 API示例

## POST /api/stock/analyze

```json
Request:
{
  "stock_code": "AAPL",
  "cost_price": 180
}
```

```json
Response:
{
  "trend": "down",
  "suggestion": "reduce position",
  "confidence": 0.72
}
```

---

# 🧩 数据库设计

```sql
Table: stock_position

id INT
stock_code VARCHAR
cost_price DECIMAL
created_at DATETIME
```

---

# 🚀 如何开发（按SOP）

---

## Step 1：定义契约

* API
* DB结构

---

## Step 2：拆任务

```text
1. 初始化项目
2. DB连接
3. stock表
4. API接口
5. AI服务
```

---

## Step 3：逐任务开发

每个任务：

* 调用AI
* 验收
* commit

---

# 🧪 示例任务

## Task: 实现股票分析接口

输出：

* /api/stock.py
* /service/stock_service.py

---

# 🔥 核心收获

你会学到：

* 如何控制AI
* 如何避免代码失控
* 如何快速做MVP

---

# 🧠 一句话总结

> 这是一个“如何用AI正确做项目”的示例
