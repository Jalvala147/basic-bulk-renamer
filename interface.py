import customtkinter as ctk
from tkinter import messagebox, filedialog
from rename import rename_files

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_entry.delete(0, ctk.END)
        folder_entry.insert(0, folder_path)

def rename():
    folder_path = folder_entry.get()
    new_name = name_entry.get().strip()
    extension = extension_entry.get().strip()

    if not folder_path or not new_name:
        messagebox.showerror("Error", "Please select a folder and enter a new name.")
        return

    if extension and not extension.startswith('.'):
        extension = '.' + extension

    try:
        renamed_files = rename_files(folder_path, new_name, extension)
        messagebox.showinfo("Success", f"Renamed {renamed_files} files.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


ctk.set_appearance_mode("system")  
ctk.set_default_color_theme("dark-blue")  

window = ctk.CTk()
window.title("✨ Bulk File Renamer ✨")
window.geometry("700x300")
window.resizable(False, False)


title_label = ctk.CTkLabel(window, text="Bulk File Renamer", font=ctk.CTkFont(size=18, weight="bold"))
title_label.pack(pady=15)


frame = ctk.CTkFrame(window, fg_color="transparent")
frame.pack(padx=20, pady=10, fill="x")


folder_label = ctk.CTkLabel(frame, text="📁 Folder:")
folder_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)
folder_entry = ctk.CTkEntry(frame, width=300)
folder_entry.grid(row=0, column=1, padx=5, pady=5)
browse_button = ctk.CTkButton(frame, text="Browse", command=select_folder)
browse_button.grid(row=0, column=2, padx=5, pady=5)


name_label = ctk.CTkLabel(frame, text="📝 New Name:")
name_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
name_entry = ctk.CTkEntry(frame, width=300)
name_entry.grid(row=1, column=1, columnspan=2, sticky="we", padx=5, pady=5)


ext_label = ctk.CTkLabel(frame, text="📄 Extension (optional):")
ext_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
extension_entry = ctk.CTkEntry(frame, width=300)
extension_entry.grid(row=2, column=1, columnspan=2, sticky="we", padx=5, pady=5)


rename_button = ctk.CTkButton(window, text="🔁 Rename Files", command=rename)
rename_button.pack(pady=20, ipadx=10, ipady=5)

window.mainloop()
