# 🧠 Multi-Agent Content Writing System

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![CrewAI](https://img.shields.io/badge/CrewAI-enabled-green)
![License](https://img.shields.io/badge/license-MIT-blue)

This project demonstrates a simple multi-agent system for collaborative content generation using **CrewAI**. The agents simulate the workflow of writing an article by splitting the task into three distinct roles: planning, writing, and reviewing.

## ✨ Scenario
A team of agents collaborates to write an article titled **"The Rise of AI in Everyday Life"**.

## 🤖 Agent Roles

- **PlannerAgent**: Creates an outline for the article.
- **WriterAgent**: Generates content for each section of the outline.
- **ReviewerAgent**: Reviews and edits the final draft.

## 🔁 Agent Collaboration
Agents explicitly pass information from one to another to complete the writing workflow:

## 🚀 How to Run
Make sure you have Python 3.10+ and the required dependencies.

```bash
pip install -r requirements.txt
python main.py

## 📂 Project Structure
multi_agent_project/
├── agents/
│   ├── planner_agent.py
│   ├── writer_agent.py
│   └── reviewer_agent.py
├── logs/
│   └── agent_logs.txt
├── main.py
├── requirements.txt
└── README.md
