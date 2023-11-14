#Count rows from CSV
import csv

csv_file_path = (r"C:\Users\mwalker\Desktop\CS_HR_DASH\Capstone_HR_Dashboard\All Certs_Clean.csv")

def count_csv_rows(file_path):
    try:
        with open(file_path, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            # Use the len function to count the number of rows in the CSV
            row_count = len(list(reader))
            return row_count
    except FileNotFoundError:
        return -1  # File not found error
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return -1  # Other errors


row_count = count_csv_rows(csv_file_path)


#Create fake names
from faker import Faker
fake = Faker()


for i in range(0, row_count):
    New_Data = print(fake.name())


#Update names with fake names
input_csv_file = (r"C:\Users\mwalker\Desktop\CS_HR_DASH\Capstone_HR_Dashboard\All Certs_Clean.csv")
output_csv_file = (r"C:\Users\mwalker\Desktop\CS_HR_DASH\Capstone_HR_Dashboard\All Certs_New Names.csv")
replacement_data = New_Data


def update_first_column(input_file, output_file, replacement_data):
  try:
      with open(input_file, 'r', newline='') as csv_input:
          with open(output_file, 'w', newline='') as csv_output:
              reader = csv.reader(csv_input)
              writer = csv.writer(csv_output)
              for row in reader:
                  if row:  # Check if the row is not empty
                      # Replace the data in the first column
                      row[0] = replacement_data
                  writer.writerow(row)
      print(f"Data in the first column of '{input_file}' updated and saved to '{output_file}'.")
  except FileNotFoundError:
      print(f"File not found: '{input_file}'")
  except Exception as e:
      print(f"An error occurred: {str(e)}")

# Final:
update_first_column(input_csv_file, output_csv_file, replacement_data)