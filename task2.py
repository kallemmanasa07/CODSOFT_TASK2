import tkinter as tk
from tkinter import messagebox


# ---------------- FUNCTIONS ---------------- #

def click(value):
    entry.insert(tk.END, value)


def clear():
    entry.delete(0, tk.END)


def backspace(event=None):
    current = entry.get()

    if current:
        entry.delete(len(current) - 1, tk.END)

    return "break"


def calculate(event=None):
    try:
        expression = entry.get().strip()

        if not expression:
            return

        result = eval(expression)

        entry.delete(0, tk.END)
        entry.insert(0, str(result))

    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")

    except Exception:
        messagebox.showerror("Error", "Invalid Expression!")


def key_filter(event):
    allowed = "0123456789+-*/."

    # Allow Enter and Backspace
    if event.keysym in ("Return", "BackSpace"):
        return

    if event.char and event.char not in allowed:
        return "break"


# ---------------- WINDOW ---------------- #

root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="#dfeaf5")

try:
    root.state("zoomed")
except:
    root.geometry("1200x700")

# ---------------- MAIN FRAME ---------------- #

frame = tk.Frame(
    root,
    bg="white",
    bd=5,
    relief="ridge",
    padx=30,
    pady=30
)

frame.place(relx=0.5, rely=0.5, anchor="center")

# ---------------- TITLE ---------------- #

title = tk.Label(
    frame,
    text="Simple Calculator",
    font=("Arial", 28, "bold"),
    bg="white",
    fg="#1f4e79"
)

title.grid(row=0, column=0, columnspan=4, pady=15)

# ---------------- DISPLAY ---------------- #

entry = tk.Entry(
    frame,
    font=("Arial", 24),
    width=20,
    justify="right",
    bd=8
)

entry.grid(row=1, column=0, columnspan=4, padx=10, pady=20)
entry.focus_set()

# ---------------- BUTTONS ---------------- #

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '⌫', '+'],
    ['C', '=']
]

for r, row in enumerate(buttons):
    for c, char in enumerate(row):

        if char == "=":
            cmd = calculate
            color = "#28a745"

        elif char == "C":
            cmd = clear
            color = "#dc3545"

        elif char == "⌫":
            cmd = backspace
            color = "#ff9800"

        else:
            cmd = lambda x=char: click(x)
            color = "#1f4e79"

        btn = tk.Button(
            frame,
            text=char,
            command=cmd,
            font=("Arial", 20, "bold"),
            width=5,
            height=2,
            bg=color,
            fg="white",
            activebackground=color
        )

        if r == 4:
            btn.grid(
                row=r + 2,
                column=c * 2,
                columnspan=2,
                padx=8,
                pady=8,
                sticky="nsew"
            )
        else:
            btn.grid(
                row=r + 2,
                column=c,
                padx=8,
                pady=8
            )

# ---------------- KEYBOARD SUPPORT ---------------- #

entry.bind("<Return>", calculate)
root.bind("<Return>", calculate)

entry.bind("<BackSpace>", backspace)

entry.bind("<Key>", key_filter)

# ---------------- FOOTER ---------------- #

footer = tk.Label(
    root,
    text="Enter = Calculate | Backspace = Delete | Supports Keyboard Input",
    font=("Arial", 12),
    bg="#dfeaf5",
    fg="gray"
)

footer.pack(side="bottom", pady=10)

# ---------------- RUN ---------------- #

root.mainloop()