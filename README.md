# Command Line Calculator
A simple command-line calculator built using Python.  
It runs in a REPL (loop until exit), supports basic arithmetic operations, and includes unit tests with 100% coverage.

## Features
- Addition (+), Subtraction (-), Multiplication (*), Division (/)
- Continuous input until user types `exit`
- Error handling for invalid input and divide by zero
- Unit tests using pytest
- 100% test coverage
- GitHub Actions CI using a `.github` folder

## Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Run
python3 calculator.py

## Test
pytest --cov=calculator
