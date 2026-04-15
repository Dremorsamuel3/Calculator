import tkinter as tk

# Create window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Entry field
entry = tk.Entry(root, font=("Arial", 18), borderwidth=5, justify='right')
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Functions
def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression, {"__builtins__": None}, {})
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Button layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3)
]

# Create buttons
for (text, row, col) in buttons:
    if text == "C":
        btn = tk.Button(root, text=text, font=("Arial", 14), command=clear)
    elif text == "=":
        btn = tk.Button(root, text=text, font=("Arial", 14), command=calculate)
    else:
        btn = tk.Button(root, text=text, font=("Arial", 14),
                        command=lambda t=text: click(t))

    btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

# Make layout responsive
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Run app
root.mainloop()