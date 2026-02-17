# QA Web Automation Framework

Selenium + PyTest automation framework built using the Page Object Model (POM).

## Tech Stack

- Python 3.13
- Selenium WebDriver
- PyTest
- WebDriver Manager
- PyTest-HTML

## Features

- Page Object Model architecture
- Explicit waits (WebDriverWait)
- Headless execution support
- Screenshot capture on failure
- HTML test reporting

## Project Structure

qa-web-automation-framework/
│
├── pages/ # Page Object Models
│ ├── login_page.py
│ └── inventory_page.py
│
├── tests/ # Test cases
│ ├── test_login.py
│ └── test_smoke.py
│
├── utils/ # Framework utilities
│ └── driver_factory.py
│
├── screenshots/ # Auto-created on test failure
│
├── conftest.py # PyTest fixtures and hooks
├── pytest.ini # Test configuration
├── requirements.txt # Project dependencies
└── README.md

## Design Decisions

- Implemented Page Object Model (POM) to separate UI locators from test logic.
- Used explicit waits (WebDriverWait) to improve stability and reduce flaky tests.
- Centralized WebDriver creation in a driver factory for maintainability.
- Added screenshot capture on failure to assist debugging.
- Configured HTML reporting for better test visibility.

## Setup & Execution

### 1. Clone the repository

git clone https://github.com/MauDevFernandes/qa-web-automation-framework.git
cd qa-web-automation-framework

### 2. Create virtual environment

python -m venv venv

### 3. Activate virtual environment (Windows)

venv\Scripts\activate

### 4. Install dependencies

pip install -r requirements.txt

### 5. Run tests

pytest

### 6. Run in headless mode

pytest --headless

## Sample Test Coverage

- Valid login scenario
- Invalid login scenario (error validation)
- Basic smoke test

## Future Improvements

- CI/CD integration with GitHub Actions
- Parameterized test data
- Cross-browser support
- Logging integration
