import tkinter as tk
# Function to perform the calculation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = operator_var.get()

        if operator == "+":
            result.set(num1 + num2)
        elif operator == "-":
            result.set(num1 - num2)
        elif operator == "*":
            result.set(num1 * num2)
        elif operator == "/":
            if num2 == 0:
                result.set("Error: Division by zero")
            else:
                result.set(num1 / num2)
    except ValueError:
        result.set("Error: Invalid input")


# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry fields
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=0, padx=10, pady=10)

operator_var = tk.StringVar()
operator_var.set("+")
operator_menu = tk.OptionMenu(root, operator_var, "+", "-", "*", "/")
operator_menu.grid(row=0, column=1, padx=10, pady=10)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=0, column=2, padx=10, pady=10)

# Button to perform the calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Result label
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Run the main loop
root.mainloop()

