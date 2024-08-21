import requests
import random
from PIL import Image, ImageTk
import io
import tkinter as tk

def fetch_random_image(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/new.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        image_posts = [post['data']['url'] for post in posts if post['data']['url'].endswith(('jpg', 'jpeg', 'png'))]

        if image_posts:
            random_image = random.choice(image_posts)
            return random_image
        else:
            print("No images found in the latest posts.")
            return None
    else:
        print(f"Error: {response.status_code}")
        return None

def download_image(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        image_bytes = io.BytesIO(response.content)
        img = Image.open(image_bytes)
        max_width = 800
        max_height = 600
        
        img.thumbnail((max_width, max_height), Image.LANCZOS)
        return img
    else:
        print(f"Error: {response.status_code}")
        return None

def show_image_in_window(image):
    root = tk.Tk()
    root.title("Random meme")
    tk_image = ImageTk.PhotoImage(image)

    label = tk.Label(root, image=tk_image)
    label.pack()
    root.mainloop()

def main():
    subreddit = 'memes' 
    image_url = fetch_random_image(subreddit)
    
    if image_url:
        image = download_image(image_url)
        if image:
            show_image_in_window(image)

if __name__ == "__main__":
    main()
