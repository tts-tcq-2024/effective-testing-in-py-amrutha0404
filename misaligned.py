class IOutputInterface:
    def print(self, message):
        raise NotImplementedError(message)

class MockOutput(IOutputInterface):
    def __init__(self):
        self.messages = []

    def print(self, message):
        print(message)
        self.messages.append(message)

def print_color_map(output):
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            output.print(f'{i * 5 + j} | {major_colors[i]} | {minor_colors[i]}')
    return len(major_colors) * len(minor_colors)


def test_print_color_map():
    # Create a mock output object to capture printed messages
    mock_output = MockOutput()

    # Run the function and capture the output
    print_color_map(mock_output)

    # Define the expected output based on the 25-pair color code
    expected_output = [
        "0 | White | Blue",
        "1 | White | Orange",
        "2 | White | Green",
        "3 | White | Brown",
        "4 | White | Slate",
        "5 | Red | Blue",
        "6 | Red | Orange",
        "7 | Red | Green",
        "8 | Red | Brown",
        "9 | Red | Slate",
        "10 | Black | Blue",
        "11 | Black | Orange",
        "12 | Black | Green",
        "13 | Black | Brown",
        "14 | Black | Slate",
        "15 | Yellow | Blue",
        "16 | Yellow | Orange",
        "17 | Yellow | Green",
        "18 | Yellow | Brown",
        "19 | Yellow | Slate",
        "20 | Violet | Blue",
        "21 | Violet | Orange",
        "22 | Violet | Green",
        "23 | Violet | Brown",
        "24 | Violet | Slate"
    ]

    # Compare the captured output with the expected output
    for i, expected in enumerate(expected_output):
        assert mock_output.messages[i] == expected, f"Mismatch at line {i}: {mock_output.messages[i]} != {expected}"

    print("All is Well./Maybe")

test_print_color_map()
