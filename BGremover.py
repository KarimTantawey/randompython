import tkinter as tk
from tkinter import filedialog
from rembg import remove
from PIL import Image, ImageTk
import threading

class BackgroundRemoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Background Remover")
        
        self.output_image = None
        self.output_image_path = 'output.png'

        self.label = tk.Label(root, text="Select an image to remove background")
        self.label.pack(pady=10)
        
        self.select_button = tk.Button(root, text="Select Image", command=self.select_image)
        self.select_button.pack(pady=5)
        
        self.save_button = tk.Button(root, text="Save Picture", command=self.save_image, state=tk.DISABLED)
        self.save_button.pack(pady=5)
        
        self.canvas = tk.Canvas(root, width=800, height=800) 
        self.canvas.pack(pady=10)
        
        self.image_label = tk.Label(root, text="")
        self.image_label.pack(pady=5)
    
    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            print(f"Selected image: {file_path}")
            threading.Thread(target=self.process_image, args=(file_path,)).start()

    def process_image(self, input_image_path):
        try:
        
            input_image = Image.open(input_image_path)
            
            
            self.output_image = remove(input_image)
            self.output_image.save(self.output_image_path)
            
            
            self.root.after(0, self.update_image_display)
            self.root.after(0, self.image_label.config, {"text": "Background removed! Ready to save."})
            self.root.after(0, self.save_button.config, {"state": tk.NORMAL}) 
        except Exception as e:
            self.root.after(0, self.image_label.config, {"text": f"An error occurred: {e}"})
    
    def update_image_display(self):
        if self.output_image:
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            img_width, img_height = self.output_image.size
            
            
            scale = min(canvas_width / img_width, canvas_height / img_height)
            new_width = int(img_width * scale)
            new_height = int(img_height * scale)
            
            resized_image = self.output_image.resize((new_width, new_height), Image.LANCZOS)
            
            output_image_tk = ImageTk.PhotoImage(resized_image)
           
            self.canvas.delete("all")
          
            self.canvas.create_image(0, 0, anchor=tk.NW, image=output_image_tk)
            self.canvas.image = output_image_tk  
    
    def save_image(self):
        if self.output_image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                   filetypes=[("PNG files", "*.png"),
                                                              ("All files", "*.*")])
            if save_path:
                self.output_image.save(save_path)
                self.image_label.config(text=f"Image saved as {save_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BackgroundRemoverApp(root)
    root.mainloop()
