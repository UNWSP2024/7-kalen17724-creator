# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2) 

import math

def distance(point1, point2):
    """Calculate distance between two 3D points (tuples)."""
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def get_point_input(label):
    """Prompt user for a 3D coordinate and return as a tuple of floats."""
    while True:
        try:
            coords = input(f"Enter the {label} point as x,y,z (e.g., 1,2,3): ")
            x_str, y_str, z_str = coords.split(",")
            x, y, z = float(x_str), float(y_str), float(z_str)
            return (x, y, z)
        except ValueError:
            print("Invalid input. Please enter three numbers separated by commas.")

def main():
    print("3D Distance Calculator")
    point1 = get_point_input("first")
    point2 = get_point_input("second")
    
    dist = distance(point1, point2)
    print(f"\nThe distance between {point1} and {point2} is: {dist:.3f}")

# Run the program
if __name__ == "__main__":
    main()