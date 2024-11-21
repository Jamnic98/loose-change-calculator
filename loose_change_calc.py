# Creating the new `loose_change.py` file with the requested changes
file_path = "/mnt/data/loose_change.py"

import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from base64 import b64decode
from os import remove

# CONSTANTS
ENTRY_BOX_WIDTH = 3
X_POSITION = 650
Y_POSITION = 200
APP_TITLE = "LCC"
TITLE_FONT = "Arial 11 bold"
LABEL_FONT = "Arial 10"
COIN_VALUES = {
    "1p": 0.01,
    "2p": 0.02,
    "5p": 0.05,
    "10p": 0.10,
    "20p": 0.20,
    "50p": 0.50,
    "£1": 1.00,
    "£2": 2.00,
}


class MainApp(tk.Frame):
    def __init__(self, parent):
        """Initialize the main application."""
        super().__init__(parent)
        self.parent = parent
        self.__setup_window()

        # Variables for input and output
        self.input_vars = {key: tk.StringVar() for key in COIN_VALUES}
        self.output_vars = {key: tk.StringVar() for key in COIN_VALUES}
        self.total = tk.StringVar()

        self.error_flag = False

        # UI Setup
        self.__create_widgets()
        self.__layout_widgets()

    def __setup_window(self):
        """Configure the main window."""
        self.parent.title(APP_TITLE)
        self.parent.resizable(width=False, height=False)
        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()
        self.parent.geometry(f"+{int(screen_width/2 - 250)}+{int(screen_height/2 - 250)}")

    def __create_widgets(self):
        """Create and initialize widgets."""
        self.title_label = tk.Label(self.parent, text="LOOSE CHANGE CALCULATOR", font=TITLE_FONT)
        self.labels = {
            "value": tk.Label(self.parent, text="Value", font=LABEL_FONT),
            "quantity": tk.Label(self.parent, text="Quantity", font=LABEL_FONT),
            "total": tk.Label(self.parent, text="Total", font=LABEL_FONT),
        }
        self.entries = {
            key: tk.Entry(self.parent, width=ENTRY_BOX_WIDTH, textvariable=self.input_vars[key])
            for key in COIN_VALUES
        }
        self.outputs = {
            key: tk.Label(self.parent, textvariable=self.output_vars[key]) for key in COIN_VALUES
        }
        self.calculate_button = tk.Button(
            self.parent, text="CALCULATE", font=LABEL_FONT, command=self.calculate_total
        )
        self.total_label = tk.Label(self.parent, textvariable=self.total)

    def __layout_widgets(self):
        """Arrange widgets in the window."""
        self.title_label.grid(row=0, columnspan=5, padx=10, pady=10)

        # Header Labels
        self.labels["value"].grid(row=1, column=0, padx=10, pady=5)
        self.labels["quantity"].grid(row=1, column=2, padx=10, pady=5)
        self.labels["total"].grid(row=1, column=4, padx=10, pady=5)

        # Coin Rows
        for i, (key, value) in enumerate(COIN_VALUES.items(), start=2):
            tk.Label(self.parent, text=key).grid(row=i, column=0, padx=10, pady=5)
            tk.Label(self.parent, text="x").grid(row=i, column=1)
            self.entries[key].grid(row=i, column=2, padx=10, pady=5)
            tk.Label(self.parent, text="=").grid(row=i, column=3)
            self.outputs[key].grid(row=i, column=4, padx=10, pady=5)

        # Total and Calculate Button
        self.calculate_button.grid(row=len(COIN_VALUES) + 2, columnspan=4, pady=20)
        self.total_label.grid(row=len(COIN_VALUES) + 2, column=4)

    def calculate_total(self):
        """Calculate the total value of all entered coins."""
        total = 0
        self.error_flag = False

        for key, value in COIN_VALUES.items():
            input_value = self.input_vars[key].get().strip()
            if not input_value:
                self.input_vars[key].set("0")
                self.output_vars[key].set("£0.00")
                continue

            try:
                quantity = int(input_value)
                coin_total = quantity * value
                total += coin_total
                self.output_vars[key].set(f"£{coin_total:.2f}")
            except ValueError:
                self.error_flag = True
                self.output_vars[key].set("!")

        if self.error_flag:
            self.total.set("Error in input!")
        else:
            self.total.set(f"Total: £{total:.2f}")


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
