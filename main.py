import os
import tkinter as tk
from tkinter import filedialog
import time



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

keylist = ["t9R#x8uKp$z%Y5", "7jL@vPmN&c2Q*H", "s6G$bDf3nE!wA4", "F8#yMhT%Zx9k1U", "qW@pXoRm7V*JlI", "e2C$dSjN&g5BtK", "6iA!kOwYf#G4xL", "b1U@2JyH9q3MvP", "V$rS0nT7zFt@Ll", "h5N#fXc9B!sWd8", "a4Z*mPwJ@u&yK7", "Q8@8HbU9gNt1Ei", "2rC#kLl3nWfV7I", "D$pRt@hXm6yGxK", "g1A&fYlN5zW!oB", "root"]

inputkey = input("Enter your key/password: ")

if inputkey == keylist[0] or [1] or [2] or [3] or [4]:
    print("Ok we will load the spoffer")
else:
    print(inputkey + " Is not a valid key")
    print("Reload program and try again.")
    quit

time.sleep(5)

print("Delelte Digital Intelements!")

time.sleep(5)

# Opret hovedvindue
root = tk.Tk()

# Funktion til at slette fil
def delete_file():
    selected_item = listbox.curselection()[0]  # Få den valgte fil fra listen
    file_path = listbox.get(selected_item)  # Få filstien
    os.remove(file_path)  # Slet filen
    listbox.delete(selected_item)  # Fjern filen fra listen

# Angiv stien til FiveM-mappen
fivem_path = os.path.expanduser("~") + "\AppData\Local\FiveM\FiveM.app"

try:
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

except FileNotFoundError:
    # Vis en fejlmeddelelse, hvis FiveM-mappen ikke kunne findes
    tk.messagebox.showerror("Fejl", "Could not find your fivem...")

# Vis hovedvindue
root.mainloop()

print("Now unlink your discord and make a new steam ac!")
print("------------------------------------------------------------------------------------------------")
print("change your fivem version to release")
print("------------------------------------------------------------------------------------------------")

time.sleep(5)
print("")
print("")
print("")
print("")
print("Delete Logs Folder!")
print("------------------------------------------------------------------------------------------------")



# Opret hovedvindue
root = tk.Tk()

# Funktion til at slette fil
def delete_file():
    selected_item = listbox.curselection()[0]  # Få den valgte fil fra listen
    file_path = listbox.get(selected_item)  # Få filstien
    os.remove(file_path)  # Slet filen
    listbox.delete(selected_item)  # Fjern filen fra listen

# Angiv stien til FiveM-mappen
fivem_path = os.path.expanduser("~") + "\AppData\Local\FiveM\FiveM.app"

try:
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

except FileNotFoundError:
    # Vis en fejlmeddelelse, hvis FiveM-mappen ikke kunne findes
    tk.messagebox.showerror("Fejl", "Could not find your fivem...")

# Vis hovedvindue
root.mainloop()





