import tkinter as tk
from tkinter import filedialog, messagebox
import os
import re
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class FileNameReplacer:
    def __init__(self, master):
        self.master = master
        master.title("File Name Replacer")
        master.geometry("600x550")

        # Style
        self.style = ttk.Style(theme='flatly')

        # Variables
        self.folder_path = tk.StringVar()
        self.search_string = tk.StringVar()
        self.replace_string = tk.StringVar()
        self.use_regex = tk.BooleanVar(value=False)
        self.case_sensitive = tk.BooleanVar(value=True)
        self.recursive = tk.BooleanVar(value=True)

        # Folder Selection
        ttk.Label(master, text="Folder:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        ttk.Entry(master, textvariable=self.folder_path, width=50).grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        ttk.Button(master, text="Browse", command=self.browse_folder).grid(row=0, column=2, padx=10, pady=5, sticky=tk.W)

        # Search and Replace Strings
        ttk.Label(master, text="Search String:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        ttk.Entry(master, textvariable=self.search_string, width=50).grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        ttk.Label(master, text="Replace String:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        ttk.Entry(master, textvariable=self.replace_string, width=50).grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

        # Options
        ttk.Checkbutton(master, text="Use Regular Expression", variable=self.use_regex).grid(row=3, column=0, columnspan=3, padx=10, pady=5, sticky=tk.W)
        ttk.Checkbutton(master, text="Case Sensitive", variable=self.case_sensitive).grid(row=4, column=0, columnspan=3, padx=10, pady=5, sticky=tk.W)
        ttk.Checkbutton(master, text="Recursive Search", variable=self.recursive).grid(row=5, column=0, columnspan=3, padx=10, pady=5, sticky=tk.W)

        # Buttons
        ttk.Button(master, text="Preview", command=self.preview, bootstyle=PRIMARY).grid(row=6, column=0, columnspan=3, padx=10, pady=10)
        ttk.Button(master, text="Replace Files", command=self.replace_files, bootstyle=SUCCESS).grid(row=7, column=0, columnspan=3, padx=10, pady=10)

        # Preview Listbox
        self.listbox_preview = tk.Listbox(master, width=70, height=8)
        self.listbox_preview.grid(row=8, column=0, columnspan=3, padx=10, pady=5)

        # Status and Progress Bar
        self.status_label = ttk.Label(master, text="")
        self.status_label.grid(row=9, column=0, columnspan=3, padx=10, pady=5, sticky=tk.W)

        self.progressbar = ttk.Progressbar(master, orient=tk.HORIZONTAL, length=550, mode='determinate')
        self.progressbar.grid(row=10, column=0, columnspan=3, padx=10, pady=5)

    def browse_folder(self):
        """Open folder selection dialog"""
        folder_path = filedialog.askdirectory()
        self.folder_path.set(folder_path)

    def preview(self):
        """Preview file name changes"""
        folder_path = self.folder_path.get()
        search_string = self.search_string.get()
        replace_string = self.replace_string.get()
        use_regex = self.use_regex.get()
        case_sensitive = self.case_sensitive.get()
        recursive = self.recursive.get()

        if not folder_path:
            messagebox.showerror("Error", "Please select a folder.")
            return

        self.listbox_preview.delete(0, tk.END)
        files = self.get_files(folder_path, recursive)
        for file_path in files:
            original_name = os.path.basename(file_path)
            if use_regex:
                if case_sensitive:
                    new_name = re.sub(search_string, replace_string, original_name)
                else:
                    new_name = re.sub(search_string, replace_string, original_name, flags=re.IGNORECASE)
            else:
                if case_sensitive:
                    new_name = original_name.replace(search_string, replace_string)
                else:
                    new_name = original_name.lower().replace(search_string.lower(), replace_string)
            self.listbox_preview.insert(tk.END, f"{original_name} -> {new_name}")

    def replace_files(self):
        """Replace file names"""
        folder_path = self.folder_path.get()
        search_string = self.search_string.get()
        replace_string = self.replace_string.get()
        use_regex = self.use_regex.get()
        case_sensitive = self.case_sensitive.get()
        recursive = self.recursive.get()

        if not folder_path:
            messagebox.showerror("Error", "Please select a folder.")
            return

        files = self.get_files(folder_path, recursive)
        total_files = len(files)
        self.progressbar["maximum"] = total_files
        self.progressbar["value"] = 0

        for i, file_path in enumerate(files):
            try:
                dir_name = os.path.dirname(file_path)
                original_name = os.path.basename(file_path)
                if use_regex:
                    if case_sensitive:
                        new_name = re.sub(search_string, replace_string, original_name)
                    else:
                        new_name = re.sub(search_string, replace_string, original_name, flags=re.IGNORECASE)
                else:
                    if case_sensitive:
                        new_name = original_name.replace(search_string, replace_string)
                    else:
                        new_name = original_name.lower().replace(search_string.lower(), replace_string)
                new_path = os.path.join(dir_name, new_name)

                if original_name != new_name:
                    os.rename(file_path, new_path)
                    self.status_label.config(text=f"Replaced: {original_name} -> {new_name}")
                else:
                    self.status_label.config(text=f"No change: {original_name}")

                self.progressbar["value"] = i + 1
                self.master.update_idletasks()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to replace file {file_path}: {str(e)}")
                self.status_label.config(text=f"Error: {original_name}")
                break

        self.status_label.config(text="Completed")
        messagebox.showinfo("Completed", "File name replacement completed.")

    def get_files(self, folder_path, recursive):
        """Get files in folder recursively"""
        files = []
        if recursive:
            for root, _, filenames in os.walk(folder_path):
                for filename in filenames:
                    files.append(os.path.join(root, filename))
        else:
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                if os.path.isfile(file_path):
                    files.append(file_path)
        return files

if __name__ == "__main__":
    root = ttk.Window(themename="flatly")
    replacer = FileNameReplacer(root)
    root.mainloop()
