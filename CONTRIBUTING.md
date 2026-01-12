# Contributing to Data Platform Starter Kit

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing.

## Code of Conduct

We are committed to providing a welcoming and inclusive environment for all contributors. Please be respectful and constructive in all interactions.

## Getting Started

### Fork and Clone

```bash
git clone https://github.com/YOUR_USERNAME/data-platform-starter-kit.git
cd data-platform-starter-kit
git remote add upstream https://github.com/BalaVigneshNV/data-platform-starter-kit.git
```

### Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install
```

## Development Workflow

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

Branch naming conventions:
- `feature/description` - New features
- `fix/description` - Bug fixes
- `docs/description` - Documentation updates
- `refactor/description` - Code refactoring
- `test/description` - Test improvements

### 2. Make Your Changes

- Keep commits focused and atomic
- Write clear, descriptive commit messages
- Follow the existing code style

### 3. Write Tests

```bash
# Run existing tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src

# Run specific test file
pytest tests/unit/test_bronze_ingestion.py -v
```

### 4. Code Quality Checks

```bash
# Format code with Black
black src/ tests/ dags/

# Check with Flake8
flake8 src/ tests/ dags/

# Type checking with mypy
mypy src/

# All checks
pre-commit run --all-files
```

### 5. Documentation

- Update docstrings for new functions/classes
- Add/update relevant documentation in `docs/`
- Include examples in docstrings

```python
def process_bronze_data(df: pyspark.sql.DataFrame) -> pyspark.sql.DataFrame:
    """
    Process raw bronze data with ingestion metadata.
    
    Args:
        df: Raw DataFrame from bronze layer
        
    Returns:
        Processed DataFrame with metadata columns
        
    Example:
        >>> df = read_bronze_table('customer_raw')
        >>> processed_df = process_bronze_data(df)
    """
```

### 6. Commit Your Changes

```bash
git add .
git commit -m "feat: add new feature description"
```

Commit message format:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation
- `style:` - Code style changes
- `refactor:` - Code refactoring
- `test:` - Test additions/changes
- `chore:` - Build, dependencies, etc.

### 7. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then open a Pull Request on GitHub.

## Pull Request Process

### PR Requirements

- [ ] Tests pass locally (`pytest tests/`)
- [ ] Code follows style guide (black, flake8)
- [ ] Documentation is updated
- [ ] Commit messages are clear and descriptive
- [ ] No breaking changes without discussion

### PR Description Template

```markdown
## Description
Brief description of changes.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring

## Related Issues
Closes #ISSUE_NUMBER

## Testing
How was this tested?

## Screenshots (if applicable)

## Checklist
- [ ] Tests pass
- [ ] Code is formatted
- [ ] Documentation updated
- [ ] No breaking changes
```

## Areas for Contribution

### High Priority
- [ ] Complete Silver layer data quality framework
- [ ] Implement advanced SCD Type 2 patterns
- [ ] Add streaming pipeline examples
- [ ] Enhance monitoring dashboards

### Medium Priority
- [ ] Additional data source connectors
- [ ] Performance optimization guides
- [ ] Cost optimization scripts
- [ ] Integration tests expansion

### Low Priority
- [ ] Documentation improvements
- [ ] Example datasets
- [ ] Community contributed use cases

## Reporting Issues

### Bug Reports

Include:
1. Description of the bug
2. Steps to reproduce
3. Expected behavior
4. Actual behavior
5. Environment (Python version, OS, etc.)
6. Logs/error messages

### Feature Requests

Include:
1. Use case description
2. Proposed solution
3. Alternative approaches considered
4. Impact on existing functionality

## Code Style Guide

### Python Style

- Follow PEP 8
- Use Black for formatting
- Line length: 100 characters
- Use type hints

```python
def transform_data(
    source_df: pyspark.sql.DataFrame,
    config: Dict[str, Any]
) -> pyspark.sql.DataFrame:
    """Transform source data according to config."""
    return source_df.filter(...).select(...)
```

### Naming Conventions

- Classes: `PascalCase`
- Functions/variables: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Private methods: `_leading_underscore`

### File Organization

```
module/
├── __init__.py
├── main_module.py          # Main logic
├── schemas.py              # Data schemas
├── utils.py                # Helper functions
└── tests/
    ├── __init__.py
    └── test_main_module.py
```

## Documentation Guidelines

### Docstring Format

```python
def function_name(param1: str, param2: int) -> bool:
    """
    Short description.
    
    Longer description if needed.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When value is invalid
        
    Example:
        >>> result = function_name("test", 42)
        >>> print(result)
        True
    """
```

### Markdown Documentation

- Use clear headings (h1-h4)
- Include code examples
- Add diagrams when helpful
- Keep language simple and clear

## Testing Guidelines

### Test Structure

```python
import pytest
from src.bronze.ingestion import ingest_data


class TestIngestData:
    """Tests for data ingestion."""
    
    def test_ingest_valid_data(self, sample_df):
        """Test ingestion with valid data."""
        result = ingest_data(sample_df)
        assert result.count() > 0
    
    def test_ingest_empty_data(self, empty_df):
        """Test ingestion with empty data."""
        result = ingest_data(empty_df)
        assert result.count() == 0
```

### Coverage Requirements

- Minimum 80% code coverage
- All public methods tested
- Edge cases covered

## Questions?

- Open a [GitHub Discussion](https://github.com/BalaVigneshNV/data-platform-starter-kit/discussions)
- Check existing documentation
- Review similar contributions

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing! 🎉
