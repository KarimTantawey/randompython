import tkinter as tk
from tkinter import messagebox, Toplevel, Label
import requests

API_KEY = 'API KEY'

def get_recipes(ingredients):
    url = f"https://api.spoonacular.com/recipes/findByIngredients?apiKey={API_KEY}&ingredients={ingredients}&number=5"
    try:
        response = requests.get(url)
        response.raise_for_status()
        recipes = response.json()
        return recipes
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Error fetching recipes: {e}")
        return None

def get_recipe_details(recipe_id):
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        recipe_details = response.json()
        return recipe_details
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Error fetching recipe details: {e}")
        return None

def show_recipes():
    ingredients = entry_ingredients.get()
    if not ingredients:
        messagebox.showwarning("Warning", "Please enter at least one ingredient.")
        return
    
    recipes = get_recipes(ingredients)
    if recipes:
        results_box.delete('1.0', tk.END)  
        for recipe in recipes:
            title = recipe.get('title', 'No title')
            recipe_id = recipe.get('id', 'No ID')


            results_box.insert(tk.END, f"{title}\n")

            start_index = results_box.index(tk.END + "-1l linestart")
            end_index = results_box.index(tk.END + "-1l lineend")

            results_box.tag_add(f"recipe_{recipe_id}", start_index, end_index)
            results_box.tag_configure(f"recipe_{recipe_id}", foreground="blue", underline=True)
            results_box.tag_bind(f"recipe_{recipe_id}", "<Button-1>", lambda event, recipe_id=recipe_id: show_recipe_details(recipe_id))

    else:
        messagebox.showinfo("Info", "No recipes found for the given ingredients.")

def show_recipe_details(recipe_id):
    details = get_recipe_details(recipe_id)
    if details:
        details_window = Toplevel(root)
        details_window.title(details.get('title', 'Recipe Details'))

        title_label = Label(details_window, text=details.get('title', 'No title'), font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        ingredients_label = Label(details_window, text="Ingredients:", font=("Arial", 14, "bold"))
        ingredients_label.pack(pady=5)

        ingredients_text = "\n".join([ingredient['original'] for ingredient in details.get('extendedIngredients', [])])
        ingredients_box = Label(details_window, text=ingredients_text, justify="left")
        ingredients_box.pack(pady=5)

        instructions_label = Label(details_window, text="Instructions:", font=("Arial", 14, "bold"))
        instructions_label.pack(pady=5)

        instructions_text = details.get('instructions', 'No instructions available')
        instructions_box = Label(details_window, text=instructions_text, wraplength=350, justify="left")
        instructions_box.pack(pady=5)

root = tk.Tk()
root.title("Recipe Finder")
root.geometry("400x400")

label = tk.Label(root, text="Enter ingredients (comma-separated):")
label.pack(pady=10)

entry_ingredients = tk.Entry(root, width=50)
entry_ingredients.pack(pady=5)

button_search = tk.Button(root, text="Find Recipes", command=show_recipes)
button_search.pack(pady=10)

results_box = tk.Text(root, width=50, height=15, wrap=tk.WORD)
results_box.pack(pady=10)

root.mainloop()
