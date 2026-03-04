import tkinter as tk
from tkinter import colorchooser

def pick_color():
    # Opens the standard OS color picker (the "drag" interface)
    color_info = colorchooser.askcolor(title="Select a Color")

    # color_info returns ((R, G, B), "#hexcode")
    if color_info[1]:
        hex_code = color_info[1]

        # Update the interface
        canvas.config(bg=hex_code)
        label.config(text=f"Selected HEX: {hex_code.upper()}", bg="white")

# Main window setup
root = tk.Tk()
root.title("Visual Color Tester")
root.geometry("500x400")
root.configure(bg="white")

# Instruction Label
instruction = tk.Label(root, text="Click the button to drag and select a color:", bg="white", font=("Arial", 12))
instruction.pack(pady=15)

# The "Swatch" Area (shows the color on white)
canvas = tk.Frame(root, width=300, height=200, highlightbackground="white", highlightthickness=1)
canvas.pack(pady=10)

# Display the HEX code
label = tk.Label(root, text="HEX Code: #FFFFFF", bg="white", font=("Courier", 14, "bold"))
label.pack(pady=10)

# The Trigger Button
btn = tk.Button(root, text="Open Color Map", command=pick_color, padx=20, pady=10)
btn.pack(pady=20)

root.mainloop()
