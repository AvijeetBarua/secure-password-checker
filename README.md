# Secure Password Health Checker & Database

A lightweight local security utility built using **Python** and **SQLite3** designed to evaluate password complexity, execute automated unit tests, and store account credentials using secure cryptographic hashing.

# Features
* **Password Complexity Engine:** Automatically rates inputs as Weak, Medium, or Strong using conditional string evaluation.
* **Cryptographic Storage:** Utilizes Python's native `hashlib` to convert plain-text inputs into secure SHA-256 hashes before database injection.
* **Relational Database Logging:** Maps credentials securely to an isolated SQL layout with unique key constraints to prevent username duplication.
* **Automated Unit Testing:** Includes a dedicated test suite (`test_password.py`) to verify the integrity of the evaluation logic across multiple edge cases.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Database:** SQLite3
* **Libraries:** `hashlib`, `sqlite3`

## 🧪 Testing
To run the automated validation tests, execute the following command in your terminal:
```bash
python test_password.py
