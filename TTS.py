import tkinter as tk
from gtts import gTTS
import os
import pygame
import random
import string

def generate_random_filename(extension=".mp3"):
 
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return random_string + extension

def say_sentence():
    sentence = sentence_var.get()
    tts = gTTS(text=sentence, lang='en')
    
    random_filename = generate_random_filename()
    tts.save(random_filename)
    
    pygame.mixer.init()
    pygame.mixer.music.load(random_filename)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        root.update()  
    
    pygame.mixer.music.unload()  
    pygame.mixer.quit()  
    os.remove(random_filename)


root = tk.Tk()
root.title("Text to Speech")
root.geometry("400x200")
root.configure(bg='#2b2b2b')

sentence_var = tk.StringVar()


title_label = tk.Label(root, text="Text to Speech Converter", bg='#2b2b2b', fg='#ffffff', font=("Helvetica", 16))
sentence_entry = tk.Entry(root, textvariable=sentence_var, width=40)
say_button = tk.Button(root, text="Say It", command=say_sentence, bg='#3c3f41', fg='#ffffff')


title_label.pack(pady=10)
sentence_entry.pack(pady=20)
say_button.pack(pady=20)


root.mainloop()
