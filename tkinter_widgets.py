import tkinter as tk

# root window
parent = tk.Tk()

# tk.WidgetName(parent_frame, options)

# parent paramter is telling tkinter to put this entry field in window
tk.Entry(parent, width=25).pack()
tk.Button(parent, text="LOOKOUT!").pack()
tk.Checkbutton(parent, text='RememberMe', variable=tk.IntVar()).pack()
tk.Label(parent, text="What's Your Name?").pack()
tk.OptionMenu(parent, tk.IntVar(), "Select Age", "15+", "25+", "40+", "60+").pack()
tk.Scrollbar(parent, orient=tk.VERTICAL).pack()
tk.Radiobutton(parent, text='Democratic', variable=tk.IntVar(), value=3).pack()
tk.Radiobutton(parent, text='Republican', variable=tk.IntVar(), value=5).pack()


parent.mainloop()



 
 # wyzant - profiles for what you can teach, will find clients for you
 # takelessons -