# 🧠 Quotes Generation Chatbot

A lightweight chatbot app built using **FastAPI**, **HTML/JavaScript**, and managed with **Poetry**. It generates quotes based on user queries across different categories like funny, motivational, love, sad, and life.

---

## 🚀 Features

- 🔍 Keyword-based category matching
- 💬 Clean and responsive web UI
- 🔢 Supports multiple quotes in one go (e.g., “3 funny quotes”)
- ⚡ FastAPI-powered backend
- 📦 Poetry for package management

---

## 📁 Project Structure

quotes-generation/
├── app.py            # FastAPI backend that serves API and HTML
├── quotes.json       # JSON file storing categorized quotes
├── index.html        # Frontend UI for chatbot (served by FastAPI)
├── pyproject.toml    # Poetry configuration and dependencies
├── .gitignore        # Git ignore rules
├── README.md         # Project documentation