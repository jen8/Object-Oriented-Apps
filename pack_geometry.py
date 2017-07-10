import tkinter as tk # import library

root = tk.Tk() # create window
label1 = tk.Label(root, text="BANANA") # create label
button1 = tk.Button(root, text="Button!")

label1.pack()
button1.pack()


root.mainloop() # keep window open

