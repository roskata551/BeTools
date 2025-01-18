from modules import ThreeBetCalculate, Screen
import keyboard  # For listening to global hotkeys
import tkinter as tk
import threading

class ThreeSelections:

    def __init__(self):
        # Initialize key variables
        self.calculate = ThreeBetCalculate()
        self.screen = Screen()

        self.bet_data = {"fair_odd1": 0.00,
                         "fair_odd2": 0.00,
                         "fair_odd3": 0.00,
                         "pinnacle_odd1": 0.000,
                         "pinnacle_odd2": 0.000,
                         "pinnacle_odd3": 0.000,
                         "pinnacle_vig": 0.00,
                         "probability1": 0.00,
                         "probability2": 0.00,
                         "probability3": 0.00,
                         "ev_odd1": 0.00,
                         "ev_odd2": 0.00,
                         "ev_odd3": 0.00,
                         "ev_percentage1": 0.00,
                         "ev_percentage2": 0.00,
                         "ev_percentage3": 0.00,
                         "ev_vig": 0.00,
                         "bet_size": 0.00,
                         "bankroll": 0.00
                         }  # Dictionary for all the variables

        self.root = tk.Tk()  # Main GUI window
        self.labels = {}  # Dictionary for all the labels

        self.main()  # Launch main application logic

    def set_text_labels(self):

        """First Column with static information"""
        probability_text_label = tk.Label(
            self.root,
            text="Probability:",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=10
        )
        probability_text_label.grid(row=1, column=1, padx=5, pady=10)  # Place label in grid with padding

        pinnacle_odds_text_label = tk.Label(
            self.root,
            text="Pinnacle Odds:",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=12
        )
        pinnacle_odds_text_label.grid(row=2, column=1, padx=5, pady=10)  # Place label in grid with padding

        fair_odds_text_label = tk.Label(
            self.root,
            text="Fair Odds:",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=10
        )
        fair_odds_text_label.grid(row=3, column=1, padx=5, pady=10)  # Place label in grid with padding

        ev_odds_text_label = tk.Label(
            self.root,
            text="EV Odds:",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=10
        )
        ev_odds_text_label.grid(row=4, column=1, padx=5, pady=10)  # Place label in grid with padding

        ev_percentage_text_label = tk.Label(
            self.root,
            text="EV Percentage:",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=12
        )
        ev_percentage_text_label.grid(row=5, column=1, padx=5, pady=10)  # Place label in grid with padding

        """Second Column with static information"""
        pinnacle_vig_label = tk.Label(
            self.root,
            text="Pinnacle VIG:",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=10
        )
        pinnacle_vig_label.grid(row=1, column=5, padx=5, pady=10)  # Place label in grid with padding

        ev_vig_label = tk.Label(
            self.root,
            text="EV VIG:",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=10
        )
        ev_vig_label.grid(row=2, column=5, padx=5, pady=10)  # Place label in grid with padding

        bankroll_text_label = tk.Label(
            self.root,
            text="Bankroll:",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=10
        )
        bankroll_text_label.grid(row=3, column=5, padx=5, pady=10)  # Place label in grid with padding

        bet_size_text_label = tk.Label(
            self.root,
            text="Bet Size:",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=10
        )
        bet_size_text_label.grid(row=4, column=5, padx=5, pady=10)  # Place label in grid with padding

        calculate_text_label = tk.Label(
            self.root,
            text="Calculate:",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=10
        )
        calculate_text_label.grid(row=5, column=5, padx=5, pady=10)  # Place label in grid with padding

        """Static information for the additional instructions"""
        empty_label = tk.Label(
            self.root,
            text="",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=8
        )
        empty_label.grid(row=6, column=1, columnspan=3, padx=0, pady=0)  # Place label in grid with padding

        alt1_label = tk.Label(
            self.root,
            text="Alt+1 to update the Pinnacle and Fair Odds",  # Text for the extra row
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Helvetica", 10)
        )
        alt1_label.grid(row=7, column=1, columnspan=3, padx=10, pady=0, sticky="w")  # Span across all columns

        alt2_label = tk.Label(
            self.root,
            text="Alt+2 to update the EV Odds and EV Percentages",  # Text for the extra row
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Helvetica", 10)
        )
        alt2_label.grid(row=8, column=1, columnspan=3, padx=10, pady=5, sticky="w")  # Span across all columns

    def set_data_labels(self):

        """First Column with active data"""
        self.labels["probability1"] = tk.Label(
            self.root,
            text="0.00%",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=8
        )
        self.labels["probability1"].grid(row=1, column=2, padx=5, pady=10)  # Place label in grid with padding

        self.labels["probability2"] = tk.Label(
            self.root,
            text="0.00%",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=8
        )
        self.labels["probability2"].grid(row=1, column=3, padx=5, pady=10)  # Place label in grid with padding

        self.labels["probability3"] = tk.Label(
            self.root,
            text="0.00%",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=8
        )
        self.labels["probability3"].grid(row=1, column=4, padx=5, pady=10)  # Place label in grid with padding

        self.labels["pinnacle_odd1"] = tk.Label(
            self.root,
            text="0.000",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=8
        )
        self.labels["pinnacle_odd1"].grid(row=2, column=2, padx=5, pady=10)  # Place label in grid with padding

        self.labels["pinnacle_odd2"] = tk.Label(
            self.root,
            text="0.000",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=8
        )
        self.labels["pinnacle_odd2"].grid(row=2, column=3, padx=5, pady=10)  # Place label in grid with padding

        self.labels["pinnacle_odd3"] = tk.Label(
            self.root,
            text="0.000",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=8
        )
        self.labels["pinnacle_odd3"].grid(row=2, column=4, padx=5, pady=10)  # Place label in grid with padding

        self.labels["fair_odd1"] = tk.Label(
            self.root,
            text="0.00",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=8
        )
        self.labels["fair_odd1"].grid(row=3, column=2, padx=5, pady=10)  # Place label in grid with padding

        self.labels["fair_odd2"] = tk.Label(
            self.root,
            text="0.00",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=8
        )
        self.labels["fair_odd2"].grid(row=3, column=3, padx=5, pady=10)  # Place label in grid with padding

        self.labels["fair_odd3"] = tk.Label(
            self.root,
            text="0.00",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=8
        )
        self.labels["fair_odd3"].grid(row=3, column=4, padx=5, pady=10)  # Place label in grid with padding

        self.labels["ev_odd1"] = tk.Label(
            self.root,
            text="0.00",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=8
        )
        self.labels["ev_odd1"].grid(row=4, column=2, padx=5, pady=10)  # Place label in grid with padding

        self.labels["ev_odd2"] = tk.Label(
            self.root,
            text="0.00",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=8
        )
        self.labels["ev_odd2"].grid(row=4, column=3, padx=5, pady=10)  # Place label in grid with padding

        self.labels["ev_odd3"] = tk.Label(
            self.root,
            text="0.00",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=8
        )
        self.labels["ev_odd3"].grid(row=4, column=4, padx=5, pady=10)  # Place label in grid with padding

        self.labels["ev_percentage1"] = tk.Label(
            self.root,
            text="0.00%",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=8
        )
        self.labels["ev_percentage1"].grid(row=5, column=2, padx=5, pady=10)  # Place label in grid with padding

        self.labels["ev_percentage2"] = tk.Label(
            self.root,
            text="0.00%",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=8
        )
        self.labels["ev_percentage2"].grid(row=5, column=3, padx=5, pady=10)  # Place label in grid with padding80

        self.labels["ev_percentage3"] = tk.Label(
            self.root,
            text="0.00%",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=8
        )
        self.labels["ev_percentage3"].grid(row=5, column=4, padx=5, pady=10)  # Place label in grid with padding80

        """Second Column with active data"""
        self.labels["pinnacle_vig"] = tk.Label(
            self.root,
            text="0.00%",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=8
        )
        self.labels["pinnacle_vig"].grid(row=1, column=6, padx=5, pady=10)  # Place label in grid with padding

        self.labels["ev_vig"] = tk.Label(
            self.root,
            text="0.00%",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=8
        )
        self.labels["ev_vig"].grid(row=2, column=6, padx=5, pady=10)  # Place label in grid with padding

        self.labels["bet_size"] = tk.Label(
            self.root,
            text="0.00$",  # Set text
            bg="#595959",  # Background color
            fg="#29c914",  # Text color
            font=("Typeface", 16),  # Font and size
            width=8
        )
        self.labels["bet_size"].grid(row=4, column=6, padx=5, pady=10)  # Place label in grid with padding

    def set_active_elements(self):
        self.labels["bankroll_text_box"] = tk.Text(self.root, height=1, width=8, font=("Typeface", 13))
        self.labels["bankroll_text_box"].grid(row=3, column=6, padx=5, pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.grid(row=5, column=6, padx=10, pady=10)

        calculate_odd1_button = tk.Button(button_frame,
                                          text="Odd1",
                                          command=self.calculate_odd1,
                                          width=5,  # Width in character units
                                          height=1,
                                          bg="#616161",  # Background color
                                          fg="#29c914",  # Text color
                                          font=("Typeface", 12),
                                          )
        calculate_odd1_button.grid(row=0, column=0)

        calculate_odd2_button = tk.Button(button_frame,
                                          text="Odd2",
                                          command=self.calculate_odd2,
                                          width=5,  # Width in character units
                                          height=1,
                                          bg="#616161",  # Background color
                                          fg="#29c914",  # Text color
                                          font=("Typeface", 12),
                                          )
        calculate_odd2_button.grid(row=0, column=1)

        calculate_odd3_button = tk.Button(button_frame,
                                          text="Odd3",
                                          command=self.calculate_odd3,
                                          width=5,  # Width in character units
                                          height=1,
                                          bg="#616161",  # Background color
                                          fg="#29c914",  # Text color
                                          font=("Typeface", 12),
                                          )
        calculate_odd3_button.grid(row=0, column=3)

    def calculate_odd1(self):
        self.bet_data["bet_size"] = self.calculate.kelly_criterion_odd1(self.bet_data)
        self.bet_data["bankroll"] = self.labels["bankroll_text_box"].get("1.0", tk.END)

        formatted_bet_data = self.calculate.format_data(self.bet_data)
        self.labels["bet_size"].config(text=formatted_bet_data["bet_size"] + "$")

    def calculate_odd2(self):
        self.bet_data["bet_size"] = self.calculate.kelly_criterion_odd2(self.bet_data)
        self.bet_data["bankroll"] = self.labels["bankroll_text_box"].get("1.0", tk.END)

        formatted_bet_data = self.calculate.format_data(self.bet_data)
        self.labels["bet_size"].config(text=formatted_bet_data["bet_size"] + "$")

    def calculate_odd3(self):
        self.bet_data["bet_size"] = self.calculate.kelly_criterion_odd3(self.bet_data)
        self.bet_data["bankroll"] = self.labels["bankroll_text_box"].get("1.0", tk.END)

        formatted_bet_data = self.calculate.format_data(self.bet_data)
        self.labels["bet_size"].config(text=formatted_bet_data["bet_size"] + "$")

    def alt1_update(self):
        formatted_bet_data = self.calculate.format_data(self.bet_data)

        self.labels["pinnacle_odd1"].config(text=formatted_bet_data["pinnacle_odd1"])
        self.labels["pinnacle_odd2"].config(text=formatted_bet_data["pinnacle_odd2"])
        self.labels["pinnacle_odd3"].config(text=formatted_bet_data["pinnacle_odd3"])
        self.labels["fair_odd1"].config(text=formatted_bet_data["fair_odd1"])
        self.labels["fair_odd2"].config(text=formatted_bet_data["fair_odd2"])
        self.labels["fair_odd3"].config(text=formatted_bet_data["fair_odd3"])
        self.labels["pinnacle_vig"].config(text=formatted_bet_data["pinnacle_vig"] + "%")
        self.labels["probability1"].config(text=formatted_bet_data["probability1"] + "%")
        self.labels["probability2"].config(text=formatted_bet_data["probability2"] + "%")
        self.labels["probability3"].config(text=formatted_bet_data["probability3"] + "%")

        self.labels["ev_odd1"].config(text="0.00")
        self.labels["ev_odd2"].config(text="0.00")
        self.labels["ev_odd3"].config(text="0.00")
        self.labels["ev_percentage1"].config(text="0.00")
        self.labels["ev_percentage2"].config(text="0.00")
        self.labels["ev_percentage3"].config(text="0.00")

    def alt2_update(self):
        formatted_bet_data = self.calculate.format_data(self.bet_data)

        self.labels["ev_odd1"].config(text=formatted_bet_data["ev_odd1"])
        self.labels["ev_odd2"].config(text=formatted_bet_data["ev_odd2"])
        self.labels["ev_odd3"].config(text=formatted_bet_data["ev_odd3"])
        self.labels["ev_percentage1"].config(text=formatted_bet_data["ev_percentage1"] + "%")
        self.labels["ev_percentage2"].config(text=formatted_bet_data["ev_percentage2"] + "%")
        self.labels["ev_percentage3"].config(text=formatted_bet_data["ev_percentage3"] + "%")
        self.labels["ev_vig"].config(text=formatted_bet_data["ev_vig"] + "%")

    def start_gui(self):

        # Create the main application window
        self.root.title("Two Bets Tesseract")
        self.root.configure(bg="#595959")  # Set the background color of the main window

        self.set_text_labels()
        self.set_data_labels()
        self.set_active_elements()

        self.root.mainloop()

    def hot_keys(self):
        # Bind the hotkey (Alt+1) to get the True Odds
        keyboard.add_hotkey("alt+1", self.alt1_function)

        keyboard.add_hotkey("alt+2", self.alt2_function)

        # Wait indefinitely for the hotkey or an exit command (ESC)
        keyboard.wait("esc")  # Exits the program when ESC is pressed

    def alt1_function(self):
        """Updates the fair odds and the pinnacle odds"""
        self.screen.take_screenshot("TrueShot1")
        self.screen.take_screenshot("TrueShot2")
        self.screen.take_screenshot("TrueShot3")

        self.bet_data["pinnacle_odd1"] = self.screen.read_image("TrueShot1")
        self.bet_data["pinnacle_odd2"] = self.screen.read_image("TrueShot2")
        self.bet_data["pinnacle_odd3"] = self.screen.read_image("TrueShot3")

        self.bet_data["fair_odd1"], self.bet_data["fair_odd2"], self.bet_data["fair_odd3"] =\
            self.calculate.fair_odds(self.bet_data)

        self.bet_data["pinnacle_vig"] = self.calculate.pinnacle_vig(self.bet_data)

        self.bet_data["probability1"], self.bet_data["probability2"], self.bet_data["probability3"] =\
            self.calculate.probability(self.bet_data)

        self.alt1_update()

    def alt2_function(self):
        """Updates the ev odds, ev vig and ev percentage"""
        self.screen.take_screenshot("EVShot1")
        self.screen.take_screenshot("EVShot2")
        self.screen.take_screenshot("EVShot3")

        self.bet_data["ev_odd1"] = self.screen.read_image("EVShot1")
        self.bet_data["ev_odd2"] = self.screen.read_image("EVShot2")
        self.bet_data["ev_odd3"] = self.screen.read_image("EVShot3")

        self.bet_data["ev_percentage1"], self.bet_data["ev_percentage2"], self.bet_data["ev_percentage3"] =\
            self.calculate.ev_percentage(self.bet_data)
        self.bet_data["ev_vig"] = self.calculate.ev_vig(self.bet_data)

        self.alt2_update()

    def main(self):
        threading.Thread(target=self.hot_keys).start()

        self.start_gui()


if __name__ == "__main__":
    # Create an instance of the class
    my_instance = ThreeSelections()
