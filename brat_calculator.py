import tkinter as tk

def press_key(key):
    current = display_var.get()
    if key == "C":
        display_var.set("")
    elif key == "=":
        try:
            # Evaluate the expression
            result = eval(current)
            display_var.set(str(result))
        except Exception:
            display_var.set("error")
    else:
        display_var.set(current + str(key))

# Brat theme colors and settings
BRAT_GREEN = "#8ace00"
BRAT_FONT = ("Arial Narrow", 18, "bold") # Attempting to look like the album font
DISPLAY_FONT = ("Arial", 24)

root = tk.Tk()
root.title("brat calculator")
root.geometry("300x400")
root.configure(bg=BRAT_GREEN)

display_var = tk.StringVar()

# Display Area
display_entry = tk.Entry(
    root, 
    textvariable=display_var, 
    font=DISPLAY_FONT, 
    bg=BRAT_GREEN, 
    fg="black", 
    highlightthickness=0,
    bd=0,
    justify="right"
)
display_entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, sticky="ew")

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    button = tk.Button(
        root, 
        text=text, 
        font=BRAT_FONT,
        bg=BRAT_GREEN, 
        fg="black",
        activebackground=BRAT_GREEN,
        activeforeground="white", # slight interaction
        bd=1,
        relief="flat",
        command=lambda t=text: press_key(t)
    )
    button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

# Configure grid weights to expand evenly
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)

if __name__ == "__main__":
    root.mainloop()
