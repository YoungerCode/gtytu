def square(number_to_square):
    hash_row = "#" * number_to_square
    for i in range(number_to_square):
        print(hash_row)

num_square = int(input("Enter your integer for squares: "))
square(num_square)
