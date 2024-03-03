import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
import pyperclip

class MultiCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Word Counter v1.5 by @FreddyDeveloper")

        self.label = tk.Label(root, text="Enter The Text:", fg="black", bg="lightgray")
        self.label.config(font=("Helvetica", 12, "bold"))  
        self.label.pack(pady=10)

        self.text_box = tk.Text(root, height=30, width=80, fg="white", bg="blue")
        self.text_box.pack(padx=10)

        self.count_button = tk.Button(root, text="Analyze Text", command=self.count_all, fg="white", bg="green", width=15)
        self.count_button.pack(pady=5)

        self.clear_button = tk.Button(root, text="Clear Text", command=self.clear_text, fg="white", bg="blue", width=15)
        self.clear_button.pack(pady=5)

        self.result_label = tk.Label(root, text="Count: 0", fg="white", bg="red", width=100)
        self.result_label.pack(pady=10)

        self.paste_button = tk.Button(root, text="Paste Clipboard Text", command=self.paste_text, fg="white", bg="black")
        self.paste_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save As...", command=self.save_text, fg="white", bg="green", width=15)
        self.save_button.pack(pady=5)

    def count_all(self):
        text = self.text_box.get("1.0", "end-1c")
        char_count = len(text)
        self.result_label.config(text=f"Count: {char_count} characters")

    def clear_text(self):
        self.text_box.delete("1.0", "end")
        self.result_label.config(text="Count: 0 characters")

    def paste_text(self):
        clipboard_text = pyperclip.paste()
        self.text_box.delete("1.0", "end")
        self.text_box.insert("1.0", clipboard_text)
        
        text = self.text_box.get("1.0", "end-1c")
        char_count = len(text)
        self.result_label.config(text=f"Count: {char_count} characters")
		
    def save_text(self):
        text = self.text_box.get("1.0", "end-1c")
        file_types = [
            ("Python", "*.py"),
            ("PHP", "*.php"),
            ("HTML", "*.html"),
            ("Text", "*.txt"),
            ("Word Document", "*.doc"),
            ("PDF", "*.pdf"),
            ("HTAccess", ".htaccess"),
            ("SQL", "*.sql"),
        ]
        file_path = tkinter.filedialog.asksaveasfilename(filetypes=file_types, defaultextension=".txt")

        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(text)
                tkinter.messagebox.showinfo("Saved", "Text saved successfully.")
            except Exception as e:
                tkinter.messagebox.showerror("Error", f"Error saving the file: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MultiCounterApp(root)
    root.configure(bg="lightgray")
    root.mainloop()
