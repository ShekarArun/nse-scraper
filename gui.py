import tkinter as tk
from tkinter import ttk, filedialog
from threading import Thread
from storeData import DataCollector
import os


class DataCollectorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("NSE Data Collector")
        self.root.geometry("600x400")
        self.collector = DataCollector()
        self.collection_thread = None

        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # File selection frame
        file_frame = ttk.LabelFrame(
            main_frame, text="Output File Selection", padding="5")
        file_frame.grid(row=0, column=0, columnspan=2,
                        sticky=(tk.W, tk.E), pady=5)

        self.file_path = tk.StringVar(value="underlyings.csv")
        self.file_entry = ttk.Entry(
            file_frame, textvariable=self.file_path, width=50)
        self.file_entry.grid(row=0, column=0, padx=5)

        browse_btn = ttk.Button(
            file_frame, text="Browse", command=self.browse_file)
        browse_btn.grid(row=0, column=1, padx=5)

        # Control buttons
        self.start_btn = ttk.Button(
            main_frame, text="Start Collection", command=self.start_collection)
        self.start_btn.grid(row=1, column=0, pady=10)

        self.stop_btn = ttk.Button(
            main_frame, text="Stop Collection", command=self.stop_collection, state=tk.DISABLED)
        self.stop_btn.grid(row=1, column=1, pady=10)

        # Status frame
        status_frame = ttk.LabelFrame(main_frame, text="Status", padding="5")
        status_frame.grid(row=2, column=0, columnspan=2,
                          sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)

        # Add text widget for logging
        self.log_text = tk.Text(status_frame, height=15, width=60)
        self.log_text.grid(row=0, column=0, padx=5, pady=5)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(
            status_frame, orient=tk.VERTICAL, command=self.log_text.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.log_text.configure(yscrollcommand=scrollbar.set)

        # Redirect print statements to the text widget
        import sys
        sys.stdout = self

    def write(self, text):
        self.log_text.insert(tk.END, text)
        self.log_text.see(tk.END)
        self.root.update_idletasks()

    def flush(self):
        pass

    def browse_file(self):
        initial_dir = os.path.dirname(self.file_path.get()) or os.getcwd()
        filename = filedialog.asksaveasfilename(
            initialdir=initial_dir,
            title="Select Output File",
            filetypes=(("CSV files", "*.csv"), ("All files", "*.*")),
            defaultextension=".csv"
        )
        if filename:
            self.file_path.set(filename)

    def start_collection(self):
        self.collector.set_output_file(self.file_path.get())
        self.collection_thread = Thread(
            target=self.collector.start_collection, daemon=True)
        self.collection_thread.start()

        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.file_entry.config(state=tk.DISABLED)

    def stop_collection(self):
        self.collector.stop_collection()
        if self.collection_thread:
            self.collection_thread.join(timeout=2)

        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.file_entry.config(state=tk.NORMAL)


def main():
    root = tk.Tk()
    app = DataCollectorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
