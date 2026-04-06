# 📈 AI Stock Assistant

> Example project built with ai-dev-harness

---

# 🇺🇸 English

## 🎯 Project Goal

Build a minimal AI-powered stock assistant that can:

* Analyze a stock based on user input
* Provide actionable suggestions
* Output structured AI responses

---

## 🧩 Features (MVP)

✅ Stock analysis
✅ Risk-aware suggestions

❌ No real-time market data
❌ No complex trading strategies
❌ No multi-user system

---

## 🏗️ Architecture

```text
Frontend (optional)
 ↓
FastAPI Backend
 ↓
AI Service Layer
 ↓
Database (MySQL)
```

---

## 📄 API Example

### POST /api/stock/analyze

Request:

```json
{
  "stock_code": "AAPL",
  "cost_price": 180
}
```

Response:

```json
{
  "trend": "down",
  "suggestion": "reduce position",
  "confidence": 0.72
}
```

---

## 🧩 Database Schema

```sql
CREATE TABLE stock_position (
  id INT PRIMARY KEY AUTO_INCREMENT,
  stock_code VARCHAR(10),
  cost_price DECIMAL(10,2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🚀 Development Workflow

This project follows the ai-dev-harness methodology:

### Step 1: Define Contracts

* API structure
* Database schema

---

### Step 2: Break Into Tasks

Example:

```text
1. Initialize project
2. Setup database
3. Create stock model
4. Implement API endpoint
5. Integrate AI service
```

---

### Step 3: AI Execution (Per Task)

Each task is:

* Clearly defined
* Independently executable
* Strictly validated

---

### Step 4: Validation

* API works
* Output matches contract
* No fake logic

---

## 🧪 Example Task

Task: Implement stock analysis API

Output:

* backend/api/stock.py
* backend/service/ai_service.py

---

## 🔥 Key Learnings

* How to control AI output
* How to avoid messy code
* How to build MVP fast and safely

---

## 🧠 Summary

> This is not just a demo
> It is a reference implementation of controlled AI development

---

# 🇨🇳 中文

## 🎯 项目目标

构建一个最小可用的 AI 股票助手：

* 根据用户输入分析股票
* 提供建议
* 输出结构化结果

---

## 🧩 功能范围（MVP）

✅ 股票分析
✅ 风险提示

❌ 不做实时行情
❌ 不做复杂策略
❌ 不做多用户系统

---

## 🏗️ 架构

```text
前端（可选）
 ↓
FastAPI后端
 ↓
AI服务层
 ↓
数据库（MySQL）
```

---

## 📄 API 示例

### POST /api/stock/analyze

请求：

```json
{
  "stock_code": "AAPL",
  "cost_price": 180
}
```

返回：

```json
{
  "trend": "down",
  "suggestion": "减仓",
  "confidence": 0.72
}
```

---

## 🧩 数据库结构

```sql
CREATE TABLE stock_position (
  id INT PRIMARY KEY AUTO_INCREMENT,
  stock_code VARCHAR(10),
  cost_price DECIMAL(10,2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🚀 开发流程

该示例遵循 ai-dev-harness 方法论：

---

### Step 1：定义契约

* API结构
* 数据库结构

---

### Step 2：任务拆分

示例：

```text
1. 初始化项目
2. 配置数据库
3. 创建模型
4. 实现接口
5. 接入AI服务
```

---

### Step 3：AI逐任务执行

每个任务：

* 明确
* 独立
* 可验证

---

### Step 4：验收

* 接口可运行
* 输出符合契约
* 无伪实现

---

## 🧪 示例任务

任务：实现股票分析接口

输出：

* backend/api/stock.py
* backend/service/ai_service.py

---

## 🔥 核心收获

* 如何控制AI开发
* 如何避免代码失控
* 如何快速构建MVP

---

## 🧠 总结

> 这不仅是示例
> 更是一个“可控AI开发”的参考实现
