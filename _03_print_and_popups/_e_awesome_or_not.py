from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    num = random.randint(0, 3)
    # 2. Print your variable to the console
    print(num)
    # 3. Get the user to enter something that they think is awesome
    awesome = simpledialog.askstring(None, "Enter something that you think is awesome")
    # 4. If your variable is  0
    if num == 0:
        # -- tell the user whatever they entered is awesome!
        messagebox.showinfo(None, awesome + " is awesome")
    # 5. If your variable is  1
    if num == 1:
        # -- tell the user whatever they entered is ok.
        messagebox.showinfo(None, awesome + " is okay")
    
    # 6. If your variable is  2
    if num == 2:
        # -- tell the user whatever they entered is boring.
        messagebox.showinfo(None, awesome + " is boring")
    # 7. If your variable is  3
    if num == 3:
        # -- invent your own message to give to the user (be nice).
        messagebox.showinfo(None, "error, cannot compute")
    # Run the window's .mainloop() method
    window.mainloop()