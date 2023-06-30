import tkinter as tk
import time

def update_clock():
    current_time = time.strftime( '%H:%M:%S %a' )
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

# Create a main windows
windows = tk.Tk()
windows.title("Digital Clock")

#Create a label to display the clock
clock_label = tk.Label(windows, font=('Arial', 80))
clock_label.pack(padx=20, pady=20)

#update the clock initially
update_clock()

#start the Tkinter event loop
windows.mainloop()