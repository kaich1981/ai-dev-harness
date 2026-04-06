# AI Stock Assistant

> A runnable MVP example built with ai-dev-harness SOP

## Quick Start

```bash
cd examples/ai_stock_assistant
pip install -r requirements.txt
python -m pytest tests/ -v        # run tests
uvicorn app.main:app --reload     # start server
```

Or use the one-liner:

```bash
bash run.sh
```

## API Endpoints

| Method | Path                  | Description          |
| ------ | --------------------- | -------------------- |
| POST   | `/api/stock/analyze`  | Analyze a stock      |
| GET    | `/api/stock/history`  | Query history        |
| GET    | `/health`             | Health check         |
| GET    | `/docs`               | Swagger UI (auto)    |

### Example: Analyze

```bash
curl -X POST http://127.0.0.1:8000/api/stock/analyze \
  -H "Content-Type: application/json" \
  -d '{"stock_code": "AAPL", "cost_price": 180}'
```

```json
{
  "stock_code": "AAPL",
  "trend": "stable",
  "suggestion": "Hold current position. Monitor for breakout signals.",
  "confidence": 0.68,
  "risk_note": "This is an AI-generated analysis for AAPL. It does not constitute financial advice."
}
```

## Project Structure

```
ai_stock_assistant/
  contracts/          # API / DB / AI output contracts (define before coding)
  tasks/              # Task breakdown (one task at a time)
  app/
    api/              # FastAPI route handlers
    service/          # Business logic & AI service
    models/           # SQLAlchemy models + DB connection
    schemas/          # Pydantic request/response schemas
  tests/              # Pytest test cases
  requirements.txt
  run.sh              # One-click start
```

## SOP Workflow Demonstrated

1. **Contracts first** -- see `contracts/` for API, DB, and AI output contracts
2. **Task breakdown** -- see `tasks/TASK_LIST.md` for step-by-step tasks
3. **Per-task implementation** -- each module maps to one task
4. **Validation** -- tests cover contract compliance
5. **Iterate** -- swap `_analyze()` in `stock_service.py` with a real LLM call

## Tech Stack

- FastAPI + Uvicorn
- SQLAlchemy + SQLite (swap to MySQL/PostgreSQL for production)
- Pydantic v2
- Pytest + httpx

---

# AI 股票助手（中文版）

> 基于 ai-dev-harness SOP 构建的可运行 MVP 示例

## 快速开始

```bash
cd examples/ai_stock_assistant
pip install -r requirements.txt
python -m pytest tests/ -v        # 运行测试
uvicorn app.main:app --reload     # 启动服务
```

或者一键启动：

```bash
bash run.sh
```

## API 接口

| 方法   | 路径                   | 说明          |
| ------ | --------------------- | ------------- |
| POST   | `/api/stock/analyze`  | 分析股票       |
| GET    | `/api/stock/history`  | 查询分析历史    |
| GET    | `/health`             | 健康检查       |
| GET    | `/docs`               | Swagger 文档   |

### 示例：分析股票

```bash
curl -X POST http://127.0.0.1:8000/api/stock/analyze \
  -H "Content-Type: application/json" \
  -d '{"stock_code": "AAPL", "cost_price": 180}'
```

```json
{
  "stock_code": "AAPL",
  "trend": "stable",
  "suggestion": "Hold current position. Monitor for breakout signals.",
  "confidence": 0.68,
  "risk_note": "This is an AI-generated analysis for AAPL. It does not constitute financial advice."
}
```

## 项目结构

```
ai_stock_assistant/
  contracts/          # API / DB / AI 输出契约（编码前先定义）
  tasks/              # 任务拆分（一次一个任务）
  app/
    api/              # FastAPI 路由处理
    service/          # 业务逻辑 & AI 服务
    models/           # SQLAlchemy 模型 + 数据库连接
    schemas/          # Pydantic 请求/响应定义
  tests/              # Pytest 测试用例
  requirements.txt
  run.sh              # 一键启动脚本
```

## SOP 流程演示

1. **契约先行** -- 见 `contracts/` 目录，包含 API、数据库、AI 输出契约
2. **任务拆分** -- 见 `tasks/TASK_LIST.md`，逐步拆解的开发任务
3. **逐任务实现** -- 每个模块对应一个任务
4. **验收测试** -- 测试覆盖契约合规性
5. **迭代优化** -- 将 `stock_service.py` 中的 `_analyze()` 替换为真实 LLM 调用

## 技术栈

- FastAPI + Uvicorn
- SQLAlchemy + SQLite（生产环境替换为 MySQL/PostgreSQL）
- Pydantic v2
- Pytest + httpx
