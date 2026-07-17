# Electrical AI Engineering Suite

A production-ready, open-source platform for electrical engineering design, simulation, analysis, debugging, and documentation.

## Overview

The Electrical AI Engineering Suite is a comprehensive engineering assistant that helps electrical engineers design, simulate, analyze, debug, and document electronic systems. It combines powerful AI capabilities with professional engineering tools to create a seamless workflow for hardware development.

---

## Features

### AI Agents

* **Electrical Engineering Agent**: Circuit design, analog/digital circuits, power electronics, signal processing, control systems.
* **Firmware Agent**: Support for STM32, ESP32, Arduino, Raspberry Pi Pico, AVR with C/C++/Rust/MicroPython.
* **PCB Agent**: KiCad integration for schematics, layouts, footprints, symbols, netlists, Gerbers, drill files, BOM.
* **Simulation Agent**: LTspice/ngspice integration for automatic simulation, parameter sweeps, frequency response, transient analysis.
* **Datasheet Agent**: PDF parsing, specification extraction, component comparison, alternative recommendations.
* **BOM Agent**: Bill of materials generation with pricing, stock availability, supplier comparison.
* **Documentation Agent**: Markdown, PDF, HTML generation for engineering reports, user manuals, assembly guides.

### Technical Stack

* **Backend**: Python 3.12, FastAPI, SQLAlchemy, PostgreSQL, Redis, Docker, JWT Authentication, Celery, WebSockets.
* **Frontend**: Next.js, React, TypeScript, Tailwind CSS, shadcn/ui, React Flow.
* **AI**: Claude Code, OpenAI API, MCP (Model Context Protocol), LangGraph, LangChain, Vector Memory, RAG.
* **Database**: PostgreSQL with pgvector extension for vector embeddings.
* **DevOps**: Docker, Docker Compose, GitHub Actions, Nginx.
* **Testing**: Pytest, Playwright.

---

## Getting Started

### Prerequisites

Ensure you have the following installed on your machine and that ports **5432**, **6379**, **8000**, and **3000** are available:
* Docker and Docker Compose
* Node.js 18+ and npm
* Python 3.12+ 

### Installation

**1. Clone the repository:**
```bash
git clone [https://github.com/bendeguzibukovicsi-cmyk/electrical-ai-engineering-suite.git](https://github.com/bendeguzibukovicsi-cmyk/electrical-ai-engineering-suite.git)
cd electrical-ai-engineering-suite
