import tkinter as tk
from base64 import b64decode
from os import remove

# CONSTANTS
ENTRY_BOX_WIDTH = 3
X_POSITION = 650
Y_POSITION = 200
APP_TITLE = ""
TITLE_FONT = "Arial 11 bold"
LABEL_FONT = "Arial 10"


class MainApp(tk.Frame):
    def __init__(self, parent):

        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.icon = \
            ("AAABAAEAEBAQAAEABAAoAQAAFgAAACgAAAAQAAAAIAAAAAEABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKf/\n"
             "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAREQA\n"
             "AAAAAEREREQAAAAEREREREAAAERAAAAERAAAREQEREREAARERARERERABERAAAREREAEREQEREREQARERARERERAAEREBEQ\n"
             "ERAAAREQAQAREAAAEREAAREAAAABEREREAAAAAABERAAAAAAAAAAAAAAD8PwAA8A8AAOAHAADAAwAAgAEAAIABAAAAAAAAA\n"
             "AAAAAAAAAAAAAAAgAEAAIABAADAAwAA4AcAAPAPAAD8PwAA\n"
             "")

        icon_data = b64decode(self.icon)
        self.tempFile = "icon.ico"
        icon_file = open(self.tempFile, "wb")
        icon_file.write(icon_data)
        icon_file.close()
        my_window.wm_iconbitmap(default=self.tempFile)
        remove(self.tempFile)

        my_window.resizable(width=False, height=False)
        screen_width = my_window.winfo_screenwidth()
        screen_height = my_window.winfo_screenheight()
        my_window.geometry("+%d+%d" % (screen_width / 2 - 250, screen_height / 2 - 250))
        my_window.title(APP_TITLE)
        self.error_flag = False

        self.one_pence_input_var = tk.StringVar()
        self.two_pence_input_var = tk.StringVar()
        self.five_pence_input_var = tk.StringVar()
        self.ten_pence_input_var = tk.StringVar()
        self.twenty_pence_input_var = tk.StringVar()
        self.fifty_pence_input_var = tk.StringVar()
        self.one_pound_input_var = tk.StringVar()
        self.two_pound_input_var = tk.StringVar()

        self.one_pence_output_var = tk.StringVar()
        self.two_pence_output_var = tk.StringVar()
        self.five_pence_output_var = tk.StringVar()
        self.ten_pence_output_var = tk.StringVar()
        self.twenty_pence_output_var = tk.StringVar()
        self.fifty_pence_output_var = tk.StringVar()
        self.one_pound_output_var = tk.StringVar()
        self.two_pound_output_var = tk.StringVar()

        self.tot_1p = 0
        self.tot_2p = 0
        self.tot_5p = 0
        self.tot_10p = 0
        self.tot_20p = 0
        self.tot_50p = 0
        self.tot_1pound = 0
        self.tot_2pound = 0

        self.total = tk.StringVar()
        self.total_array = []

        # LABELS
        self.title = tk.Label(my_window, text="LOOSE CHANGE CALCULATOR", font=TITLE_FONT)

        self.label_1 = tk.Label(my_window, text="Value", font=LABEL_FONT)
        self.label_2 = tk.Label(my_window, text="Quantity", font=LABEL_FONT)
        self.label_3 = tk.Label(my_window, text="Total", font=LABEL_FONT)

        self.one_pence_label = tk.Label(my_window, text="1p")
        self.two_pence_label = tk.Label(my_window, text="2p")
        self.five_pence_label = tk.Label(my_window, text="5p")
        self.ten_pence_label = tk.Label(my_window, text="10p")
        self.twenty_pence_label = tk.Label(my_window, text="20p")
        self.fifty_pence_label = tk.Label(my_window, text="50p")
        self.one_pound_label = tk.Label(my_window, text="£1")
        self.two_pound_label = tk.Label(my_window, text="£2")

        self.one_pence_times_sign = tk.Label(my_window, text="x")
        self.two_pence_times_sign = tk.Label(my_window, text="x")
        self.five_pence_times_sign = tk.Label(my_window, text="x")
        self.ten_pence_times_sign = tk.Label(my_window, text="x")
        self.twenty_pence_times_sign = tk.Label(my_window, text="x")
        self.fifty_pence_times_sign = tk.Label(my_window, text="x")
        self.one_pound_times_sign = tk.Label(my_window, text="x")
        self.two_pound_times_sign = tk.Label(my_window, text="x")

        self.one_pence_equals_sign = tk.Label(my_window, text="=")
        self.two_pence_equals_sign = tk.Label(my_window, text="=")
        self.five_pence_equals_sign = tk.Label(my_window, text="=")
        self.ten_pence_equals_sign = tk.Label(my_window, text="=")
        self.twenty_pence_equals_sign = tk.Label(my_window, text="=")
        self.fifty_pence_equals_sign = tk.Label(my_window, text="=")
        self.one_pound_equals_sign = tk.Label(my_window, text="=")
        self.two_pound_equals_sign = tk.Label(my_window, text="=")

        self.one_pence_output = tk.Label(my_window, textvariable=self.one_pence_output_var)
        self.two_pence_output = tk.Label(my_window, textvariable=self.two_pence_output_var)
        self.five_pence_output = tk.Label(my_window, textvariable=self.five_pence_output_var)
        self.ten_pence_output = tk.Label(my_window, textvariable=self.ten_pence_output_var)
        self.twenty_pence_output = tk.Label(my_window, textvariable=self.twenty_pence_output_var)
        self.fifty_pence_output = tk.Label(my_window, textvariable=self.fifty_pence_output_var)
        self.one_pound_output = tk.Label(my_window, textvariable=self.one_pound_output_var)
        self.two_pound_output = tk.Label(my_window, textvariable=self.two_pound_output_var)

        self.output_label = tk.Label(my_window, textvariable=self.total)

        # ENTRIES
        self.one_pence_entry = tk.Entry(my_window, width=ENTRY_BOX_WIDTH, textvariable=self.one_pence_input_var)
        self.two_pence_entry = tk.Entry(my_window, width=ENTRY_BOX_WIDTH, textvariable=self.two_pence_input_var)
        self.five_pence_entry = tk.Entry(my_window, width=ENTRY_BOX_WIDTH, textvariable=self.five_pence_input_var)
        self.ten_pence_entry = tk.Entry(my_window, width=ENTRY_BOX_WIDTH, textvariable=self.ten_pence_input_var)
        self.twenty_pence_entry = tk.Entry(my_window, width=ENTRY_BOX_WIDTH, textvariable=self.twenty_pence_input_var)
        self.fifty_pence_entry = tk.Entry(my_window, width=ENTRY_BOX_WIDTH, textvariable=self.fifty_pence_input_var)
        self.one_pound_entry = tk.Entry(my_window, width=ENTRY_BOX_WIDTH, textvariable=self.one_pound_input_var)
        self.two_pound_entry = tk.Entry(my_window, width=ENTRY_BOX_WIDTH, textvariable=self.two_pound_input_var)

        # BUTTONS
        self.calculate_button = tk.Button(my_window,
                                          text="CALCULATE",
                                          font="Arial 10 bold",
                                          command=self.calculate_total)

        # PACKING
        self.title.grid(row=0, columnspan=5, padx=10, pady=10)

        self.label_1.grid(row=1, column=0, padx=10, pady=5)
        self.label_2.grid(row=1, column=2, padx=10, pady=5)
        self.label_3.grid(row=1, column=4, padx=10, pady=5)

        self.one_pence_label.grid(row=2, column=0, padx=10, pady=5)
        self.two_pence_label.grid(row=3, column=0, padx=10, pady=5)
        self.five_pence_label.grid(row=4, column=0, padx=10, pady=5)
        self.ten_pence_label.grid(row=5, column=0, padx=10, pady=5)
        self.twenty_pence_label.grid(row=6, column=0, padx=10, pady=5)
        self.fifty_pence_label.grid(row=7, column=0, padx=10, pady=5)
        self.one_pound_label.grid(row=8, column=0, padx=10, pady=5)
        self.two_pound_label.grid(row=9, column=0, padx=10, pady=5)

        self.one_pence_times_sign.grid(row=2, column=1)
        self.two_pence_times_sign.grid(row=3, column=1)
        self.five_pence_times_sign.grid(row=4, column=1)
        self.ten_pence_times_sign.grid(row=5, column=1)
        self.twenty_pence_times_sign.grid(row=6, column=1)
        self.fifty_pence_times_sign.grid(row=7, column=1)
        self.one_pound_times_sign.grid(row=8, column=1)
        self.two_pound_times_sign.grid(row=9, column=1)

        self.one_pence_entry.grid(row=2, column=2, padx=10, pady=5)
        self.two_pence_entry.grid(row=3, column=2, padx=10, pady=5)
        self.five_pence_entry.grid(row=4, column=2, padx=10, pady=5)
        self.ten_pence_entry.grid(row=5, column=2, padx=10, pady=5)
        self.twenty_pence_entry.grid(row=6, column=2, padx=10, pady=5)
        self.fifty_pence_entry.grid(row=7, column=2, padx=10, pady=5)
        self.one_pound_entry.grid(row=8, column=2, padx=10, pady=5)
        self.two_pound_entry.grid(row=9, column=2, padx=10, pady=5)

        self.one_pence_equals_sign.grid(row=2, column=3)
        self.two_pence_equals_sign.grid(row=3, column=3)
        self.five_pence_equals_sign.grid(row=4, column=3)
        self.ten_pence_equals_sign.grid(row=5, column=3)
        self.twenty_pence_equals_sign.grid(row=6, column=3)
        self.fifty_pence_equals_sign.grid(row=7, column=3)
        self.one_pound_equals_sign.grid(row=8, column=3)
        self.two_pound_equals_sign.grid(row=9, column=3)

        self.one_pence_output.grid(row=2, column=4)
        self.two_pence_output.grid(row=3, column=4)
        self.five_pence_output.grid(row=4, column=4)
        self.ten_pence_output.grid(row=5, column=4)
        self.twenty_pence_output.grid(row=6, column=4)
        self.fifty_pence_output.grid(row=7, column=4)
        self.one_pound_output.grid(row=8, column=4)
        self.two_pound_output.grid(row=9, column=4)

        self.calculate_button.grid(row=10, columnspan=4, pady=20)
        self.output_label.grid(row=10, column=4)

        self.one_pence_entry.focus()

    def calculate_total(self):
        """Method to take all entries from the value column, multiply by their nominal values and sum"""
        self.total_array.clear()
        self.error_flag = False

        # Remove all spaces
        one_pence = self.one_pence_input_var.get().strip()
        two_pence = self.two_pence_input_var.get().strip()
        five_pence = self.five_pence_input_var.get().strip()
        ten_pence = self.ten_pence_input_var.get().strip()
        twenty_pence = self.twenty_pence_input_var.get().strip()
        fifty_pence = self.fifty_pence_input_var.get().strip()
        one_pound = self.one_pound_input_var.get().strip()
        two_pound = self.two_pound_input_var.get().strip()

        if len(one_pence) == 0:
            self.one_pence_input_var.set("0")
            self.one_pence_output_var.set("£0.00")
        else:
            try:
                number_of_1p = int(one_pence)
                self.tot_1p = f'{(number_of_1p * 0.01):.2f}'
                self.one_pence_output_var.set("£" + self.tot_1p)
                self.tot_1p = float(self.tot_1p)
                self.total_array.append(self.tot_1p)

            except ValueError:
                self.error_flag = True
                self.one_pence_output_var.set("!")

        if len(two_pence) == 0:
            self.two_pence_input_var.set("0")
            self.two_pence_output_var.set("£0.00")
        else:
            try:
                number_of_2p = int(two_pence)
                self.tot_2p = f'{(number_of_2p * 0.02):.2f}'
                self.two_pence_output_var.set("£" + self.tot_2p)
                self.tot_2p = float(self.tot_2p)
                self.total_array.append(self.tot_2p)
            except ValueError:
                self.error_flag = True
                self.two_pence_output_var.set("!")

        if len(five_pence) == 0:
            self.five_pence_input_var.set("0")
            self.five_pence_output_var.set("£0.00")
        else:
            try:
                number_of_5p = int(five_pence)
                self.tot_5p = f'{(number_of_5p * 0.05):.2f}'
                self.five_pence_output_var.set("£" + self.tot_5p)
                self.tot_5p = float(self.tot_5p)
                self.total_array.append(self.tot_5p)
            except ValueError:
                self.error_flag = True
                self.five_pence_output_var.set("!")

        if len(ten_pence) == 0:
            self.ten_pence_input_var.set("0")
            self.ten_pence_output_var.set("£0.00")
        else:
            try:
                number_of_10p = int(ten_pence)
                self.tot_10p = f'{(number_of_10p * 0.10):.2f}'
                self.ten_pence_output_var.set("£" + self.tot_10p)
                self.tot_10p = float(self.tot_10p)
                self.total_array.append(self.tot_10p)
            except ValueError:
                self.error_flag = True
                self.ten_pence_output_var.set("!")

        if len(twenty_pence) == 0:
            self.twenty_pence_input_var.set("0")
            self.twenty_pence_output_var.set("£0.00")
        else:
            try:
                number_of_20p = int(twenty_pence)
                self.tot_20p = f'{(number_of_20p * 0.20):.2f}'
                self.twenty_pence_output_var.set("£" + self.tot_20p)
                self.tot_20p = float(self.tot_20p)
                self.total_array.append(self.tot_20p)
            except ValueError:
                self.error_flag = True
                self.twenty_pence_output_var.set("!")

        if len(fifty_pence) == 0:
            self.fifty_pence_input_var.set("0")
            self.fifty_pence_output_var.set("£0.00")
        else:
            try:
                number_of_50p = int(fifty_pence)
                self.tot_50p = f'{(number_of_50p * 0.50):.2f}'
                self.fifty_pence_output_var.set("£" + self.tot_50p)
                self.tot_50p = float(self.tot_50p)
                self.total_array.append(self.tot_50p)
            except ValueError:
                self.error_flag = True
                self.fifty_pence_output_var.set("!")

        if len(one_pound) == 0:
            self.one_pound_input_var.set("0")
            self.one_pound_output_var.set("£0.00")
        else:
            try:
                number_of_1pound = int(one_pound)
                self.tot_1pound = f'{(number_of_1pound * 1.00):.2f}'
                self.one_pound_output_var.set("£" + self.tot_1pound)
                self.tot_1pound = float(self.tot_1pound)
                self.total_array.append(self.tot_1pound)
            except ValueError:
                self.error_flag = True
                self.one_pound_output_var.set("!")

        if len(two_pound) == 0:
            self.two_pound_input_var.set("0")
            self.two_pound_output_var.set("£0.00")
        else:
            try:
                number_of_2pound = int(two_pound)
                self.tot_2pound = f'{(number_of_2pound * 2.00):.2f}'
                self.two_pound_output_var.set("£" + self.tot_2pound)
                self.tot_2pound = float(self.tot_2pound)
                self.total_array.append(self.tot_2pound)
            except ValueError:
                self.error_flag = True
                self.two_pound_output_var.set("!")

        if not self.error_flag:

            output = f'{sum(self.total_array):.2f}'
            output = ("£" + str(output))
            self.total.set(output)

        elif self.error_flag:
            self.total.set("!!!")


if __name__ == "__main__":
    my_window = tk.Tk()
    MainApp(my_window)
    my_window.mainloop()
