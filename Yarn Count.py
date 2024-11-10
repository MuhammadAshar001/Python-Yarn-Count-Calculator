import tkinter as tk
from tkinter import ttk

def update_length_visibility(event):
    """Show or hide the length input field based on the selected count system."""
    system = count_system.get()
    if system == "English Count":
        length_label.grid(row=1, column=0, padx=10, pady=5)
        length_entry.grid(row=1, column=1, padx=10, pady=5)
    else:
        length_label.grid_remove()
        length_entry.grid_remove()

def calculate_count():
    try:
        weight = float(weight_entry.get())
        system = count_system.get()

        # Initialize length to None
        length = None

        # Only get the length input if the selected system is "English Count"
        if system == "English Count":
            length = float(length_entry.get())

        if system == "Denier":
            # Use fixed length of 9000 meters
            result = (weight / 9000) * 9000
        elif system == "Tex":
            # Use fixed length of 1000 meters
            result = (weight / 1000) * 1000
        elif system == "English Count":
            # For English Count, use the provided formula with length and weight
            length_in_yards = length * 1.09361
            weight_in_grains = weight * 15.432
            result = 8.33 * (length_in_yards / weight_in_grains)
        else:
            result = "Invalid System Selected"

        result_label.config(text=f"Result: {result:.2f} {system}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Yarn Count Calculator")

# Create input fields
tk.Label(root, text="Weight (in grams):").grid(row=0, column=0, padx=10, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=5)

# Length input field only for English Count
length_label = tk.Label(root, text="Length (in meters):")
length_entry = tk.Entry(root)

# Create dropdown menu for count system
tk.Label(root, text="Select Count System:").grid(row=2, column=0, padx=10, pady=5)
count_system = ttk.Combobox(root, values=["Denier", "Tex", "English Count"])
count_system.grid(row=2, column=1, padx=10, pady=5)
count_system.set("Denier")  # Set default value
count_system.bind("<<ComboboxSelected>>", update_length_visibility)  # Bind event to update visibility

# Create a button to calculate
calculate_button = tk.Button(root, text="Calculate", command=calculate_count)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label to display the result
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
