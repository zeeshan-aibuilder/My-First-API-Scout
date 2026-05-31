# 🪙 My First API Scout (Crypto Fetcher)

> A production-grade CLI tool built in Python to fetch real-time cryptocurrency data using the CoinGecko API and log it efficiently using OS-level operations.

## 🚀 Overview
This project serves as a foundational architecture test for network requests, OS environment management, and tabular data parsing. It dynamically formats API endpoints based on user input and sanitizes JSON payloads before committing them to a local CSV database.

## 🧠 Core Engineering Features
* **Dynamic API Routing:** Constructs API endpoints dynamically based on sanitized user inputs (`capitalize()`, `upper()`).
* **OS Lifecycle Management:** Automatically detects the host OS to clear terminals and builds necessary local directories (`os.makedirs`) if missing.
* **Persistent Tabular Logging:** Utilizes the `csv` library with timestamp encoding to safely append session data without risking data overwrites or formatting corruption.

## 💻 Execution & Setup
To run this project, ensure you have a Python virtual environment activated.

```bash
# Install required dependencies
pip install requests

# Execute the application
python api_scout.py
