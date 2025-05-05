# PyUtils Contribution Guidelines

Thank you for considering contributing to PyUtils! This document outlines how to contribute effectively to our project.

## Getting Started

1. **Fork the repository** to your GitHub account
2. **Clone your fork** to your local machine
3. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements-dev.txt
   ```
4. **Verify setup** by running tests:
   ```bash
   pytest
   ```

## Contribution Workflow

1. **Choose an issue** from the issue tracker or create a new one
   - Look for issues labeled "good first issue" if you're new
   - Comment on the issue to let others know you're working on it

2. **Create a branch** with a descriptive name
   - Use the format: `feature/short-description` or `bugfix/short-description`

3. **Write your code** following our coding standards
   - Ensure your code has appropriate unit tests
   - Run existing tests to verify you haven't broken anything

4. **Submit a pull request**
   - Include a clear title and description
   - Reference the issue number in your PR description using #number
   - Wait for a code review

## Coding Standards

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Use 4 spaces for indentation, not tabs
- Use docstrings for all modules, classes, and functions (follow [Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html))
- Keep functions small and focused on a single responsibility
- Use type hints wherever possible
- Use meaningful variable and function names
- Write unit tests for all new functionality

## Unit Testing

- Every utility module must have a corresponding test file
- Test coverage should be at least 80% for new code
- Tests should include:
  - Normal case tests
  - Edge case tests (empty values, None, etc.)
  - Performance tests for critical operations
- We use pytest for testing

## Difficulty Levels for Contributors

We tag issues with difficulty levels to help contributors find appropriate tasks:

- **Beginner**: Requires basic Python knowledge. Good for first-time contributors.
- **Intermediate**: Requires good understanding of Python features and OOP concepts.
- **Advanced**: Requires deep knowledge of Python internals, concurrency, or complex algorithms.

## Code Review Process

- All code changes require at least one review
- Reviewers will check for:
  - Correctness of implementation
  - Code quality and adherence to standards
  - Appropriate test coverage
  - Performance considerations
- We use Black and flake8 for code formatting and linting, which will be run automatically in CI

## Documentation

- All public functions should have docstrings
- Update the appropriate documentation in the docs/ directory
- Include examples in the examples/ directory for new features

## Need Help?

- Check our Wiki for detailed documentation
- Ask questions in our discussion forum/chat
- Join our regular community meetings

We appreciate your contributions and look forward to building this toolkit together!