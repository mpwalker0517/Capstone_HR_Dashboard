import pandas as pd
import tkinter as tk
from tkinter import IntVar

def create_checkboxes_for_names(csv_file_path):
    # Read the names from the CSV 
    try:
        df = pd.read_csv(csv_file_path)
        names = df['Employee Name'].tolist()  
    except FileNotFoundError:
        print(f"File not found: {csv_file_path}")
        return
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return

    # Create a tkinter window
    window = tk.Tk()
    window.title("Names with Checkboxes")

    # Create IntVar list to hold the checkbox states
    checkbox_vars = [IntVar() for _ in names]

    # Create and display checkboxes
    for i, name in enumerate(names):
        checkbox = tk.Checkbutton(window, text=name, variable=checkbox_vars[i])
        checkbox.pack(anchor='w')

    window.mainloop()

# Example usage:
csv_file_path = 'your_file.csv'
create_checkboxes_for_names(csv_file_path)