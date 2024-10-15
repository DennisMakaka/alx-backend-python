# 0x02. Python - Async Comprehension

## Python - Backend

This project focuses on asynchronous programming in Python, specifically on writing asynchronous generators and comprehensions. You'll explore how to handle asynchronous operations effectively and measure their performance.

### Resources
Here are some resources to help you understand the concepts covered in this project:

- [PEP 530 – Asynchronous Comprehensions](https://www.python.org/dev/peps/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep530)
- [Type-hints for generators](https://docs.python.org/3/library/typing.html#typing.Generator)

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using **Python 3.7**.
- The first line of all your files should be exactly: `#!/usr/bin/env python3`.
- Your code must follow the `pycodestyle` style (version 2.5.x).
- All functions and coroutines must be type-annotated.
- Your files should end with a new line.
- Your modules and functions should have proper documentation.
- A **README.md** file at the root of the project folder is mandatory.

## Project Structure

### Task 0: Async Generator

Write a coroutine called `async_generator` that:
- Loops 10 times.
- Asynchronously waits for 1 second, then yields a random number between 0 and 10.

### Task 1: Async Comprehension

- Import `async_generator` from the previous task.
- Write a coroutine called `async_comprehension` that collects 10 random numbers using an async comprehension over `async_generator`.
- Return the 10 random numbers.

### Task 2: Run Time for Four Parallel Comprehensions

- Import `async_comprehension` from the previous file.
- Write a coroutine called `measure_runtime` that executes `async_comprehension` four times in parallel using `asyncio.gather`.
- Measure and return the total runtime (approximately 10 seconds).

## Repository

- **GitHub repository**: `alx-backend-python`
- **Directory**: `0x02-python_async_comprehension`
- **Files**:
  - `0-async_generator.py`
  - `1-async_comprehension.py`
  - `2-measure_runtime.py`


