import csv
import os


def clean_csv(file_path):

    if not os.path.exists(file_path):
        print(f"Error: The csv file '{file_path}' does not exist.")
        return

    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            rows = list(reader)

        if not rows:
            print("The csv file is empty.")
            return

        cleaned_rows = []
        for row in rows:
            cleaned_row = [cell.strip() for cell in row if cell.strip()]
            if cleaned_row:
                cleaned_rows.append(cleaned_row)

        print("\nArchivo CSV Limpio:")
        print("-" * 40)
        for cleaned_row in cleaned_rows:
            print(", ".join(cleaned_row))
        print("-" * 40)

    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
