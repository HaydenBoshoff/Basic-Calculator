from tkinter import *
import tkinter as tk
from string import ascii_letters


class Calculator:
    """Manage the calculators behaviour and functionality."""
    def __init__(self):
        """Initializing the calculator attributes."""
        self.expression = ""
        self.total = None

        # Root
        self.root = Tk()
        self.root.title("Calculator by Hayden Boshoff")
        self.root.geometry("400x544")  # If you change this make sure to change the canvas width and height as well.
        self.root.resizable(False, False)
        self.root.iconbitmap("icon.ico")

        # Appearance
        font = "Helvetica"
        font_size = 20
        canvas = tk.Canvas(self.root, width=400, height=544)
        canvas.pack()

        # Entry Field
        self.entry_text = StringVar()
        self.entry = tk.Entry(canvas, textvariable=self.entry_text)
        self.entry.config(font=(font, 26))
        canvas.create_window(200, 32, window=self.entry)

        # Number Buttons
        button_0 = tk.Button(self.root, text="0", width=11, height=2)
        button_0.config(font=(font, font_size), relief=GROOVE, command=lambda: self.press(0))
        canvas.create_window(101, 492, window=button_0)

        button_1 = tk.Button(self.root, text="1", width=5, height=2)
        button_1.config(font=(font, font_size), relief=GROOVE, command=lambda: self.press(1))
        canvas.create_window(53, 396, window=button_1)

        button_2 = tk.Button(self.root, text="2", width=5, height=2)
        button_2.config(font=(font, font_size), relief=GROOVE, command=lambda: self.press(2))
        canvas.create_window(151, 396, window=button_2)

        button_3 = tk.Button(self.root, text="3", width=5, height=2)
        button_3.config(font=(font, font_size), relief=GROOVE, command=lambda: self.press(3))
        canvas.create_window(249, 396, window=button_3)

        button_4 = tk.Button(self.root, text="4", width=5, height=2)
        button_4.config(font=(font, font_size), relief=GROOVE, command=lambda: self.press(4))
        canvas.create_window(53, 300, window=button_4)

        button_5 = tk.Button(self.root, text="5", width=5, height=2)
        button_5.config(font=(font, font_size), relief=GROOVE, command=lambda: self.press(5))
        canvas.create_window(151, 300, window=button_5)

        button_6 = tk.Button(self.root, text="6", width=5, height=2)
        button_6.config(font=(font, font_size), relief=GROOVE, command=lambda: self.press(6))
        canvas.create_window(249, 300, window=button_6)

        button_7 = tk.Button(self.root, text="7", width=5, height=2)
        button_7.config(font=(font, font_size), relief=GROOVE, command=lambda: self.press(7))
        canvas.create_window(53, 204, window=button_7)

        button_8 = tk.Button(self.root, text="8", width=5, height=2)
        button_8.config(font=(font, font_size), relief=GROOVE, command=lambda: self.press(8))
        canvas.create_window(151, 204, window=button_8)

        button_9 = tk.Button(self.root, text="9", width=5, height=2)
        button_9.config(font=(font, font_size), relief=GROOVE, command=lambda: self.press(9))
        canvas.create_window(249, 204, window=button_9)

        # Operator and Function Buttons
        button_clear = tk.Button(self.root, text="C", width=5, height=2)
        button_clear.config(font=(font, font_size), relief=GROOVE, command=self.clear)
        canvas.create_window(53, 108, window=button_clear)

        button_divide = tk.Button(self.root, text="÷", width=5, height=2)
        button_divide.config(font=(font, font_size), relief=GROOVE, command=lambda: self.press("/"))
        canvas.create_window(151, 108, window=button_divide)

        button_multiply = tk.Button(self.root, text="×", width=5, height=2)
        button_multiply.config(font=(font, font_size), relief=GROOVE, command=lambda: self.press("*"))
        canvas.create_window(249, 108, window=button_multiply)

        button_backspace = tk.Button(self.root, text="⌫", width=5, height=2)
        button_backspace.config(font=(font, font_size), relief=GROOVE, command=self.backspace)
        canvas.create_window(347, 108, window=button_backspace)

        button_addition = tk.Button(self.root, text="+", width=5, height=2)
        button_addition.config(font=(font, font_size), relief=GROOVE, command=lambda: self.press("+"))
        canvas.create_window(347, 204, window=button_addition)

        button_subtraction = tk.Button(self.root, text="-", width=5, height=2)
        button_subtraction.config(font=(font, font_size), relief=GROOVE, command=lambda: self.press("-"))
        canvas.create_window(347, 300, window=button_subtraction)

        button_enter = tk.Button(self.root, text="=", width=5, height=5)
        button_enter.config(font=(font, font_size), relief=GROOVE, command=self.equal)
        canvas.create_window(347, 444, window=button_enter)

        button_decimal = tk.Button(self.root, text=".", width=5, height=2)
        button_decimal.config(font=(font, font_size), relief=GROOVE, command=lambda: self.press("."))
        canvas.create_window(249, 492, window=button_decimal)

    def press(self, num):
        """Check what has been pressed and add it to the expression variable"""
        self.expression += str(num)
        self.entry_text.set(self.expression)

    def backspace(self):
        """Delete the last character of the sequence"""
        self.entry_text.get()
        self.expression = self.expression[:-1]
        self.entry_text.set(self.expression)

    def clear(self):
        """Clear the expression and entry text"""
        self.expression = ""
        self.entry_text.set("")

    def equal(self):
        """Evaluate the sum of the expression"""
        self.expression = self.entry_text.get()
        contains_letters = False

        for i in self.expression:
            if i in ascii_letters:
                contains_letters = True
                break

        if contains_letters:
            self.entry_text.set("ERROR")
            self.expression = ""
        else:
            # Due to the Syntax Error (Leading zeros not permitted) I had to add a number variable which will set
            # the number of leading zeros you can have to 10,000 which I think would suffice. It is a high number,
            # but it doesn't slow the program down at all, if the expression is valid it would just evaluate it and
            # not keep looping.
            number = 0
            while number < 10000:
                try:
                    self.total = eval(self.expression)

                    # Check if the expression evaluates to an integer or float and display the number accordingly.
                    if self.total % 1 == 0:
                        result = int(self.total)
                        self.expression = str(result)
                        self.entry_text.set(str(result))
                        break
                    else:
                        self.expression = str(self.total)
                        self.entry_text.set(str(self.total))
                        break
                except SyntaxError:
                    # Catches the leading zeros until there aren't any left.
                    if self.expression.startswith("0"):
                        self.expression = self.expression[1:]
                        self.entry_text.set(self.expression)
                        number += 1
                    # Catches other errors that may arise.
                    else:
                        self.expression = ""
                        self.entry_text.set("ERROR")
                        break
                # Reset the number value so that can allow for a program loop.
                number = 0


if __name__ == "__main__":
    calculator = Calculator()

    """This looks messy, and I will try my best to fix it but as of now that is the best way I know how to do it.
       I have tried to create a for loop to create the bindings for me but it didn't work"""

    # Number Keybind
    calculator.root.bind("0", lambda event: calculator.press(0))
    calculator.root.bind("1", lambda event: calculator.press(1))
    calculator.root.bind("2", lambda event: calculator.press(2))
    calculator.root.bind("3", lambda event: calculator.press(3))
    calculator.root.bind("4", lambda event: calculator.press(4))
    calculator.root.bind("5", lambda event: calculator.press(5))
    calculator.root.bind("6", lambda event: calculator.press(6))
    calculator.root.bind("7", lambda event: calculator.press(7))
    calculator.root.bind("8", lambda event: calculator.press(8))
    calculator.root.bind("9", lambda event: calculator.press(9))

    # Operator and Function Buttons
    calculator.root.bind("<Delete>", lambda event: calculator.clear())
    calculator.root.bind("/", lambda event: calculator.press("/"))
    calculator.root.bind("*", lambda event: calculator.press("*"))
    calculator.root.bind("<BackSpace>", lambda event: calculator.backspace())
    calculator.root.bind("+", lambda event: calculator.press("+"))
    calculator.root.bind("-", lambda event: calculator.press("-"))
    calculator.root.bind("<Return>", lambda event: calculator.equal())
    calculator.root.bind(".", lambda event: calculator.press("."))

    # Main Loop
    calculator.root.mainloop()
