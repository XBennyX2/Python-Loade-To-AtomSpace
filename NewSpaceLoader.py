import csv
from hyperon import MeTTa

def load_csv_data_to_newspace(csv_file_path, space_name="newspace"):

    # Create a MeTTa instance
    metta = MeTTa()

    # Bind a new space with the given name
    metta.run(f"!(bind! &{space_name} (new-space))")
    
    # Open and read the CSV file
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        
        # Process each row in the CSV file
        for row in reader:
            # Start with the TruthValue (last column)
            expr = f"({row[-1]} "  
            # Add each header-value pair as a sub-expression
            for i, value in enumerate(row[:-1]):
                expr += f" ({headers[i]} {value})"
            expr += ")"  # Close the expression
            print(f"Loading: {expr}")  # Debug: show the expression being loaded
            try:
                # Load the expression into the new space
                metta.run(f"!(add-atom &{space_name} {expr})")
            except Exception as e:
                print(f"Failed to load: {expr}\nError: {e}")
    
    return metta

#Checking The Function
metta_instance = load_csv_data_to_newspace("truth.csv", "myNewSpace")

result = metta_instance.run("!(match &myNewSpace ($tv $a $b $c $d) ($tv $a $b $c $d))")
print("Query Results:", result)
