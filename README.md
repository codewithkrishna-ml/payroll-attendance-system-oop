# Employee Payroll & Attendance System 💼📊

An automated backend console application built in Python using core **Object-Oriented Programming (OOP)** architectures to manage corporate workforces. This system seamlessly coordinates daily employee attendance tracking logs with dynamic monthly payroll calculations based on explicit days present, complete with built-in ledger persistence handlers.

---

## 🌟 About the Developer

*   **Age/Class:** 16 Years Old (Class 10th) 🎯
*   **Future Goal:** B.Tech in Artificial Intelligence and Machine Learning (AI-ML).
*   **Milestone:** Successfully completed the **100 Days of Code** challenge!
*   **Current Focus:** Learning Data Structures & Algorithms (DSA) and data science libraries like **NumPy** and **Pandas**.

---

## ✨ Key Features

*   **Dynamic Corporate Registry:** Adds employee profiles with automated sequential counter metrics starting from an initial baseline (`ID: 101`).
*   **Daily Attendance Monitor:** Tracks operational states using character codes (`P` for Present / `A` for Absent), appending runtime tracking arrays upon verification.
*   **Pro-Rata Pay Engine:** Automatically computes a precise per-day financial rate (`Base Salary / 30`) to output neat, comprehensive salary slips reflecting absolute days present.
*   **Tabular Data Dashboard:** Implements clean, left-aligned terminal grid rendering loops to view overall structural employee stats at a single glance.
*   **Scratch-Built CSV Ledger:** Exports system records into organized spreadsheet formats (`employee_attendance_ledger.csv`) manually without using bulk external libraries.

---

## 🛠️ OOP Concepts & Architecture Demonstrated

This enterprise-inspired prototype prioritizes clean data encapsulation, modular design, and robust input sanitization:
*   **Classes & System Abstraction:** Structured cleanly around independent logical blueprints: `Employee` (individual metadata container) and `PayrollSystem` (the core tracking database controller).
*   **Composition & State Tracking:** The master management class aggregates multiple dynamic references inside a central dictionary layout (`employee_db`), mapping data modifications efficiently via object hashes.
*   **Input Validation Checkpoints:** Features defensive code blocks (`try-except ValueError`) that trap floating-point conversion errors instantly to safeguard pricing parameters from accidental user crashes.

---

## 🚀 How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone https://github.com
    ```
2.  **Navigate to the project folder:**
    ```bash
    cd payroll-attendance-system-oop
    ```
3.  **Run the interactive employee manager loop:**
    ```bash
    python main.py
    ```

---

## 📝 Prerequisites
*   **Python 3.x** installed on your machine.
*   Runs completely on pure Python architecture without needing external library components.
