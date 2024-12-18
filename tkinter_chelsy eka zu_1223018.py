import tkinter as tk
from tkinter import ttk
import time

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("300x200")

        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        # Display for the stopwatch
        self.time_display = tk.Label(root, text="00:00:00", font=("Arial", 30))
        self.time_display.pack(pady=20)

        # Start button
        self.start_button = ttk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)

        # Stop button
        self.stop_button = ttk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        # Reset button
        self.reset_button = ttk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.update_time()

    def stop(self):
        if self.running:
            self.running = False
            self.elapsed_time = time.time() - self.start_time

    def reset(self):
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.time_display.config(text="00:00:00")

    def update_time(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            minutes, seconds = divmod(int(self.elapsed_time), 60)
            hours, minutes = divmod(minutes, 60)
            time_string = f"{hours:02}:{minutes:02}:{seconds:02}"
            self.time_display.config(text=time_string)
            self.root.after(100, self.update_time)

# Create the main window
if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
