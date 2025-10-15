data = []

# Step 1: Collect data using a loop
while True:
    try:
        year = int(input("Enter year (e.g., 2010): "))
        state = input("Enter state name: ")
        population = int(input("Enter population: "))
        
        data.append([year, state, population])
        
        another = input("Do you want to enter another record? (yes/no): ").strip().lower()
        if another != 'yes':
            break
    except ValueError:
        print("Invalid input. Please enter correct data types.")

# Step 2: Ask user for a year to sum populations
try:
    target_year = int(input("Enter the year to calculate total population: "))
    
    total_population = 0
    for record in data:
        if record[0] == target_year:
            total_population += record[2]
    
    print(f"Total population for the year {target_year}: {total_population}")

except ValueError:
    print("Invalid year input.")