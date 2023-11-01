import gspread
import tkinter as tk
from tkinter import IntVar

def create_checkboxes_for_google_sheet(sheet_name, creds_file):
    try:
        gc = gspread.service_account(filename=creds_file)  # Load Google Sheets credentials
        sh = gc.open(sheet_name)  # Open the Google Sheet by name

        worksheet = sh.get_worksheet(0)  # Use the first worksheet in the Google Sheet

        # Read the names from the Google Sheet
        names = worksheet.col_values(1)  # Assuming names are in the first column

        # Create a tkinter window
        window = tk.Tk()
        window.title("Names from Google Sheet with Checkboxes")

        # Create IntVar list to hold the checkbox states
        checkbox_vars = [IntVar() for _ in names]

        # Create and display checkboxes
        for i, name in enumerate(names):
            checkbox = tk.Checkbutton(window, text=name, variable=checkbox_vars[i])
            checkbox.pack(anchor='w')

        window.mainloop()

    except FileNotFoundError:
        print(f"File not found: {creds_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
google_sheet_name = 'Your Google Sheet Name'
google_creds_file = 'your-credentials.json'  # Replace with your credentials JSON file

create_checkboxes_for_google_sheet(google_sheet_name, google_creds_file)
