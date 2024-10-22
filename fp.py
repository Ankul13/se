def get_weight(level, type):
    # Define weight values for each complexity level and function type
    weights = {
        "Low": {"EI": 4, "EO": 4, "UI": 4, "ILF": 7, "EIF": 5},
        "Average": {"EI": 5, "EO": 5, "UI": 4, "ILF": 10, "EIF": 7},
        "High": {"EI": 6, "EO": 7, "UI": 6, "ILF": 15, "EIF": 10},
    }
    # Return the weight for the specified level and type, or 0 if invalid
    return weights.get(level, {}).get(type, 0)

def main():
    # Input the number of each function type
    ei_count = int(input("Enter number of External Inputs (EI): "))
    eo_count = int(input("Enter number of External Outputs (EO): "))
    ui_count = int(input("Enter number of User Inquiries (UI): "))
    ilf_count = int(input("Enter number of Internal Logical Files (ILF): "))
    eif_count = int(input("Enter number of External Interface Files (EIF): "))

    # Input complexity adjustment factor level
    complexity_level = input("Enter complexity adjustment factor level (Low, Average, High): ").capitalize()

    # Determine scale based on user input
    if complexity_level == "Low":
        scale = 1
    elif complexity_level == "Average":
        scale = 3
    elif complexity_level == "High":
        scale = 5
    else:
        print("Invalid complexity level.")
        return

    # Step 1: Calculate Unadjusted Function Points (UFP)
    UFP = (
        ei_count * get_weight(complexity_level, "EI") +
        eo_count * get_weight(complexity_level, "EO") +
        ui_count * get_weight(complexity_level, "UI") +
        ilf_count * get_weight(complexity_level, "ILF") +
        eif_count * get_weight(complexity_level, "EIF")
    )

    # Step 2: Calculate the Function Point adjustment factor (CAF)
    F = 14 * scale  # Calculate F based on scale
    CAF = 0.65 + (0.01 * F)  # Calculate CAF based on F

    # Step 3: Calculate the final Function Points (FP)
    FP = UFP * CAF

    # Output the results
    print(f"Complexity Adjustment Factor (CAF): {CAF:.2f}")
    print(f"Unadjusted Function Points (UFP): {UFP}")
    print(f"Function Point (FP): {FP:.2f}")

# Ensure the script runs only if it's executed directly
if __name__ == "__main__":
    main()

# output entries
# Enter number of External Inputs (EI): 50
# Enter number of External Outputs (EO): 40
# Enter number of User Inquiries (UI): 35
# Enter number of Internal Logical Files (ILF): 6
# Enter number of External Interface Files (EIF): 4
# Enter complexity adjustment factor level (Low, Average, High): average