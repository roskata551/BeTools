import tkinter as tk
from tkinter import Canvas  # For creating the GUI for mouse-based selection
import pyscreenshot  # For capturing screenshots of a specific region
from PIL import Image, ImageFilter, ImageOps  # To handle and process image files
import pytesseract  # For Optical Character Recognition

# Path to the Tesseract-OCR executable, adjust as necessary for your system
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust path as needed


class TwoBetCalculate:

    def fair_odds(self, bet_data: dict):
        try:
            true_percentage1 = (1 / float(bet_data["pinnacle_odd1"])) * 100
            true_percentage2 = (1 / float(bet_data["pinnacle_odd2"])) * 100

            total_probability = true_percentage1 + true_percentage2

            fair_percentage1 = (true_percentage1 / total_probability) * 100
            fair_percentage2 = (true_percentage2 / total_probability) * 100

            fair_odd1 = 1 / (fair_percentage1 / 100)
            fair_odd2 = 1 / (fair_percentage2 / 100)

        except (ValueError, ZeroDivisionError) as error:
            print(f"Conversion error: {error}")
            fair_odd1 = 0.00
            fair_odd2 = 0.00

        return fair_odd1, fair_odd2

    def ev_percentage(self, bet_data: dict):

        try:
            probability1 = 1 / float(bet_data["fair_odd1"])
            probability2 = 1 / float(bet_data["fair_odd2"])

            ev_percentage1 = (probability1 * (float(bet_data["ev_odd1"]) - 1)) - (1 - probability1)
            ev_percentage2 = (probability2 * (float(bet_data["ev_odd2"]) - 1)) - (1 - probability2)

            ev_percentage1 = ev_percentage1 * 100
            ev_percentage2 = ev_percentage2 * 100

        except (ValueError, ZeroDivisionError) as error:
            print(f"Conversion error: {error}")
            ev_percentage1 = 0.00
            ev_percentage2 = 0.00

        return ev_percentage1, ev_percentage2

    def probability(self, bet_data: dict):

        try:
            probability1 = (1 / bet_data["fair_odd1"]) * 100
            probability2 = (1 / bet_data["fair_odd2"]) * 100

        except (ValueError, ZeroDivisionError) as error:
            print(f"Conversion error: {error}")
            probability1 = 0.00
            probability2 = 0.00

        return probability1, probability2

    def pinnacle_vig(self, bet_data: dict):

        try:
            prob1 = 1 / float(bet_data["pinnacle_odd1"])
            prob2 = 1 / float(bet_data["pinnacle_odd2"])

            vig = ((prob1 + prob2) * 100) - 100

        except (ValueError, ZeroDivisionError) as error:
            print(f"Conversion error: {error}")
            vig = 0.00

        return vig

    def ev_vig(self, bet_data: dict):
        try:
            prob1 = 1 / float(bet_data["ev_odd1"])
            prob2 = 1 / float(bet_data["ev_odd2"])

            vig = ((prob1 + prob2) * 100) - 100

        except (ValueError, ZeroDivisionError) as error:
            print(f"Conversion error: {error}")
            vig = 0.00

        return vig

    def kelly_criterion_odd1(self, bet_data: dict):
        try:
            probability1 = 1 / float(bet_data["fair_odd1"])
            ev_percentage1 = (probability1 * (float(bet_data["ev_odd1"]) - 1)) - (1 - probability1)

            second = float(bet_data["ev_odd1"]) - 1
            bankroll_fraction = ev_percentage1 / second

            bet_size = float(bet_data["bankroll"]) * bankroll_fraction

        except (ValueError, ZeroDivisionError) as error:
            print(f"Conversion error: {error}")
            bet_size = 0.00

        return bet_size

    def kelly_criterion_odd2(self, bet_data: dict):
        try:
            probability2 = 1 / float(bet_data["fair_odd2"])
            ev_percentage2 = (probability2 * (float(bet_data["ev_odd2"]) - 1)) - (1 - probability2)

            second = float(bet_data["ev_odd2"]) - 1
            bankroll_fraction = ev_percentage2 / second
            bet_size = float(bet_data["bankroll"]) * bankroll_fraction

        except (ValueError, ZeroDivisionError) as error:
            print(f"Conversion error: {error}")
            bet_size = 0.00

        return bet_size

    def format_data(self, bet_data: dict):

        float_dictionary = {}
        for key, value in bet_data.items():
            try:
                float_dictionary[key] = float(value)
            except ValueError as error:
                print(f"Conversion error: {error}")
                float_dictionary[key] = 0.00

        rounded_data = {}
        for key, value in float_dictionary.items():
            if key == "pinnacle_odd1" or key == "pinnacle_odd2":
                rounded_data[key] = round(value, 3)
            else:
                rounded_data[key] = round(value, 2)

        string_data = {}
        for key, value in rounded_data.items():
            string_data[key] = str(value)

        return string_data


class ThreeBetCalculate:

    def fair_odds(self, bet_data: dict):
        try:
            true_percentage1 = (1 / float(bet_data["pinnacle_odd1"])) * 100
            true_percentage2 = (1 / float(bet_data["pinnacle_odd2"])) * 100
            true_percentage3 = (1 / float(bet_data["pinnacle_odd3"])) * 100

            total_probability = true_percentage1 + true_percentage2 + true_percentage3

            fair_percentage1 = (true_percentage1 / total_probability) * 100
            fair_percentage2 = (true_percentage2 / total_probability) * 100
            fair_percentage3 = (true_percentage3 / total_probability) * 100

            fair_odd1 = 1 / (fair_percentage1 / 100)
            fair_odd2 = 1 / (fair_percentage2 / 100)
            fair_odd3 = 1 / (fair_percentage3 / 100)

        except (ValueError, ZeroDivisionError) as error:
            print(f"Conversion error: {error}")
            fair_odd1 = 0.00
            fair_odd2 = 0.00
            fair_odd3 = 0.00

        return fair_odd1, fair_odd2, fair_odd3

    def ev_percentage(self, bet_data: dict):

        try:
            probability1 = 1 / float(bet_data["fair_odd1"])
            probability2 = 1 / float(bet_data["fair_odd2"])
            probability3 = 1 / float(bet_data["fair_odd3"])

            ev_percentage1 = (probability1 * (float(bet_data["ev_odd1"]) - 1)) - (1 - probability1)
            ev_percentage2 = (probability2 * (float(bet_data["ev_odd2"]) - 1)) - (1 - probability2)
            ev_percentage3 = (probability3 * (float(bet_data["ev_odd3"]) - 1)) - (1 - probability3)

            ev_percentage1 = ev_percentage1 * 100
            ev_percentage2 = ev_percentage2 * 100
            ev_percentage3 = ev_percentage3 * 100

        except (ValueError, ZeroDivisionError) as error:
            print(f"Conversion error: {error}")
            ev_percentage1 = 0.00
            ev_percentage2 = 0.00
            ev_percentage3 = 0.00

        return ev_percentage1, ev_percentage2, ev_percentage3

    def probability(self, bet_data: dict):

        try:
            probability1 = (1 / bet_data["fair_odd1"]) * 100
            probability2 = (1 / bet_data["fair_odd2"]) * 100
            probability3 = (1 / bet_data["fair_odd3"]) * 100

        except (ValueError, ZeroDivisionError) as error:
            print(f"Conversion error: {error}")
            probability1 = 0.00
            probability2 = 0.00
            probability3 = 0.00

        return probability1, probability2, probability3

    def pinnacle_vig(self, bet_data: dict):

        try:
            prob1 = 1 / float(bet_data["pinnacle_odd1"])
            prob2 = 1 / float(bet_data["pinnacle_odd2"])
            prob3 = 1 / float(bet_data["pinnacle_odd3"])

            vig = ((prob1 + prob2 + prob3) * 100) - 100

        except (ValueError, ZeroDivisionError) as error:
            print(f"Conversion error: {error}")
            vig = 0.00

        return vig

    def ev_vig(self, bet_data: dict):
        try:
            prob1 = 1 / float(bet_data["ev_odd1"])
            prob2 = 1 / float(bet_data["ev_odd2"])
            prob3 = 1 / float(bet_data["ev_odd3"])

            vig = ((prob1 + prob2 + prob3) * 100) - 100

        except (ValueError, ZeroDivisionError) as error:
            print(f"Conversion error: {error}")
            vig = 0.00

        return vig

    def kelly_criterion_odd1(self, bet_data: dict):
        try:
            probability1 = 1 / float(bet_data["fair_odd1"])
            ev_percentage1 = (probability1 * (float(bet_data["ev_odd1"]) - 1)) - (1 - probability1)

            second = float(bet_data["ev_odd1"]) - 1
            bankroll_fraction = ev_percentage1 / second

            bet_size = float(bet_data["bankroll"]) * bankroll_fraction

        except (ValueError, ZeroDivisionError) as error:
            print(f"Conversion error: {error}")
            bet_size = 0.00

        return bet_size

    def kelly_criterion_odd2(self, bet_data: dict):
        try:
            probability2 = 1 / float(bet_data["fair_odd2"])
            ev_percentage2 = (probability2 * (float(bet_data["ev_odd2"]) - 1)) - (1 - probability2)

            second = float(bet_data["ev_odd2"]) - 1
            bankroll_fraction = ev_percentage2 / second
            bet_size = float(bet_data["bankroll"]) * bankroll_fraction

        except (ValueError, ZeroDivisionError) as error:
            print(f"Conversion error: {error}")
            bet_size = 0.00

        return bet_size

    def kelly_criterion_odd3(self, bet_data: dict):
        try:
            probability3 = 1 / float(bet_data["fair_odd3"])
            ev_percentage3 = (probability3 * (float(bet_data["ev_odd3"]) - 1)) - (1 - probability3)

            second = float(bet_data["ev_odd3"]) - 1
            bankroll_fraction = ev_percentage3 / second
            bet_size = float(bet_data["bankroll"]) * bankroll_fraction

        except (ValueError, ZeroDivisionError) as error:
            print(f"Conversion error: {error}")
            bet_size = 0.00

        return bet_size

    def format_data(self, bet_data: dict):

        float_dictionary = {}
        for key, value in bet_data.items():
            try:
                float_dictionary[key] = float(value)
            except ValueError as error:
                print(f"Conversion error: {error}")
                float_dictionary[key] = 0.00

        rounded_data = {}
        for key, value in float_dictionary.items():
            if key == "pinnacle_odd1" or key == "pinnacle_odd2" or key == "pinnacle_odd3":
                rounded_data[key] = round(value, 3)
            else:
                rounded_data[key] = round(value, 2)

        string_data = {}
        for key, value in rounded_data.items():
            string_data[key] = str(value)

        return string_data


class Screen:

    def take_screenshot(self, screenshot_name):
        """Launch a GUI for selecting an area to screenshot."""
        # Create a root window using Tkinter
        root = tk.Tk()

        # Make the window fullscreen and semi-transparent for easy selection
        root.attributes('-fullscreen', True)
        root.attributes('-alpha', 0.3)  # Set transparency to 30%
        root.title("Select Area")  # Title for the window

        # Create a canvas to detect mouse movements and draw the selection rectangle
        canvas = Canvas(root, cursor="cross", bg="gray")
        canvas.pack(fill="both", expand=True)  # Make the canvas fill the entire window

        # Variables to track mouse coordinates and rectangle object
        start_x = start_y = None  # Starting point of the selection
        rect_id = None  # ID of the rectangle being drawn

        # Event handler for mouse button press
        def on_mouse_down(event):
            nonlocal start_x, start_y, rect_id
            start_x, start_y = event.x, event.y  # Record the starting coordinates
            # Create a rectangle at the starting point
            rect_id = canvas.create_rectangle(start_x, start_y, start_x, start_y, outline="red", width=2)

        # Event handler for mouse drag (moving the cursor while holding the button)
        def on_mouse_drag(event):
            nonlocal rect_id
            # Update the rectangle's coordinates as the mouse moves
            canvas.coords(rect_id, start_x, start_y, event.x, event.y)

        # Event handler for mouse button release
        def on_mouse_up(event):
            nonlocal start_x, start_y
            # Calculate the bounding box coordinates of the selected area
            x1, y1 = min(start_x, event.x), min(start_y, event.y)  # Top-left corner
            x2, y2 = max(start_x, event.x), max(start_y, event.y)  # Bottom-right corner

            root.destroy()  # Close the selection GUI

            # Capture the selected screen region using the bounding box
            screenshot = pyscreenshot.grab(bbox=(x1, y1, x2, y2))

            # Save the screenshot to a file
            screenshot.save(f"ScreenShots/{screenshot_name}.png")

        # Bind the mouse events to their respective handlers
        canvas.bind("<ButtonPress-1>", on_mouse_down)  # Left mouse button press
        canvas.bind("<B1-Motion>", on_mouse_drag)  # Mouse drag with left button held
        canvas.bind("<ButtonRelease-1>", on_mouse_up)  # Left mouse button release

        # Start the Tkinter main loop
        root.mainloop()

    def read_image(self, image_name):
        image = Image.open(f"ScreenShots/{image_name}.png")
        image = image.convert("L")  # Convert to grayscale
        image = ImageOps.invert(image)  # Invert colors (if text is blue on white)
        image = image.filter(ImageFilter.SHARPEN)  # Sharpen the image
        image = image.resize((image.width * 3, image.height * 3), Image.Resampling.LANCZOS)  # Resize for better OCR
        # PSM 7 for single-line text; whitelist numbers and period.
        custom_config = r'--psm 6 -c tessedit_char_whitelist=0123456789.'
        text = pytesseract.image_to_string(image, config=custom_config)

        return text





