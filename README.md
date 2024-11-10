Here's a README for your Python Yarn Count System project:

---

# Yarn Count Calculator

A simple Python-based Yarn Count Calculator that computes yarn count in Denier, Tex, and English Count systems. This application uses a Tkinter graphical interface, making it easy for users to enter weight and length (when required) to get the yarn count based on the selected system.

## Features

- Calculates yarn count in three systems: **Denier**, **Tex**, and **English Count**.
- Automatically adjusts the input fields based on the selected system.
- Provides a straightforward interface for easy data entry and result display.

## Installation

To run this application, you'll need:
- Python 3.x installed on your machine.
- `tkinter` library (it comes pre-installed with Python on most platforms).

## Usage

1. Run the script:
    ```bash
    python yarn_count_calculator.py
    ```

2. In the application:
   - **Weight**: Enter the weight of the yarn in grams (or grains for English Count).
   - **Length**: Only required for English Count; enter length in meters.
   - **Select Count System**: Choose Denier, Tex, or English Count from the dropdown.

3. Click the **Calculate** button, and the result will be displayed at the bottom.

## Calculation Details

- **Denier**: Assumes a fixed length of 9000 meters.
- **Tex**: Assumes a fixed length of 1000 meters.
- **English Count**: Uses length (converted to yards) and weight (converted to grains) for calculation.

---

## License

This project is licensed under the MIT License.

