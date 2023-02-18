import tkinter as tk
from tkinter import filedialog
import os

# Opret hovedvindue
root = tk.Tk()

# Funktion til at åbne filbrowser
def open_file_browser():
    # Vælg mappe
    global start_dir
    start_dir = filedialog.askdirectory(initialdir=start_dir)
    path_label.config(text="Slet filer i: " + start_dir)

# Funktion til at slette filer
def delete_files():
    # Få søgeterm fra brugerinput
    search_term = search_entry.get()

    # Opret liste over filer, der skal slettes
    files_to_delete = []
    for root_dir, subdirs, files in os.walk(start_dir):
        for file in files:
            if search_term in file:
                files_to_delete.append(os.path.join(root_dir, file))

    # Vis liste over filer, der skal slettes
    confirm_message = "Følgende filer vil blive slettet:\n\n"
    for file in files_to_delete:
        confirm_message += file + "\n"
    confirm_message += "\nEr du sikker på, at du vil fortsætte?"
    if tk.messagebox.askyesno(title="Bekræft sletning", message=confirm_message):
        # Slet filer
        for file in files_to_delete:
            os.remove(file)
        tk.messagebox.showinfo(title="Sletning fuldført", message="Filerne blev slettet.")

# Opret label til at vise sti
start_dir = "C:/"
path_label = tk.Label(root, text="Slet filer i: " + start_dir)
path_label.pack()

# Opret knap til at åbne filbrowser
browse_button = tk.Button(root, text="Vælg sti", command=open_file_browser)
browse_button.pack()

# Opret label og entry til søgeterm
search_label = tk.Label(root, text="Søg efter filer, der indeholder:")
search_label.pack()
search_entry = tk.Entry(root)
search_entry.pack()

# Opret knap til at slette filer
delete_button = tk.Button(root, text="Slet filer", command=delete_files)
delete_button.pack()

# Vis hovedvindue
root.mainloop()
#I will finish it in 3 days
