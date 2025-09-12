def generate_matrix_and_calculate_totals():
    # Get matrix dimensions from the user
    while True:
        try:
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            if rows > 0 and cols > 0:
                break
            else:
                print("Dimensions must be positive numbers. Please try again.")
        except ValueError:
            print("Invalid input. Please enter whole numbers.")

    # Generate the matrix
    matrix = []
    current_number = 1
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(current_number)
            current_number += 1
        matrix.append(row)

    # Calculate totals and store them in lists
    list_of_row_totals = [sum(row) for row in matrix]
    list_of_column_totals = [sum(col) for col in zip(*matrix)]

    # Display the results ---
    if matrix:
        max_num = rows * cols
        width = len(str(max_num))

        for r in matrix:
            formatted_nums = [f"{num:>{width}}" for num in r]
            print(f"  [ {' '.join(formatted_nums)} ]")
    else:
        print("  []") # Handle the case of an empty matrix

    print(f"List of Row Totals:    {list_of_row_totals}")
    print(f"List of Column Totals: {list_of_column_totals}")

    # Handle diagonal totals only for square matrices
    if rows == cols:
        print("Matrix is square, calculating diagonal totals...")
        n = rows
        diagonal = sum(matrix[i][i] for i in range(n))
        print(f"Main Diagonal Total: {diagonal}")
    else:
        print("Diagonal totals are only calculated for square matrices.")


generate_matrix_and_calculate_totals()