import tkinter as tk

def add():
    result.set(float(num1.get()) + float(num2.get()))

def subtract():
    result.set(float(num1.get()) - float(num2.get()))

def multiply():
    result.set(float(num1.get()) * float(num2.get()))

def divide():
    if float(num2.get()) == 0:
        result.set("Error: Division by zero")
    else:
        result.set(float(num1.get()) / float(num2.get()))


root = tk.Tk()
root.title("Simple Calculator")
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)


num1_label = tk.Label(root, text="First Number:")
num1_label.grid(row=0, column=0, sticky="ew")
num1 = tk.Entry(root)
num1.grid(row=0, column=1, sticky="ew")

num2_label = tk.Label(root, text="Second Number:")
num2_label.grid(row=1, column=0, sticky="ew")
num2 = tk.Entry(root)
num2.grid(row=1, column=1, sticky="ew")

result = tk.StringVar()
result_label = tk.Label(root, text="Result:", textvariable=result)
result_label.grid(row=2, column=0, columnspan=2, sticky="ew")


add_button = tk.Button(root, text="Add", command=add)
add_button.grid(row=3, column=0, sticky="ew")

subtract_button = tk.Button(root, text="Subtract", command=subtract)
subtract_button.grid(row=3, column=1, sticky="ew")

multiply_button = tk.Button(root, text="Multiply", command=multiply)
multiply_button.grid(row=4, column=0, sticky="ew")

divide_button = tk.Button(root, text="Divide", command=divide)
divide_button.grid(row=4, column=1, sticky="ew")


root.mainloop()