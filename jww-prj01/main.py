import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("계산기") # Calculator in Korean
        master.geometry("300x400")
        master.resizable(False, False) # Make window not resizable

        self.expression = ""
        self.input_text = tk.StringVar()

        # Entry widget to display the expression/result
        self.input_field = tk.Entry(master, textvariable=self.input_text, font=('arial', 20, 'bold'),
                                     bd=10, insertwidth=4, width=14, borderwidth=4, justify='right')
        self.input_field.grid(row=0, column=0, columnspan=4, pady=10)
        self.input_field.focus_set()

        # Define buttons in a list of lists for easier grid placement
        # Each inner list represents a row
        button_layout = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', '=', '+']
        ]

        # Create and place buttons
        for r_idx, row_buttons in enumerate(button_layout):
            for c_idx, button_text in enumerate(row_buttons):
                if button_text == '=':
                    btn = tk.Button(master, text=button_text, fg="black", width=5, height=2, bd=1,
                                    font=('arial', 14, 'bold'), command=self.on_equals)
                else:
                    btn = tk.Button(master, text=button_text, fg="black", width=5, height=2, bd=1,
                                    font=('arial', 14, 'bold'), command=lambda b=button_text: self.on_button_click(b))
                btn.grid(row=r_idx + 1, column=c_idx, pady=1, padx=1, sticky="nsew") # +1 because row 0 is for entry

        # Add Clear button separately, spanning across columns
        clear_button = tk.Button(master, text='C', fg="black", width=5, height=2, bd=1,
                                  font=('arial', 14, 'bold'), command=self.on_clear)
        clear_button.grid(row=len(button_layout) + 1, column=0, columnspan=4, pady=1, padx=1, sticky="nsew")

        # Configure column and row weights to make buttons expand
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)
        for i in range(len(button_layout) + 2): # +2 for entry row and clear button row
            master.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        """
        Appends the clicked character (number or operator) to the expression.
        """
        self.expression += str(char)
        self.input_text.set(self.expression)

    def on_clear(self):
        """
        Clears the current expression and the display.
        """
        self.expression = ""
        self.input_text.set("")

    def on_equals(self):
        """
        Evaluates the expression and displays the result.
        Handles errors like division by zero or invalid syntax.
        """
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result # Allow further operations on the result
        except ZeroDivisionError:
            messagebox.showerror("오류", "0으로 나눌 수 없습니다.") # Cannot divide by zero
            self.expression = ""
            self.input_text.set("")
        except SyntaxError:
            messagebox.showerror("오류", "잘못된 수식입니다.") # Invalid expression
            self.expression = ""
            self.input_text.set("")
        except Exception as e:
            messagebox.showerror("오류", f"오류가 발생했습니다: {e}") # An error occurred
            self.expression = ""
            self.input_text.set("")

# Main part of the script
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
