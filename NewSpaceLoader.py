import csv
from hyperon import MeTTa

def convert_csv_to_nested_format(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)

        def convert_row(row, headers):
            result = f"({row[-1]} "  
            for i, value in enumerate(row[:-1]):
                result += f" ({headers[i]} {value})"
            result += ")"  
            return result

        return [convert_row(row, headers) for row in reader]

metta = MeTTa()

csv_file_path = "truth.csv"  
formatted_output = convert_csv_to_nested_format(csv_file_path)

metta.run("!(bind! &newspace (new-space))")

for expr in formatted_output:
    print(f"Loading: {expr}")  
    try:
        metta.run(f"!(add-atom &newspace {expr})")
    except Exception as e:
        print(f"Failed to load: {expr}\nError: {e}")

query_result = metta.run("!(match &newspace ($truth $a $b $c $d) $a)")
print("Query Results:", query_result)
