import csv
from hyperon import MeTTa

def convert_csv_to_nested_format(file_path):
    # Read the CSV file
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)

        def convert_row(row, headers):
            result = f"({row[-1]} "                          # start with the Truthvalue value only
            for i, value in enumerate(row[:-1]):
                result += f"({headers[i]} {value})"
            result += ")"                                     # close the Truthvalue expression
            return result

        output = ""
        for row in reader:
            output += "\n" + convert_row(row, headers)

    return output.strip()

def load_to_atomspace(metta, formatted_output):
                                                                    # split the formatted output into lines (MeTTa expressions)
    expressions = formatted_output.split("\n")
    for expr in expressions:
        print(f"Loading: {expr}")                                    # debugging line
                                                                     # add the expression to MeTTa's Atom Space
        metta.run(f"({expr})")                                        # wrap in parentheses for MeTTa

csv_file_path = "truth.csv"  
formatted_output = convert_csv_to_nested_format(csv_file_path)

metta = MeTTa()

load_to_atomspace(metta, formatted_output)


print("Loaded Atoms:")
query_result = metta.run("!(match &self ($tv $rest) ($tv $rest))") 
for result in query_result:
    print(result)
