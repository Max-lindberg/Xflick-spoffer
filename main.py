print("                ▄▄▄▄  ▄▄   ▄▄                                                    ▄▄▄▄   ▄▄▄▄                ")
print("▀███▀   ▀██▀  ▄█▀ ▀▀▀███   ██        ▀███                                      ▄█▀ ▀▀ ▄█▀ ▀▀")
print("  ███▄  ▄█    ██▀     ██               ██                                      ██▀    ██▀")
print("   ▀██▄█▀    █████    ██ ▀███  ▄██▀██  ██  ▄██▀     ▄██▀███████████▄  ▄██▀██▄ █████  █████   ▄▄█▀██▀███▄███")
print("    ███      ██      ██   ██ ██▀  ██  ██ ▄█        ██   ▀▀ ██   ▀██ ██▀   ▀██ ██     ██    ▄█▀   ██ ██▀ ▀▀")
print("   ▄█▀▀██▄    ██      ██   ██ ██       ██▄██        ▀█████▄ ██    ██ ██     ██ ██     ██    ██▀▀▀▀▀▀ ██")
print("  ▄█   ▀██▄   ██      ██   ██ ██▄    ▄ ██ ▀██▄      █▄   ██ ██   ▄██ ██▄   ▄██ ██     ██    ██▄    ▄ ██")
print("▄██▄▄  ▄▄███▄████▄  ▄████▄████▄█████▀▄████▄ ██▄▄    ██████▀ ██████▀   ▀█████▀▄████▄ ▄████▄   ▀█████▀████▄")
print("                                                           ██")
print("                                                         ▄████▄")
key = "a"


inputkey = input("Enter your key/password: ")

if inputkey == key:
    print("Ok we will load the spoffer")
else:
    print(inputkey + " Is not a valid key")
    print("Reload program and try again.")
    quit


print("Now unlink your discord and make a new steam ac!")
print("------------------------------------------------------------------------------------------------")
print("change your fivem version to release")
print("------------------------------------------------------------------------------------------------")

import os
import tkinter as tk
from tkinter import filedialog

# Opret hovedvindue
root = tk.Tk()

# Funktion til at slette fil
def delete_file():
    selected_item = listbox.curselection()[0]  # Få den valgte fil fra listen
    file_path = listbox.get(selected_item)  # Få filstien
    os.remove(file_path)  # Slet filen
    listbox.delete(selected_item)  # Fjern filen fra listen

# Angiv stien til FiveM-mappen
fivem_path = os.path.expanduser("~") + "/AppData/Local/FiveM"

# Skift til FiveM-mappen
os.chdir(fivem_path)

# Opret liste over filer
files = os.listdir()
listbox = tk.Listbox(root)
for file in files:
    listbox.insert(tk.END, file)
listbox.pack()

# Opret knap til at slette fil
button_delete = tk.Button(root, text="Slet fil", command=delete_file)
button_delete.pack()

# Vis hovedvindue
root.mainloop()
