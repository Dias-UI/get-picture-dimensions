"""
Image Dimensions Viewer
UI to scan a folder and display the resolution
(width × height) of all image files inside.

Features:
- Folder picker dialog
- Supports JPG, PNG, GIF, BMP
- Dark themed interface
- Displays dimensions in a scrollable text box

Useful for quickly checking image sizes before uploads,
batch processing, or asset organization.
"""

import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

# Define color palette
BG_COLOR = "#1e1e1e"
FG_COLOR = "#f0f0f0"
BTN_COLOR = "#0097e6"

def get_image_dimensions(folder_path):
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('jpg', 'jpeg', 'png', 'gif', 'bmp'))]
    if not image_files:
        messagebox.showerror("Error", "No image files found in the selected folder.")
        return

    image_dimensions = []
    for image_file in image_files:
        try:
            image_path = os.path.join(folder_path, image_file)
            with Image.open(image_path) as img:
                width, height = img.size
                image_dimensions.append((image_file, f"{width} x {height}"))
        except Exception as e:
            print(f"Error processing {image_file}: {e}")

    return image_dimensions

def display_dimensions():
    folder_path = folder_entry.get()
    if not folder_path:
        messagebox.showerror("Error", "Please select a folder.")
        return

    dimensions = get_image_dimensions(folder_path)
    if not dimensions:
        return

    result_text.delete(1.0, tk.END)
    for image_file, dimension in dimensions:
        result_text.insert(tk.END, f"{image_file}\t{dimension}\n")

# Create the main window
root = tk.Tk()
root.title("Image Dimensions")
root.geometry("400x400")
root.configure(bg=BG_COLOR)

# Label and entry for input folder
folder_label = tk.Label(root, text="Select Folder:", fg=FG_COLOR, bg=BG_COLOR)
folder_label.pack(pady=10)
folder_entry = tk.Entry(root, fg=FG_COLOR, bg=BG_COLOR, width=50)
folder_entry.pack(pady=5)
folder_button = tk.Button(root, text="Browse", fg=FG_COLOR, bg=BTN_COLOR,
                          command=lambda: folder_entry.insert(tk.END, filedialog.askdirectory()))
folder_button.pack(pady=5)

# Display dimensions button
display_button = tk.Button(root, text="Display Image Dimensions", fg=FG_COLOR, bg=BTN_COLOR, command=display_dimensions)
display_button.pack(pady=10)

# Text widget to show image dimensions
result_text = tk.Text(root, fg=FG_COLOR, bg=BG_COLOR, wrap=tk.WORD)
result_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
