import tkinter as tk
from tkinter import filedialog
from functions import combine_files
import os
import sys

def choose_file1():
    file_path = filedialog.askopenfilename(title="Select the first text file", filetypes=[("Text Files", "*.txt")])
    if file_path:
        file1_var.set(file_path)
        log_message(f"Selected File 1: {file_path}")

def choose_file2():
    file_path = filedialog.askopenfilename(title="Select the second text file", filetypes=[("Text Files", "*.txt")])
    if file_path:
        file2_var.set(file_path)
        log_message(f"Selected File 2: {file_path}")

def run_combination():
    log_message("Run button clicked")
    file1 = file1_var.get()
    file2 = file2_var.get()
    
    log_message(f"File 1: {file1}")
    log_message(f"File 2: {file2}")

    if not file1 or not file2:
        log_message("Error: You must select two text files.")
        return

    combined_content, error = combine_files(file1, file2)
    
    if error:
        log_message(f"Error: {error}")
    else:
        try:
            # Determine the base directory
            if getattr(sys, 'frozen', False):
                base_dir = os.path.dirname(sys.executable)
            else:
                base_dir = os.path.dirname(os.path.abspath(__file__))

            log_message(f"Base Directory: {base_dir}")

            output_dir = os.path.join(base_dir, "outputs")
            log_message(f"Creating output directory at {output_dir}")
            os.makedirs(output_dir, exist_ok=True)
            output_file = os.path.join(output_dir, "output.txt")

            log_message(f"Output Directory: {output_dir}")
            log_message(f"Output File: {output_file}")

            with open(output_file, 'w') as f:
                f.write(combined_content)
            log_message(f"Files combined successfully! Output saved to {output_file}")
        except Exception as e:
            log_message(f"Exception occurred: {e}")
            log_message(f"Failed to write to {output_file}")

def log_message(message):
    print(message)  # Print to console for debugging
    log_text.config(state=tk.NORMAL)
    log_text.insert(tk.END, message + "\n")
    log_text.config(state=tk.DISABLED)
    log_text.see(tk.END)

app = tk.Tk()
app.title("Text File Combiner")

file1_var = tk.StringVar()
file2_var = tk.StringVar()

tk.Label(app, text="File 1:").pack()
tk.Entry(app, textvariable=file1_var, state='readonly', width=50).pack()
tk.Button(app, text="Choose File 1", command=choose_file1).pack(pady=5)

tk.Label(app, text="File 2:").pack()
tk.Entry(app, textvariable=file2_var, state='readonly', width=50).pack()
tk.Button(app, text="Choose File 2", command=choose_file2).pack(pady=5)

tk.Button(app, text="Run", command=run_combination).pack(pady=20)

log_text = tk.Text(app, state=tk.DISABLED, height=10, width=80)
log_text.pack(pady=10)

app.mainloop()
