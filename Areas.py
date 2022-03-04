def circle():
    print("You choose circle......")
    radius = float(input("Enter the radius: "))
    print("Area of circle with radius of", radius, "unit is", 3.14 * (radius ** 2), "square units")


def square():
    print("You choose square......")
    side = int(input("Enter the side: "))
    print("Area of the square with side", side, "unit is", side ** 2, "square units")


def rectangle():
    print("You choose rectangle.......")
    length = int(input("Enter the length of rectangle: "))
    bredth = int(input("Enter teh breadth of the rectangle: "))
    print("Area of the rectangle is", length * bredth, "square units")

print("Menu\n"
      "1. Circle\n"
      "2. Square\n"
      "3. Rectangle\n"
)

x = int(input("Which option you want: "))
if x == 1:
    circle()
elif x == 2:
    square()
elif x == 3:
    rectangle()
else:
    print("Invalid Option")        
