# 🧩 Task Breakdown

---

# 🇺🇸 English

> Follow SOP: one task at a time, validate before next

---

## Task 1: Project Init & DB Connection

- **Output**: `app/models/database.py`
- **Acceptance**: `python -c "from app.models.database import engine"` runs without error

---

## Task 2: Define stock_analysis Model

- **Output**: `app/models/stock.py`
- **Acceptance**: Table auto-created in SQLite on startup

---

## Task 3: Define Request/Response Schemas

- **Output**: `app/schemas/stock.py`
- **Acceptance**: Pydantic validation works for sample input

---

## Task 4: Implement AI Analysis Service

- **Output**: `app/service/stock_service.py`
- **Acceptance**: Returns valid JSON matching AI_OUTPUT_CONTRACT

---

## Task 5: Implement /api/stock/analyze Endpoint

- **Output**: `app/api/stock.py`
- **Acceptance**: `curl POST /api/stock/analyze` returns correct response

---

## Task 6: Implement /api/stock/history Endpoint

- **Output**: `app/api/stock.py` (Add route)
- **Acceptance**: `curl GET /api/stock/history?stock_code=AAPL` returns list

---

## Task 7: Add Tests

- **Output**: `tests/test_stock_api.py`
- **Acceptance**: `pytest` all pass

---

# 🇨🇳 中文

> 遵循 SOP：一次一个任务，验收通过再进入下一个

---

## 任务 1：项目初始化 & 数据库连接

- **产出**：`app/models/database.py`
- **验收**：`python -c "from app.models.database import engine"` 无报错

---

## 任务 2：定义数据模型

- **产出**：`app/models/stock.py`
- **验收**：启动时自动在 SQLite 中创建表

---

## 任务 3：定义请求/响应 Schema

- **产出**：`app/schemas/stock.py`
- **验收**：Pydantic 校验示例输入通过

---

## 任务 4：实现 AI 分析服务

- **产出**：`app/service/stock_service.py`
- **验收**：返回符合 AI_OUTPUT_CONTRACT 的有效 JSON

---

## 任务 5：实现分析接口

- **产出**：`app/api/stock.py`
- **验收**：`curl POST /api/stock/analyze` 返回正确响应

---

## 任务 6：实现历史查询接口

- **产出**：`app/api/stock.py`（新增路由）
- **验收**：`curl GET /api/stock/history?stock_code=AAPL` 返回列表

---

## 任务 7：添加测试

- **产出**：`tests/test_stock_api.py`
- **验收**：`pytest` 全部通过
