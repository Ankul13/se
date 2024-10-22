import math

# Constants for different project types
ORGANIC_A = 2.4
ORGANIC_B = 1.05
SEMIDETACHED_A = 3.0
SEMIDETACHED_B = 1.12
EMBEDDED_A = 3.6
EMBEDDED_B = 1.20

# Constants for time calculation
TIME_C = 2.5
ORGANIC_D = 0.38
SEMIDETACHED_D = 0.35
EMBEDDED_D = 0.32

def cocomo_calculation(kloc, project_type):
    # Initialize parameters for the calculation
    a, b, d = 0, 0, 0
    
    # Determine constants based on project type
    if project_type == 'O':  # Organic
        a = ORGANIC_A
        b = ORGANIC_B
        d = ORGANIC_D
    elif project_type == 'S':  # Semi-Detached
        a = SEMIDETACHED_A
        b = SEMIDETACHED_B
        d = SEMIDETACHED_D
    elif project_type == 'E':  # Embedded
        a = EMBEDDED_A
        b = EMBEDDED_B
        d = EMBEDDED_D
    else:
        print("Invalid project type selected.")
        return  # Exit if the project type is invalid
    
    # Calculate effort using the COCOMO formula
    effort = a * (kloc ** b)  # Effort in person-months
    
    # Calculate development time based on the effort
    time = TIME_C * (effort ** d)  # Development time in months
    
    # Output the results
    print("\nCOCOMO Model Estimation for Project:")
    print(f"Effort: {effort:.2f} Person-Months")
    print(f"Development Time: {time:.2f} Months")

def main():
    # Input for project size
    kloc = float(input("Enter the size of the project in KLOC (thousands of lines of code): "))
    
    # Input for project type
    print("Select the project type:")
    print("O - Organic")
    print("S - Semi-Detached")
    print("E - Embedded")
    project_type = input("Enter your choice (O/S/E): ").strip().upper()  # Normalize input
    
    # Call the COCOMO calculation function
    cocomo_calculation(kloc, project_type)

# Ensure the script runs only if it's executed directly
if __name__ == "__main__":
    main()
