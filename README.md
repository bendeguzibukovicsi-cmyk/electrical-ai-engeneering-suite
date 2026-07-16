A production-ready, open-source platform for electrical engineering design, simulation, analysis, debugging, and documentation.

## Overview

The Electrical AI Engineering Suite is a comprehensive engineering assistant that helps electrical engineers design, simulate, analyze, debug, and document electronic systems. It combines powerful AI capabilities with professional engineering tools to create a seamless workflow for hardware development.

## Features

### AI Agents
- **Electrical Engineering Agent**: Circuit design, analog/digital circuits, power electronics, signal processing, control systems
- **Firmware Agent**: Support for STM32, ESP32, Arduino, Raspberry Pi Pico, AVR with C/C++/Rust/MicroPython
- **PCB Agent**: KiCad integration for schematics, layouts, footprints, symbols, netlists, Gerbers, drill files, BOM
- **Simulation Agent**: LTspice/ngspice integration for automatic simulation, parameter sweeps, frequency response, transient analysis
- **Datasheet Agent**: PDF parsing, specification extraction, component comparison, alternative recommendations
- **BOM Agent**: Bill of materials generation with pricing, stock availability, supplier comparison
- **Documentation Agent**: Markdown, PDF, HTML generation for engineering reports, user manuals, assembly guides

### Technical Stack
- **Backend**: Python 3.12, FastAPI, SQLAlchemy, PostgreSQL, Redis, Docker, JWT Authentication, Celery, WebSockets
- **Frontend**: Next.js, React, TypeScript, Tailwind CSS, shadcn/ui, React Flow
- **AI**: Claude Code, OpenAI API, MCP (Model Context Protocol), LangGraph, LangChain, Vector Memory, RAG
- **Database**: PostgreSQL with pgvector extension for vector embeddings
- **DevOps**: Docker, Docker Compose, GitHub Actions, Nginx
- **Testing**: Pytest, Playwright

## Getting Started

### Prerequisites
- Docker and Docker Compose
- Node.js 18+ and npm
- Python 3.12+
- PostgreSQL
- Redis

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/electrical-ai-engineering-suite.git
cd electrical-ai-engineering-suite
```

2. Set up environment variables:
```bash
git clone https://github.com/bendeguzibukovicsi-cmyk/electrical-ai-engeneering-suite.git
```

3. Start the services:
```bash
docker-compose up -d
```

4. Install frontend dependencies:
```bash
cd frontend
npm install
```

5. Start the development server:
```bash
npm run dev
```

## Architecture

The system follows a microservices architecture with:
- API Gateway for routing
- Authentication Service
- Individual services for each AI agent
- Shared database and caching layers
- Event-driven communication via Redis

## Documentation

- [API Documentation](docs/api.md)
- [Architecture Overview](docs/architecture.md)
- [Development Guide](docs/development.md)
- [Deployment Guide](docs/deployment.md)
- [User Guide](docs/user-guide.md)

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions and support, please open an issue on GitHub.
