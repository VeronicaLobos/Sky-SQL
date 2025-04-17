# Sky-SQL

## Overview

This program provides a command-line interface (CLI) to query and display data about flight delays across various US airports and airlines. It utilizes a pre-existing  SQLite database containing historical flight data.

This project was developed as part of a bootcamp assignment, focusing on implementing functions and the necessary SQL queries to retrieve specific flight information.

## Technology Stack

*   Python 3.12
*   SQLite
*   SQLAlchemy
*   SQL

## Functionality

The CLI allows users to retrieve the following information:

*   Details for a specific flight by its ID.
*   A list of flights occurring on a specific date.
*   Flights delayed over 20 minutes, aggregated by airline.
*   Flights delayed over 20 minutes, aggregated by origin airport.

## Key Technical Aspects

*   **Command-Line Interface (CLI):** Provides the user interaction layer (implementation provided for the assignment).
*   **Data Source:** Reads from a provided SQLite database containing historical flight data (tables and data provided).
*   **Data Layer (DL):**
    *   Abstracts database interactions.
    *   Manages the database connection using **SQLAlchemy**.
    *   Fetches data from the database using **raw SQL queries**.

## Project Structure
```plaintext
Sky-SQL/
├── /data                   # Directory for data-related files
│   └── flights.sqlite3     # The SQLite database file
├── data.py                 # Data Layer implementation
├── main.py                 # Main application logic and CLI
├── requirements.txt        # List of Python dependencies
└── README.md               # Project overview and instructions
```
*  Tables in the database:
    *  `flights`: Contains flight information, including flight ID, date, origin, destination, and delay.
    *  `airlines`: Contains airline information, including airline ID and name.
    *  `airports`: Contains airport information, including airport ID and name.

## Installation

*   Clone this repository
    ```bash
    git clone https://github.com/VeronicaLobos/Sky-SQL.git
    ```
*  Navigate to the project directory:
    ```bash
    cd path/to/your/project
    ```
*   Set up a virtual environment (ensure that you have Python 3.12 installed):
    ```bash
    python -m venv venv
    ```
*  Install the required packages using pip or your preferred package manager:
    ```bash
    pip install -r requirements.txt
    ```
*  Run the script using Python:
    ```bash
    python3 main.py
    ```
*   Follow the prompts in the CLI to enter your queries.
