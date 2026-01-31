
# FinSage: AI-Powered Company Research & Analysis Agent

Welcome to FinSage, your intelligent platform for real-time company research, market intelligence, and AI-driven investment analysis. FinSage empowers users to make informed decisions by seamlessly aggregating the latest corporate developments, extracting high-quality insights from trusted sources, and synthesizing them into clear, actionable analyses through advanced agent workflows.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Future Aspects](#future-aspects)
- [Contributors](#contributors)
- [License](#license)

## Introduction

FinSage is an AI-driven research and investment analysis platform that automatically gathers latest company developments, scrapes high-quality sources, and synthesizes insights using LLM-based agents.

It is designed for equity research, investment memos, and financial due diligence, with a clean separation between:

- Backend agent orchestration (FastAPI + LangGraph)
- Frontend UI (Streamlit)
- Web search & content extraction pipeline (SerpAPI + Trafilatura)

## Features

### 1. Agent-Based Architecture

The system is built around modular, role-specific agents such as research, thesis, and analysis, each responsible for a well-defined task. Workflows are orchestrated using LangGraph, ensuring deterministic, debuggable, and extensible execution.

### 2. High-Quality Web Research

Real-time information is sourced through Google News using SerpAPI, enabling timely and relevant market intelligence. Sources are domain-aware and automatically deduplicated to maintain signal quality and reduce noise.

### 3. Robust Content Extraction

Article content is extracted using Trafilatura to remove boilerplate and focus on meaningful text. For edge cases and unsupported pages, BeautifulSoup is used as a reliable fallback parser.

### 4. Clean API + UI Separation
The backend is implemented with FastAPI to handle agent orchestration and analysis logic. A separate Streamlit frontend provides an interactive interface while keeping concerns cleanly decoupled.

### 5. LLM-Agnostic by Design

The system is designed to work with OpenAI, hosted APIs, or open-source language models. Models can be swapped or upgraded without modifying the core workflow logic.

## Tech Stack

FinSage is built using a diverse tech stack:

- SerpAPI for obtaining Google News links
- BeautifulSoup & Trafilatura for scraping news data
- FastAPI for the backend, utilizing LangGraph & LangChain for agent orchestration.
- Streamlit for the frontend
- Any LLM can be used (OpenAI, OSS, locally hosted)
- FAISS for vector embeddings

## Getting Started

To get started with FinSage, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/VineetShenvi/FinSage.git
   cd FinSage
   ```

2. Create a virtual environment.

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables.

   ```bash
   SERP_API_KEY=your_serpapi_key
   OPENAI_API_KEY=your_openai_key
   BACKEND_URL=http://127.0.0.1:8000 (or deployed link)
   ```

4. Run the application:

   Start the Backend
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

   Start the Frontend
   ```bash
   streamlit run ui/streamlit_app.py
   ```

   Visit `http://localhost:8000` in your browser.

## Usage

Explore FinSage and take advantage of its powerful features:

- Search for any company to find its recent investmet news.
- Get financial analysis and investment thesis for the company, along with recommendation(invest/ watch/ avoid).
- Engage with the call-to-action UI for a seamless user experience.

## Future Aspects

Stay tuned for exciting features in future releases:

- Earnings transcript analysis.
- PDF investment memo generation.

## Contributors

- [Vineet Shenvi](https://github.com/VineetShenvi)

## License

FinSage is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as per the terms of the license.

Happy investing with Finsage!
