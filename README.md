# 📂 Python File Handling & Data Persistence

This repository contains a collection of Python scripts designed to practice **File Input/Output (I/O)** operations. It demonstrates how to persist data using three common file formats: **Plain Text (.txt)**, **CSV**, and **JSON**.

## 🚀 Overview

These scripts explore the lifecycle of data persistence: creating files, reading data, appending new information, and handling errors when files go missing.

### 1. Text File Operations (`.txt`)
Basic manipulation of human-readable logs.
* **`create_file.py`**: Initializes a mission log with write mode (`w`).
* **`add_entry_file.py`**: Uses `datetime` to append timestamped entries to the log without overwriting existing data.
* **`read_file.py`**: Reads the file and prints the full history to the console.

### 2. CSV Data Processing (`.csv`)
Handling structured data for spreadsheets or inventories.
* **`write_csv.py`**: Uses the `csv` library to write rows of inventory items (Name, Quantity, Price).
* **`read_csv.py`**: Reads the inventory file using `DictReader` and calculates the total value of gold based on quantity and price.

### 3. JSON & Data Serialization (`.json`)
Managing complex data structures (dictionaries and lists) for game saves or configurations.
* **`read_edit_json.py`**: Simulates a "Hero Save" system. It dumps a dictionary to a file, reads it back, modifies attributes (leveling up), and saves the progress.
* **`view_add_json.py`**: A **Mini-Project**. A menu-driven CLI app that manages a High Score board. It allows users to view scores or add new ones, persisting the list to `scores.json` between runs.

### 4. Error Handling
* **`file_error_handling.py`**: Demonstrates the use of `try/except` blocks to handle `FileNotFoundError` gracefully by creating missing files automatically.

## 🛠️ Concepts Applied

* **Modes**: Write (`w`), Read (`r`), Append (`a`).
* **Context Managers**: Using `with open(...)` to ensure files close safely.
* **Libraries**: `csv`, `json`, `datetime`.
* **Data Serialization**: Converting Python objects (dicts/lists) into storable string formats.

## 💻 Usage

Run any script using the Python command:

```bash
# Example: Run the High Score Manager
python view_add_json.py
