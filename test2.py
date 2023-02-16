# Import required libraries
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Define function to delete files
def delete_fivem():
    # Find the path to fivem.exe
    fivem_path = filedialog.askdirectory(initialdir="C:/", title="Select your FiveM folder")
    logs = os.path.join(fivem_path, "Logs")
    digital_integration = os.path.join(fivem_path, "Digital Intelements")
    files_to_delete = [logs, digital_integration]

    # Show which files will be deleted and ask for confirmation
    message = f"The following files will be deleted:\n\n{logs}\n{digital_integration}\n\nAre you sure you want to continue?"
    confirm = messagebox.askokcancel("Confirm Deletion", message)
    if confirm:
        # Delete the files
        for file in files_to_delete:
            try:
                os.remove(file)
                print(f"{file} was deleted.")
            except OSError as e:
                print(f"Error deleting {file}: {e.strerror}")

# Create main window
root = tk.Tk()

# Create button to delete files
button = tk.Button(root, text="Delete Digital Intelements", command=delete_fivem)
button.pack()

# Show main window
root.mainloop()
