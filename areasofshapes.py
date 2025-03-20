#coding starts here
# Area of shapes

# What is the length of a side of the square? 5
# The area of the square is: 25.0
# What is the length of rectangle? 6
# What is the width of the rectangle? 7
# The area of the rectangle is: 42.0
# What is the radius of the circle? 5
# The area of the circle is: 78.5

# Ask the user for the length of a side of a square
side = float(input("What is the length of a side of the square? "))
# Calculate the area of the square
area_square = side * side
# Display the area of the square
print(f"The area of the square is: {area_square}")
print("-----------------------------------------")
# Ask the user for the length and width of a rectangle
length = float(input("What is the length of rectangle? "))
width = float(input("What is the width of the rectangle? "))
# Calculate the area of the rectangle
area_rectangle = length * width
# Display the area of the rectangle
print(f"The area of the rectangle is: {area_rectangle}")
print("-----------------------------------------")
# Ask the user for the radius of a circle
radius = float(input("What is the radius of the circle? "))
# Calculate the area of the circle
area_circle = 3.14 * radius * radius
# Display the area of the circle
print(f"The area of the circle is: {area_circle}")
print("-----------------------------------------")