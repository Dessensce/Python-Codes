import tkinter as tk
import binascii

def text_to_hex():
    text = text_entry.get()
    hex_representation = binascii.hexlify(text.encode()).decode()
    formatted_hex = ' '.join(hex_representation[i:i+2] for i in range(0, len(hex_representation), 2))
    hex_output.delete(0, tk.END)
    hex_output.insert(0, formatted_hex)

def hex_to_text():
    hex_representation = hex_entry.get()
    try:
        decoded_text = binascii.unhexlify(hex_representation).decode()
        text_output.delete(0, tk.END)
        text_output.insert(0, decoded_text)
    except binascii.Error:
        text_output.delete(0, tk.END)
        text_output.insert(0, "Invalid hexadecimal input.")

# Create the main window
window = tk.Tk()
window.title("Text-Hex Converter")
window.configure(bg="#282c36")  # Darker background color

# Styling
title_label = tk.Label(window, text="Text-Hex Converter", font=("Helvetica", 24, "bold"), fg="#FFFFFF", bg="#282c36")
title_label.grid(row=0, columnspan=2, pady=(20, 10))

# Text to Hex conversion
text_entry = tk.Entry(window, bg="#353b48", fg="#FFFFFF", font=("Helvetica", 12), insertbackground="#FFFFFF")
text_entry.grid(row=1, column=0, padx=10, pady=10)
text_convert_button = tk.Button(window, text="Convert to Hex", command=text_to_hex, bg="#007BFF", fg="#FFFFFF", font=("Helvetica", 12))
text_convert_button.grid(row=1, column=1, padx=10, pady=10)
hex_output = tk.Entry(window, bg="#353b48", fg="#FFFFFF", font=("Helvetica", 12), insertbackground="#FFFFFF", justify="right")
hex_output.grid(row=2, columnspan=2, padx=10, pady=10)

# Hex to Text conversion
hex_entry = tk.Entry(window, bg="#353b48", fg="#FFFFFF", font=("Helvetica", 12), insertbackground="#FFFFFF")
hex_entry.grid(row=3, column=0, padx=10, pady=10)
hex_convert_button = tk.Button(window, text="Convert to Text", command=hex_to_text, bg="#007BFF", fg="#FFFFFF", font=("Helvetica", 12))
hex_convert_button.grid(row=3, column=1, padx=10, pady=10)
text_output = tk.Entry(window, bg="#353b48", fg="#FFFFFF", font=("Helvetica", 12), insertbackground="#FFFFFF", justify="right")
text_output.grid(row=4, columnspan=2, padx=10, pady=10)

# Run the GUI loop
window.mainloop()
