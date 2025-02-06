from PIL import Image, ImageOps
import argparse
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, ttk

def convert_image(path, dithering=False, threshold=128, negative=False, size=None, scale=1):
    try:
        img = Image.open(path).convert("L")
    except FileNotFoundError:
        messagebox.showerror("Error", "Image file not found.")
        return None
    except Exception as e:
        messagebox.showerror("Error", f"Could not open image: {e}")
        return None

    if size != None:
        img = img.resize(size)
    elif scale != 1:
        width, height = img.size
        img = img.resize((round(width*scale), round(height*scale)))

    if negative == True:
        img = ImageOps.invert(img)

    if dithering == True:
        img = img.convert("1").convert("L")
        threshold = 1

    pixels = img.load()
    width, height = img.size
    for x in range(0, width):
        for y in range(0, height):
            pixels[x, y] = min(1, pixels[x, y]//threshold)

    newsize_x = width//2*2
    newsize_y = height//4*4

    new = Image.new(mode="L", size=(newsize_x, newsize_y))
    new.paste(img, (0, 0))
    pixels = new.load()

    result = ""
    for y in range(0, newsize_y, 4):
        for x in range(0, newsize_x, 2):
            pattern = []
            for offset in range(0, 4):
                row = [pixels[x, y+offset],
                       pixels[x+1, y+offset]]
                pattern.append(row)
            result += encode_pattern(pattern)
        result += "\n"

    return result[:-1]

def encode_pattern(pattern):
    sorted_pattern = [0]*8
    for i in range(0, 3):
        row = pattern[i]
        sorted_pattern[i] = row[0]
        sorted_pattern[i+3] = row[1]

    sorted_pattern[6] = pattern[3][0]
    sorted_pattern[7] = pattern[3][1]
    sorted_pattern = list(map(str, sorted_pattern[::-1]))

    num1 = int("".join(sorted_pattern),2)
    num2 = 10240 + num1
    char = chr(num2)
    return char

class ImageConverterGUI:
    def __init__(self, master):
        self.master = master
        master.title("Image to Braille Converter")

        self.path = ""

        # Variables for GUI elements
        self.dithering = tk.BooleanVar()
        self.negative = tk.BooleanVar()
        self.scale = tk.DoubleVar(value=1.0)
        self.threshold = tk.IntVar(value=100)
        self.sizex = tk.IntVar(value=-1)
        self.sizey = tk.IntVar(value=-1)

        # UI Elements
        self.open_button = tk.Button(master, text="Open Image", command=self.open_image)
        self.open_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.path_label = tk.Label(master, text="No image selected")
        self.path_label.grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

        self.dithering_check = tk.Checkbutton(master, text="Dithering", variable=self.dithering)
        self.dithering_check.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.negative_check = tk.Checkbutton(master, text="Negative", variable=self.negative)
        self.negative_check.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.scale_label = tk.Label(master, text="Scale:")
        self.scale_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.scale_entry = tk.Entry(master, textvariable=self.scale, width=5)
        self.scale_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.threshold_label = tk.Label(master, text="Threshold:")
        self.threshold_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.threshold_entry = tk.Entry(master, textvariable=self.threshold, width=5)
        self.threshold_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        self.sizex_label = tk.Label(master, text="Size X:")
        self.sizex_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.sizex_entry = tk.Entry(master, textvariable=self.sizex, width=5)
        self.sizex_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        self.sizey_label = tk.Label(master, text="Size Y:")
        self.sizey_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.sizey_entry = tk.Entry(master, textvariable=self.sizey, width=5)
        self.sizey_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        self.convert_button = tk.Button(master, text="Convert", command=self.convert)
        self.convert_button.grid(row=6, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

        self.result_text = tk.Text(master, height=10, width=50)
        self.result_text.grid(row=7, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

        # Configure grid weights so the text box expands
        for i in range(4):
            master.columnconfigure(i, weight=1)
        master.rowconfigure(7, weight=1)

    def open_image(self):
        self.path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
        if self.path:
            self.path_label.config(text=self.path)
        else:
            self.path_label.config(text="No image selected")

    def convert(self):
        if not self.path:
            messagebox.showerror("Error", "Please select an image first.")
            return

        size = None
        if self.sizey.get() != -1 and self.sizex.get() != -1:
            size = (self.sizex.get(), self.sizey.get())

        try:
            result = convert_image(
                self.path,
                dithering=self.dithering.get(),
                negative=self.negative.get(),
                scale=self.scale.get(),
                threshold=self.threshold.get(),
                size=size
            )

            if result is not None:
                self.result_text.delete("1.0", tk.END)
                self.result_text.insert(tk.END, result)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during conversion: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    gui = ImageConverterGUI(root)
    root.mainloop()
