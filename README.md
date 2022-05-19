# Intro to unit testing with Python


I'll be covering:

* What is a unit test?
  * how to approach functions
  * how do we write our cod3e
* Why do we write unit test?
  * Coverage
* What's special about Python vs some other languages?
  * pytest
  * pytest-cov
* What are fixtures?
* What is a mock how to use them?
  * What happens when we can't test some component of our function?


```shell


# Running coverage
pytest --cov=.  test_script.py


# Running integration tests
pytest -v -m integration --cov=examples.py  test_examples.py
```
