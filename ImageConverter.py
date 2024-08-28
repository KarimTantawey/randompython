import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def convert_image():
    # Open file dialog to select an image file
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image Files",
                     "*.jpg *.jpeg *.png *.bmp *.tiff *.gif *.webp")]
    )

    if not file_path:
        return

    # Open file dialog to select the save location
    save_path = filedialog.asksaveasfilename(
        title="Save Converted Image",
        defaultextension=".jpg",
        filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")]
    )

    if not save_path:
        return

    try:
        # Open the selected image
        with Image.open(file_path) as img:
            # Save the image in the desired format
            img.save(save_path)
        messagebox.showinfo("Success", f"Image converted and saved to {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert image: {str(e)}")

# Create the main application window
root = tk.Tk()
root.title("Image Converter")
root.geometry("300x150")

# Create and place the convert button
convert_button = tk.Button(root, text="Convert Image", command=convert_image, width=20, height=2)
convert_button.pack(pady=20)

# Run the application
root.mainloop()
