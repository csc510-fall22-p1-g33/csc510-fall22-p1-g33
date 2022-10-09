# Testing

## Running Tests

To run tests, use the following command from the project directory.
```
pytest -rA tests/*.py 
```

## Writing Tests

### Test File Conventions

Test files must be put inside the `test` folder.

Test file names should fit the following pattern: `test_*.py`.

Below are some examples of valid test file names.
```
test_foo.py
test_foo_bar.py
```

### Test Method Conventions

Test methods must be put inside test files.

Test method names should fit the following pattern: `test_*()`. Alternatively, test methods may also be named `test()`.

Below are some examples of valid test method names.
```python
test()
test_foo()
test_foo_bar()
```

### Testing Conditionals

To test a conditional within a test method, use the `assert` statement. `assert` expects the conditional to be `True`, in which case the test is considered to pass, otherwise, the test is considered to fail.

```python
assert 1 == 1 // PASS
```
```python
assert 1 == 2 // FAIL
