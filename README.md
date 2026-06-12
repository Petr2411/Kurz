# Countries Data Analyzer

A Python-based command-line application that integrates with an external REST API to fetch, process, and analyze global country data. This project demonstrates clean backend architecture, network communication, and robust data handling.

## 🚀 Features
* **External API Integration:** Fetches real-time global data using the `requests` library.
* **Data Cleaning & Transformation:** Parses complex JSON structures and handles missing or inconsistent data fields safely.
* **Architectural Cleanliness:** Built with a strict focus on professional software design principles.

## 🛠️ Software Engineering Principles Applied

### Single Responsibility Principle (SRP)
The codebase is strictly decoupled to ensure high maintainability:
* **Network Layer:** Responsible solely for API communication, HTTP requests, and error handling.
* **Business Logic Layer:** Responsible for parsing, filtering, and analyzing the raw data.
* **Presentation Layer:** Manages user input and clean console output formatting.

### Don't Repeat Yourself (DRY)
* Avoided hardcoded values by implementing centralized configuration.
* Reusable helper methods handle repetitive data parsing and dictionary lookups, keeping the codebase lean and efficient.

## 📦 Tech Stack
* **Language:** Python 3
* **Libraries:** `requests` (HTTP communication), `json` (data parsing)

## 🔧 How to Run
1. Clone the repository:
```bash
   git clone [https://github.com/Petr2411/countries-data-analyzer.git](https://github.com/Petr2411/countries-data-analyzer.git)

Install dependencies:

Bash
   pip install requests
Run the application:

Bash
   python main.py
