n = int(input("Enter an odd width (minimum 3): "))

if n < 3 or n % 2 == 0:
    print("Please enter an odd number greater than or equal to 3.")
else:
    middle = n // 2

    for row in range(n):
        if row <= middle:
            outer = middle - row
            inner = 2 * row - 1
        else:
            outer = row - middle
            inner = 2 * (n - row - 1) - 1

        print(" " * outer, end="")

        if inner <= 0:
            print("*")
        else:
            print("*" + " " * inner + "*")