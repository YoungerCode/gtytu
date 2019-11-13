def triangle(num_rows):
    for row_count in range(abs(num_rows) + 1):
        print("#" * row_count)

row_number = int(input("Enter your triangle number: "))
triangle(row_number)
