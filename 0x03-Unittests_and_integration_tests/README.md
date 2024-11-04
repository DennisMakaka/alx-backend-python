# README.md for Project 0x03: Unittests and Integration Tests

## Overview

Welcome to the **0x03. Unittests and Integration Tests** project! This project is dedicated to enhancing your skills in writing comprehensive unit and integration tests for Python functions and classes. By focusing on key testing concepts such as parameterization, mocking, and patching, you will learn how to validate both individual components (unit tests) and their interactions (integration tests) effectively.

## Key Concepts

- **Unit Tests**: These tests assess functions or methods in isolation to ensure they return expected results.
  
- **Integration Tests**: These tests validate the interactions between components of a system, testing end-to-end code paths.

- **Mocking**: This technique involves replacing parts of the code with mock objects to isolate the behavior of the function under test.

- **Patching**: This allows you to temporarily replace objects within your code with mock objects during a test.

## Requirements

- Python 3.7
- Ubuntu 18.04 LTS
- Adherence to `pycodestyle` guidelines (version 2.5)
- All files must be executable and well-documented
- Functions and methods should include type annotations

## Learning Objectives

By the end of this project, you should be able to:

- Differentiate between unit and integration tests.
- Implement common testing practices like mocking and parameterization.
- Use `unittest` and `unittest.mock` libraries effectively.

## Resources

- [unittest - Unit Testing Framework](https://docs.python.org/3/library/unittest.html)
- [unittest.mock - Mock Object Library](https://docs.python.org/3/library/unittest.mock.html)
- Parameterized tests
- Memoization

## Project Structure

The project consists of several tasks that require creating test files to validate various functions and classes. Below is a brief overview of the required files:

- **utils.py**: Contains utility functions.
- **client.py**: Contains client-related functions.
- **fixtures.py**: Provides test data.

## Tasks Overview

1. **Parameterize a Unit Test**
   - Create `TestAccessNestedMap` to test `utils.access_nested_map`.
   - Use `@parameterized.expand` to run tests with different input values and expected outputs.
   - Verify function behavior using `assertEqual`.

2. **Exception Handling**
   - Extend `TestAccessNestedMap` to test exceptions when keys are not found.
   - Use `assertRaises` to confirm that a `KeyError` is raised with the correct message.

3. **Mock HTTP Calls**
   - Create `TestGetJson` to test `utils.get_json` by mocking `requests.get`.
   - Verify that the mocked method is called once and returns expected payloads.

4. **Test Memoization**
   - Create `TestMemoize` to validate the memoize decorator.
   - Use `unittest.mock.patch` to ensure a method is called once even when accessed multiple times.

5. **Patch Decorators for Property**
   - Create `TestGithubOrgClient` in `test_client.py`.
   - Test the `_public_repos_url` property using patch to mock `GithubOrgClient.org`.

6. **Mock Method Calls**
   - Implement `test_public_repos` to test `GithubOrgClient.public_repos`.
   - Patch `get_json` and `_public_repos_url` to control return values and validate method calls.

7. **Parametrize License Checks**
   - Implement `test_has_license` to check if repos have a specific license.
   - Use `@parameterized.expand` to pass different repo and license key combinations.

8. **Integration Test Fixtures**
   - Create `TestIntegrationGithubOrgClient` to test `GithubOrgClient.public_repos`.
   - Use `@parameterized_class` to run tests with fixtures from `fixtures.py`.
   - Mock `requests.get` to return data from fixtures using side effects.

9. **Comprehensive Integration Tests**
   - Implement `test_public_repos` and `test_public_repos_with_license`.
   - Verify that `public_repos` returns results matching expected values from fixtures.


