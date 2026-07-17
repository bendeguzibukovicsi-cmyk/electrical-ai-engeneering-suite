Electrical AI Engineering Suite
A production-ready, open-source platform for electrical engineering design, simulation, analysis, debugging, and documentation.

Overview
The Electrical AI Engineering Suite is a comprehensive engineering assistant that helps electrical engineers design, simulate, analyze, debug, and document electronic systems. It combines powerful AI capabilities with professional engineering tools to create a seamless workflow for hardware development.

Features
AI Agents
Electrical Engineering Agent: Circuit design, analog/digital circuits, power electronics, signal processing, control systems.

Firmware Agent: Support for STM32, ESP32, Arduino, Raspberry Pi Pico, AVR with C/C++/Rust/MicroPython.

PCB Agent: KiCad integration for schematics, layouts, footprints, symbols, netlists, Gerbers, drill files, BOM.

Simulation Agent: LTspice/ngspice integration for automatic simulation, parameter sweeps, frequency response, transient analysis.

Datasheet Agent: PDF parsing, specification extraction, component comparison, alternative recommendations.

BOM Agent: Bill of materials generation with pricing, stock availability, supplier comparison.

Documentation Agent: Markdown, PDF, HTML generation for engineering reports, user manuals, assembly guides.

Technical Stack
Backend: Python 3.12, FastAPI, SQLAlchemy, PostgreSQL, Redis, Docker, JWT Authentication, Celery, WebSockets.

Frontend: Next.js, React, TypeScript, Tailwind CSS, shadcn/ui, React Flow.

AI: Claude Code, OpenAI API, MCP (Model Context Protocol), LangGraph, LangChain, Vector Memory, RAG.

Database: PostgreSQL with pgvector extension for vector embeddings.

DevOps: Docker, Docker Compose, GitHub Actions, Nginx.

Testing: Pytest, Playwright.

AI Integration (Recommended)
To achieve the best performance for engineering reasoning and code generation, we recommend using NVIDIA NIM models via build.nvidia.com.

Recommended Model: nvidia/nemotron-3-ultra-550b

Backend AI Integration
Install dependencies:

Bash
pip install openai python-dotenv
Create a service at services/ai_service.py:

Python
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class AIService:
    def __init__(self):
        # NVIDIA NIMs are compatible with the OpenAI SDK
        self.client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=os.environ.get("NVIDIA_API_KEY")
        )

    def generate_response(self, prompt: str, model: str = "nvidia/nemotron-3-ultra-550b"):
        try:
            completion = self.client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2, # Low temperature for precise engineering tasks
                max_tokens=4096,
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Error communicating with NVIDIA API: {str(e)}"

ai_service = AIService()
Getting Started
Prerequisites
Docker and Docker Compose

Node.js 18+ and npm

Python 3.12+

Installation
Clone the repository:

Bash
git clone https://github.com/bendeguzibukovicsi-cmyk/electrical-ai-engineering-suite.git
cd electrical-ai-engineering-suite
Set up environment variables:

Bash
cp .env.example .env
(Open your .env file and add your NVIDIA_API_KEY=nvapi-... and database credentials).

Start the infrastructure:

Bash
docker-compose up -d
Install and run frontend:

Bash
cd frontend
npm install
npm run dev
Architecture
The system follows a microservices architecture with:

API Gateway for routing

Authentication Service

Individual services for each AI agent

Shared database and caching layers

Event-driven communication via Redis

Documentation
API Documentation

Architecture Overview

Development Guide

Deployment Guide

User Guide

Contributing
We welcome contributions! Please see our Contributing Guide for details.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For questions and support, please open an issue on GitHub.
