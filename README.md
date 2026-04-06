# 🚀 ai-dev-harness

> A structured system to build AI-powered applications with control, not chaos.

---

## 🧠 What is ai-dev-harness?

**ai-dev-harness** is a practical framework for building AI-driven applications as a solo developer.

It helps you move from:

```
❌ Prompt → Code → Chaos
```

to:

```
✅ System → Contract → Task → Controlled AI Development
```

---

## 🎯 Why this project?

Most AI-generated projects fail because:

* AI writes too much at once
* No structure or constraints
* No validation or iteration
* Code becomes unmaintainable quickly

This project solves that by introducing:

> **Harness Engineering for AI Development**

A system that makes AI:

* controllable
* testable
* modular
* production-ready

---

## 🧩 Core Concept

Instead of asking AI to generate the whole project:

> ❌ “Generate a full app”

We do:

```
Idea
 → Requirement
 → Contract (DB/API)
 → Task Breakdown
 → AI per-task execution
 → Validation
 → Iteration
```

---

## 🏗️ Project Structure

```
.
├── docs/          # SOP, contracts, design docs
├── prompts/       # Reusable AI prompt templates
├── templates/     # Task / project templates
├── backend/       # FastAPI starter (AI-ready)
├── tests/         # Basic test cases
└── .github/       # CI workflows
```

---

## ⚙️ How It Works

### 1️⃣ Define Problem (MVP First)

* Who is the user?
* What is the core pain?
* What is the smallest usable version?

---

### 2️⃣ Define Contracts (🔥 Most Important)

* Database schema
* API structure
* Output format

```json
{
  "trend": "string",
  "suggestion": "string",
  "confidence": "0-1"
}
```

---

### 3️⃣ Break Into Tasks

Each task must be:

* Small (≤ 1 hour)
* Isolated
* Testable

---

### 4️⃣ AI Executes Per Task

Use controlled prompts:

```
- Only implement this task
- Follow the contract
- Do not modify other modules
```

---

### 5️⃣ Validate Every Step

* Can it run?
* Does it match contract?
* Any fake logic?
* Any side effects?

---

### 6️⃣ Iterate Safely

* Git commit per task
* Regression check
* Continuous improvement

---

## 📘 Documentation

* 👉 [AI Development SOP](docs/AI_DEV_SOP.md)
* 👉 Contracts (API / DB)
* 👉 Task Templates
* 👉 Review Checklist

---

## 🧱 Tech Stack (Default)

* FastAPI (Backend)
* MySQL (Database)
* LLM API (AI layer)

---

## 🧪 Example Use Cases

* AI stock assistant
* AI productivity tools
* AI SaaS MVP
* Internal automation tools

---

## 🔥 Key Principles

### ❗ AI is NOT the architect

You are.

---

### ❗ No contract, no code

---

### ❗ Never generate the whole project

---

### ❗ Every step must be verifiable

---

### ❗ Start small, iterate fast

---

## 🧑‍💻 Who is this for?

* Solo developers
* Indie hackers
* Engineers building AI products
* Anyone tired of messy AI-generated code

---

## 🚀 Getting Started

```bash
git clone https://github.com/YOUR_USERNAME/ai-dev-harness.git
cd ai-dev-harness
```

1. Read `docs/AI_DEV_SOP.md`
2. Pick a project idea
3. Define contracts
4. Start with Task #1

---

## 📈 Roadmap

* [ ] Frontend template (Next.js / Mini Program)
* [ ] Docker setup
* [ ] CLI for task generation
* [ ] Prompt testing system
* [ ] AI evaluation framework

---

## 🤝 Contributing

Contributions are welcome!

* Improve templates
* Add workflows
* Share real use cases

---

## ⭐ If this helps you...

Give it a star ⭐
It helps more developers build AI projects the right way.

---

## 🧩 Philosophy

> Don't let AI control your project
> Build a system that controls AI
