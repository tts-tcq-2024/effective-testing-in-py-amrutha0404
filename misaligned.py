
import io
import sys

def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major_colors[i]} | {minor_colors[i]}')
    return len(major_colors) * len(minor_colors)

def test_print_color_map():
    # Redirect stdout to capture print output
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Call the function to print the color map
    result = print_color_map()
    
    # Restore stdout
    sys.stdout = sys.__stdout__

    # Split the captured output into a list of lines
    actual_output = captured_output.getvalue().strip().split('\n')

    # Create the expected output list
    expected_output = [
        " 0 | White  | Blue   ",
        " 1 | White  | Orange ",
        " 2 | White  | Green  ",
        " 3 | White  | Brown  ",
        " 4 | White  | Slate  ",
        " 5 | Red    | Blue   ",
        " 6 | Red    | Orange ",
        " 7 | Red    | Green  ",
        " 8 | Red    | Brown  ",
        " 9 | Red    | Slate  ",
        "10 | Black  | Blue   ",
        "11 | Black  | Orange ",
        "12 | Black  | Green  ",
        "13 | Black  | Brown  ",
        "14 | Black  | Slate  ",
        "15 | Yellow | Blue   ",
        "16 | Yellow | Orange ",
        "17 | Yellow | Green  ",
        "18 | Yellow | Brown  ",
        "19 | Yellow | Slate  ",
        "20 | Violet | Blue   ",
        "21 | Violet | Orange ",
        "22 | Violet | Green  ",
        "23 | Violet | Brown  ",
        "24 | Violet | Slate  "
    ]

    # Assert that the actual output matches the expected output
    assert actual_output == expected_output, f"Mismatch in output:\nExpected: {expected_output}\nGot: {actual_output}"

    assert(result == 25)
    print("All is well (maybe!)\n")

# Run the test
test_print_color_map()
