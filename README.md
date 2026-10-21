# Secure Code Review Assistant

A Python-based web application that helps users review Python source code for potential security issues.

## Features

- Upload Python files for static security analysis.
- Uses Bandit to identify potential security issues.
- Provides explanations, risk information, and remediation suggestions.
- Displays example secure coding patterns where available.
- Generates an HTML security review report.
- Includes automated tests for core functionality and web routes.

## Technologies Used

- Python
- Flask
- Bandit
- HTML and CSS
- pytest

## Getting Started

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd secure-code-review
```

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

Install Flask, Bandit, and pytest in your environment:

```powershell
pip install flask bandit pytest
```

### 4. Run the application

```powershell
python app.py
```

Open the local URL displayed in the terminal in your browser.

### 5. Run tests

```powershell
python -m pytest -v
```

## Security Note

This project performs static analysis; it does not prove that code is completely secure. Review findings and recommendations before applying them. Do not upload confidential source code. The Flask development server is intended for local development, not public production use.

## Project Status

Student project under development. Features and testing may evolve as improvements are made.
