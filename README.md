# PyUtils

A lightweight, standard library-based Python utility collection built by the community, for the community.

## Overview

PyUtils provides common utility functions that complement Python's standard library. Our focus is on:

- **Minimal dependencies** - using only Python standard library wherever possible
- **Compatibility** - works with Python 3.7+
- **Simplicity** - easy to understand and use
- **Reliability** - well-tested and robust
- **Performance** - optimized implementations

## Project Modules

### Core (Beginner-friendly)
Basic utilities for common operations on built-in types.

```python
# Example usage
from pyutils.core.object_utils import get_default_if_none

value = None
result = get_default_if_none(value, "default")  # Returns "default"
```

### Text (Beginner to Intermediate)
Text processing utilities beyond what's available in the string methods.

```python
# Example usage
from pyutils.text.string_utils import pad_left

padded = pad_left("123", 5, "0")  # Returns "00123"
```

### Collections (Intermediate)
Utilities for working with Python collections.

```python
# Example usage
from pyutils.collections.list_utils import filter_items

filtered = filter_items(["a", "b", "c"], lambda x: x > "b")  # Returns ["c"]
```

### IO (Intermediate)
File and resource handling utilities.

```python
# Example usage
from pyutils.io.file_utils import read_file_safely

content = read_file_safely("test.txt", encoding="utf-8")
```

### Validation (Intermediate)
Data validation utilities.

```python
# Example usage
from pyutils.validation.string_validator import StringValidator

result = (StringValidator()
          .not_empty()
          .max_length(10)
          .matches(r"[A-Za-z]+")
          .validate("PyUtils"))
```

### Concurrent (Advanced)
Threading and multiprocessing utilities.

```python
# Example usage
from pyutils.concurrent.async_utils import run_with_timeout

result = run_with_timeout(long_running_function, timeout_seconds=5)
```

## Getting Started

### Prerequisites
- Python 3.8 or higher

### Installation
```bash
# Not yet on PyPI - install from GitHub
pip install git+https://github.com/nexgenclub/PyUtils.git
```

### Building from Source
```bash
# Clone the repository
git clone https://github.com/nexgenclub/PyUtils.git

# Navigate to the project directory
cd PyUtils

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest
```

## How to Contribute

We welcome contributions from Python developers of all skill levels!

1. Check out our [Contribution Guidelines](CONTRIBUTING.md)
2. Look for issues labeled "good first issue" to get started
3. Join our community discussions

## License

This project is licensed under the MIT License - see the LICENSE file for details.