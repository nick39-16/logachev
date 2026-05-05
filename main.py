import tkinter as tk
import requests
import json

# Поиск пользователя
def search_user():
    username = entry.get()
    if not username:
        result_label.config(text="Введите логин!")
        return
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code == 200:
        user = response.json()
        result_label.config(text=f"{user['login']} - {user['html_url']}")
    else:
        result_label.config(text="Пользователь не найден")

# Добавление в избранное
def add_to_favorites(user):
    try:
        with open("favorites.json", "r") as f:
            favorites = json.load(f)
    except FileNotFoundError:
        favorites = []
    favorites.append(user)
    with open("favorites.json", "w") as f:
        json.dump(favorites, f)

# GUI
root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
btn_search = tk.Button(root, text="Поиск", command=search_user)
btn_search.pack()
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()
