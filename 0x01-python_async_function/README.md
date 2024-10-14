# 0x01. Python - Async

## Project Overview

This project introduces asynchronous programming in Python. You will learn how to write asynchronous code using `async` and `await`, manage concurrency with coroutines, and work with `asyncio` tasks. The project covers fundamental concepts of asynchronous I/O, task execution, and time measurement.

## Project Requirements
- All files must be written in Python 3.7.
- Files must comply with the `pycodestyle` (2.5.x).
- Every function and coroutine must be type-annotated.
- Documentation is required for every module and function.
- Files should end with a new line and must be executable.

## Project Tasks

### 0. The basics of async
Write an asynchronous coroutine `wait_random` that takes an integer `max_delay` (default value: 10) and returns a random delay (float) between 0 and `max_delay` seconds.

- **File:** `0-basic_async_syntax.py`

### 1. Let's execute multiple coroutines at the same time with async
Create an async routine `wait_n` that takes two integers, `n` and `max_delay`, and spawns `wait_random` `n` times. Return the list of all delays in ascending order without using `sort()`.

- **File:** `1-concurrent_coroutines.py`

### 2. Measure the runtime
Create a `measure_time` function that calculates the total execution time for `wait_n(n, max_delay)` and returns `total_time / n`.

- **File:** `2-measure_runtime.py`

### 3. Tasks
Write a function `task_wait_random` that takes an integer `max_delay` and returns an `asyncio.Task` object for `wait_random`.

- **File:** `3-tasks.py`

### 4. Tasks (Modified `wait_n`)
Modify the `wait_n` function into `task_wait_n`, using `task_wait_random` instead of `wait_random`.

- **File:** `4-tasks.py`

## Repository Structure

- **GitHub Repository:** `alx-backend-python`
- **Directory:** `0x01-python_async_function`

## Resources
- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- `random.uniform` function for generating random delay.
