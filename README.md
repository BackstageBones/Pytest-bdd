# Pytest-BDD Project

This repository demonstrates Behavior-Driven Development (BDD) in Python using the `pytest-bdd` plugin for the `pytest` testing framework. It provides examples of how to write and execute BDD-style tests with `pytest-bdd`.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Behavior-Driven Development (BDD) is an extension of Test-Driven Development (TDD) that encourages collaboration among developers, testers, and business stakeholders. It involves writing tests in a natural language style, which improves communication and understanding of system behavior.

The `pytest-bdd` plugin integrates BDD into the `pytest` framework, allowing you to write tests using Gherkin syntax and leverage `pytest`'s features. [Learn more](https://github.com/pytest-dev/pytest-bdd)

## Features

- Write tests in Gherkin syntax (Given, When, Then)
- Leverage `pytest` fixtures and plugins
- Organize scenarios in feature files
- Generate test reports

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/BackstageBones/Pytest-bdd.git
   cd Pytest-bdd
   ```

2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Write Feature Files:**

   Define your scenarios in `.feature` files using Gherkin syntax. Place these files in the `features` directory.

2. **Implement Step Definitions:**

   Create corresponding step definitions in Python files within the `steps` directory. Use decorators like `@given`, `@when`, and `@then` to link Gherkin steps to Python functions.

3. **Run Tests:**

   Execute the tests using `pytest`:

   ```bash
   pytest
   ```

   For more detailed output, use:

   ```bash
   python -m pytest -s --alluredir allure-results --clean-alluredir
   ```

## Project Structure

```plaintext
Pytest-bdd/
├── locators /
├── pages /
├── modules/
├── tests/
│   └── features/
│        ├── item sorting.feature
│        ├── login.feature
│        ├── register.feature
│        └── shopping flow.feature
├── steps_definitions
│   └── test_register.py
├── conftest.py
├── requirements.txt
└── README.md
```

- **`features/`**: Contains `.feature` files written in Gherkin syntax.
- **`steps/`**: Contains Python files with step definitions.
- **`tests/`**: Contains additional test cases and configurations.
- **`conftest/`** Contains pytests re-usable global fixtures
- **`requirements.txt`**: Lists the Python dependencies for the project.
- **`README.md`**: Provides an overview and instructions for the project.

## Contributing

Contributions are welcome! If you have suggestions, improvements, or issues, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

