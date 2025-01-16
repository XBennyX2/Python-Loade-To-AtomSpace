import csv
from hyperon import MeTTa

def convert_csv_to_nested_format(file_path):
    # Read the CSV file
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)

        def convert_row(row, headers):
            result = f"({row[-1]} "  # Start with the Truthvalue value only
            for i, value in enumerate(row[:-1]):
                result += f" ({headers[i]}  {value})"
            result += ")"  # Close the Truthvalue expression
            return result

        output = ""
        for row in reader:
            output += "\n" + convert_row(row, headers)

    return output.strip()

metta = MeTTa()

csv_file_path = "truth.csv"  # Replace with your CSV file path
formatted_output = convert_csv_to_nested_format(csv_file_path)
print(formatted_output)

mea = formatted_output
metta.run(mea)
X = metta.run(''' !(match &self (True $x $y $z $r) $z)''')
print("Result",X)