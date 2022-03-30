import math # Need math for calculating square root.
import os # Need access to the operating system to clear the terminal window.

# Clear terminal/cmd before running the program.
os.system('cls||clear') 

# Application name and intro
print("""Area Calculator

Let's do some geometry!""")

# Global variable for keeping total area calculated
area_total = 0

# A function for printing a message about bad user input
# name_side - type/name of number: [side] of a square, [width] of a rectangle, [radius] of a circle etc.
# value - the number in question
# info - [OPTIONAL] additional info about the number. For instance side "(1)" of a triangle
def input_error_text(name_side: str, value: str, info:str = ""):
    print(f"""Your given {name_side}{info} ({value}) is not a positive integer.
Try again.
    """)

# Prompt the user for input, and return it as a 
# name_side - type/name of number: [side] of a square, [width] of a rectangle, [radius] of a circle etc.
# info - [OPTIONAL] additional info about the number. For instance side "(1)" of a triangle
def collect_side_input(name_side:str, info: str = "") -> str:
    return input(f"Input {name_side}{info} as an integer with a value over zero: ")

# A function for handling the input of a chosen number
# Prompts the user for a number, then makes sure the input is correct
# Prints an error message if the input doesn't work or isn't a number that fits
# Prompts the user to try again if the input is bad
# name_side - type/name of number: [side] of a square, [width] of a rectangle, [radius] of a circle etc.
# info - [OPTIONAL] additional info about the number. For instance side "(1)" of a triangle
def handle_side_input(name_side:str, info: str = ""):
    if info != "":
        info = f"[{info}]"
    handle_side_input.side = 0 # giving this a value just to be safe
    successful = False

    while not successful:
        side = collect_side_input(name_side, info)
        try:
            handle_side_input.side = int(side)
            if handle_side_input.side > 0:
                successful = True
            else:
                input_error_text(name_side, side, info)    
        except:
            input_error_text(name_side, side, info)     

# A function to prompt the user to input [width]
def input_width(info: str = "") -> int:
    handle_side_input("width", info)
    return handle_side_input.side

# A function to prompt the user to input [length]
def input_length() -> int:
    handle_side_input("length")
    return handle_side_input.side

# A function to prompt the user to input [height]
def input_height(info: str = "") -> int:
    handle_side_input("height", info)
    return handle_side_input.side

# A function to prompt the user to input the length of a [side] 
def input_side(info: str = "") -> int:
    handle_side_input("side", info)
    return handle_side_input.side

# A function to prompt the user to input the [radius] of a circle
def input_radius() -> int:
    handle_side_input("radius")
    return handle_side_input.side

# A function to calculate the area of a rectangle
# First prompts the user for length and width, then attempts to calculate the area
# Prints an error message if the result isn't a viable rectangle
def calculate_rectangle_area():
    length = input_length()
    width = input_width()
    
    area = calculate_area_four_sided(length, width)
    global area_total # make sure we use the common area_total var, and not a local var

    result = ""

    if area <= 0: # We should never be able to land here, but I've kept it for now
        result = f"A rectangle with length {length} and width {width} is probably not a rectangle, really."
    elif length != width:
        result = f"The area of a rectangle with length {length} and width {width} is {area}."

        # Add calculated area to the total 
        area_total += area
    else:
        # If the result ends up being a square, we'll still calculate the area, but inform the user it's not a rectangle 
        result = f"This is not a rectangle, this is a square with all sides being {length}. The area is {area}, though."

        # Add calculated area to the total 
        area_total += area

    print(f"""{result}
    """)

    # Check if the user wants to calculate the area of another shape
    close_or_continue()

# A function to calculate the area of a square
# First prompts the user for the length of the square's sides
def calculate_square_area():
    side = input_side()
    area = calculate_area_four_sided(side, side)

    print(f"""The area of a square with sides of {side} is {area}.
    """)

    # Add calculated area to the total 
    global area_total
    area_total += area
    
    # Check if the user wants to calculate the area of another shape
    close_or_continue()

# A function to calculate the area of a rhombus
# First prompts the user for the length of the rhombus's height and width
def calculate_rhombus_area():
    height = input_height("p")
    width = input_width("q")
    
    area = calculate_area_four_sided(height, width) / 2
    global area_total # make sure we use the common area_total var, and not a local var

    result = ""

    if area <= 0: # We should never be able to land here, but I've kept it for now
        result = f"A rhombus with height(p) {height} and width(q) {width} is probably not a rhombus."
    elif height != width:
        result = f"The area of a rhombus with height(p) {height} and width(q) {width} is {area}."

        # Add calculated area to the total 
        area_total += area
    else:
        # If the result ends up being a square, we'll still calculate the area, but inform the user it's not a rhombus 
        result = f"This is not a rhombus, this is a square standing on a corner. The area is {area}, though."

        # Add calculated area to the total 
        area_total += area
    
    print(f"""{result}
    """)

    # Check if the user wants to calculate the area of another shape
    close_or_continue()

# A function to calculate the area of a rectangle
# First prompts the user for the lengths of the triangle's sides
# Prints an error message if the result isn't a viable rectangle
def calculate_triangle_area():
    a = input_side("1")
    b = input_side("2")
    c = input_side("3")

    # Heron's formula
    s = float((a + b + c)) / 2.0
    impossible = False
    result = ""

    try:
        area = math.sqrt(s * (s - float(a)) * (s - float(b)) * (s - float(c)))
    except: # catches impossible areas, like the square root of negative numbers and the like
        impossible = True

    if impossible:
        result = f"A triangle with sides of {a}, {b} and {c} is not possible."
    elif area != 0 and not impossible:
        # Add calculated area to the total 
        global area_total
        area_total += area

        result = f"The area of a triangle with sides of {a}, {b} and {c} is {area:.5f}."
    else:   
        result = f"A triangle with sides of {a}, {b} and {c} is probably not so much a triangle, as it is a line."

    print(f"""{result}
    """)

    # Check if the user wants to calculate the area of another shape
    close_or_continue()

# Calculates the area of a circle
# First prompts the user for the radius of a circle, then uses the input to calculate the area
def calculate_circle_area():
    pi = 3.14159265359
    radius = input_radius()
    area = radius**2 * pi

    print(f"""A circle with a radius of {radius} has an area of {area:.5f}.
    """)

    # Add calculated area to the total 
    global area_total     
    area_total += area     
    
    # Check if the user wants to calculate the area of another shape
    close_or_continue()

# Calculates the area of rectangle or square
# length - length of two of the sides of the four-sided shape
# width - length of two of the sides of the four-sided shape
def calculate_area_four_sided(length: int, width: int):
    return length * width

# Checks if the user wants to calculate the area of another shape
# Asks if the user wants to continue, requests a [Y/N] reply
# Also prints the total calculated area thus far
def close_or_continue():
    # Actually accepts any string starting with Y as a yes, and is case-insensitive
    # Anything but the above counts as a N.
    continue_or_quit = input("Do you want to try again? Input Y or N: ").lower().startswith('y')
    
    if continue_or_quit: # Y
        print(f"""
The total area of all the shapes you've calculated thus far is ~{area_total:.2f}.""")

        # Go back to choosing a new shape to calculate the area of
        choose_shape()
    else: # N
        print(f"""
The total area of all the shapes you've calculated is ~{area_total:.2f}.
        """)

        # Exit program
        exit()

# Prompts the user to pick a shape to calculate the area of, then sends the user on to the calculation of said shape
# It's enough to get the first letter right
def choose_shape():
    shape = input("""
Would you like to calculate the area of a [R]ectangle, a R[H]ombus, a [S]quare, a [T]riangle or a [C]ircle? """)
    print()

    if shape.lower().startswith('r'):
        calculate_rectangle_area()
    elif shape.lower().startswith('s'):
        calculate_square_area()
    elif shape.lower().startswith('t'):
        calculate_triangle_area()
    elif shape.lower().startswith('c'):
        calculate_circle_area()
    elif shape.lower().startswith('h'):
        calculate_rhombus_area()
    # Quick secret exit
    elif shape.lower() == "exit" or shape.lower() == "quit" or shape.lower() == "stop":
        exit()
    else:
        print("""Can't help you with that. Please try again!
        """)

        close_or_continue()

# Entry point   
choose_shape()

# We should never get here, but I left it here, in case something goes really wrong
exit()