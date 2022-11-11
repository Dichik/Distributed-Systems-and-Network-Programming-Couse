print("Enter the parameters for n x m rectangle:")
n = int(input("Please enter n: "))
m = int(input("Please enter m: "))

def get_square_representation(side):
    return f"{side}x{side}"

min_square = min(n, m)
print(f"The square with minimum side is {get_square_representation(min_square)}")
print(f"But the square with minimum even side is {get_square_representation(min_square - min_square % 2)}")