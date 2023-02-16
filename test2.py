import os
import tkinter as tk
from tkinter import filedialog, messagebox

def delete_fivem():
    # Find der hvor fivem ligger
    fivem_path = filedialog.askdirectory(initialdir="C:/", title="Select your FiveM folder")
    logs = os.path.join(fivem_path, "Logs")
    digital_integration = os.path.join(fivem_path, "Digital Intelements")
    files_to_delete = [logs, digital_integration]

    # Hvilke filer der blivet slettet
    message = f"The following files will be deleted:\n\n{logs}\n{digital_integration}\n\nAre you sure you want to continue?"
    confirm = messagebox.askokcancel("Confirm Deletion", message)
    if confirm:
        # Slet filerne
        for file in files_to_delete:
            try:
                os.remove(file)
                print(f"{file} was deleted.")
            except OSError as e:
                print(f"Error deleting {file}: {e.strerror}")

# Lav et vindue
root = tk.Tk()

# Knap til at slette filerne
button = tk.Button(root, text="Delete Digital Intelements", command=delete_fivem)
button.pack()

# få vinduet fram
root.mainloop()
