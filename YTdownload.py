import os
import yt_dlp
import tkinter as tk
from tkinter import messagebox, filedialog

def download_video():
    url = url_entry.get()
    download_path = filedialog.askdirectory()
    if not url or not download_path:
        messagebox.showerror("Error", "Please provide a valid URL and download path.")
        return

    quality_mapping = {
        "360p": "best[height<=360][vcodec!=none][acodec!=none]/bestvideo[height<=360]+bestaudio/best",
        "480p": "best[height<=480][vcodec!=none][acodec!=none]/bestvideo[height<=480]+bestaudio/best",
        "720p": "best[height<=720][vcodec!=none][acodec!=none]/bestvideo[height<=720]+bestaudio/best",
        "1080p": "best[height<=1080][vcodec!=none][acodec!=none]/bestvideo[height<=1080]+bestaudio/best",
        "4k": "best[height<=2160][vcodec!=none][acodec!=none]/bestvideo[height<=2160]+bestaudio/best",
        "Audio Only": "bestaudio[ext=m4a]/bestaudio"
    }

    ydl_opts = {
        'format': quality_mapping[quality_var.get()],
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',  
        'postprocessors': [{  
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'nocheckcertificate': True,    
        'noplaylist': True,           
        'ignoreerrors': True,          
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'ffmpeg_location': 'C:\Program Files (x86)\\ffmpeg\\bin' ,
        'extractor_args': {'youtube': {'player_client': ['android']}}
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Download completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("400x250")


tk.Label(root, text="YouTube URL:").pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

quality_var = tk.StringVar(value="360p")
tk.Label(root, text="Select Quality:").pack(pady=10)
quality_options = ["360p", "480p", "720p", "1080p", "4k", "Audio Only"]
quality_menu = tk.OptionMenu(root, quality_var, *quality_options)
quality_menu.pack(pady=5)

# Download Button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(pady=20)

root.mainloop()
