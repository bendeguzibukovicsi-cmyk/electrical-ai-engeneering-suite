# Contributing to Electrical AI Engineering Suite

Thank you for considering contributing to the Electrical AI Engineering Suite! We welcome contributions from the community.

## How to Contribute

There are many ways to contribute to the project:

1. **Report bugs** - Use the issue tracker to report bugs
2. **Suggest features** - Use the issue tracker to suggest new features
3. **Improve documentation** - Help improve our documentation
4. **Fix bugs** - Pick up an issue and fix it
5. **Implement features** - Help implement new features
6. **Write tests** - Help improve test coverage

## Getting Started

1. Fork the repository
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/electrical-ai-engineering-suite.git
   ```
3. Create a new branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. Make your changes
5. Commit your changes:
   ```bash
   git commit -m "Add feature: your feature name"
   ```
6. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
7. Open a pull request

## Development Setup

### Prerequisites

- Docker and Docker Compose
- Node.js 18+ and npm
- Python 3.12+
- PostgreSQL
- Redis

### Setting Up Development Environment

1. Copy the environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` with your configuration

3. Start the services:
   ```bash
   docker-compose up -d
   ```

4. Install frontend dependencies:
   ```bash
   cd frontend
   npm install
   ```

5. Run database migrations:
   ```bash
   cd backend
   python -m alembic upgrade head
   ```

6. Start the development servers:
   ```bash
   # In one terminal
   cd backend
   python -m uvicorn app.main:app --reload
   
   # In another terminal
   cd frontend
   npm run dev
   ```

## Code Style

We follow these coding standards:

### Python
- Follow PEP 8
- Use type hints
- Document functions and classes with docstrings
- Use meaningful variable names

### JavaScript/TypeScript
- Use TypeScript for all new code
- Follow Airbnb JavaScript Style Guide
- Use ESLint and Prettier for code formatting

### Git
- Write clear, descriptive commit messages
- Keep commits focused on a single change
- Reference issues in commit messages when applicable

## Pull Request Process

1. Ensure your code passes all tests
2. Ensure your code follows the coding standards
3. Update documentation as needed
4. Keep your pull request focused on a single feature or fix
5. Respond to feedback from maintainers

## Reporting Bugs

When reporting bugs, please include:
- A clear description of the issue
- Steps to reproduce the problem
- Expected behavior vs. actual behavior
- Screenshots or logs if applicable
- Your environment (OS, browser, etc.)

## Feature Requests

When requesting features, please include:
- A clear description of the feature
- Why the feature would be useful
- Any potential implementation considerations
- Examples of how the feature would be used

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.
