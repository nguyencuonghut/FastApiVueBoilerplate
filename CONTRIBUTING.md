# Contributing to FastAPI Vue Boilerplate

## Getting Started

1. Fork the repository
2. Clone your fork
3. Create a feature branch: `git checkout -b feature/your-feature`
4. Make your changes
5. Commit: `git commit -am 'Add your feature'`
6. Push: `git push origin feature/your-feature`
7. Submit a pull request

## Development Guidelines

### Backend (Python/FastAPI)

- Follow PEP 8 style guide
- Use type hints
- Add docstrings to functions
- Test with `pytest`
- Use SQLAlchemy ORM

```bash
# Format code
black app/

# Lint
flake8 app/

# Type checking
mypy app/
```

### Frontend (Vue 3)

- Use Composition API
- Follow Vue 3 best practices
- Use TypeScript when possible
- Keep components small and focused
- Use PrimeVue components

```bash
# Format code
npm run lint

# Build
npm run build
```

## Coding Standards

### Backend
- Keep functions small and focused
- Use dependency injection
- Implement proper error handling
- Add logging statements
- Write unit tests

### Frontend
- One component per file
- Reusable components over single-use
- Clear naming conventions
- PropTypes or TypeScript
- Reactive data management with Pinia

## Testing

```bash
# Backend tests
pytest

# Frontend tests
npm run test
```

## Documentation

- Update README for major changes
- Add docstrings to public APIs
- Update comments for complex logic

## Pull Request Process

1. Ensure tests pass
2. Update CHANGELOG if needed
3. Add description of changes
4. Reference any related issues

## Code of Conduct

- Be respectful and inclusive
- Help newcomers
- Report issues constructively
- Focus on code quality

---

Thank you for contributing! 🎉
