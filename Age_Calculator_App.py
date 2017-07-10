from PIL import Image, ImageTk

# use datetime object, since we can't get subtract from birthdate str format
import datetime 
import tkinter as tk

# creates tk obj from tk module
window = tk.Tk()
window.geometry("400x400")
window.title("Age Calculator App")

# adding labels
name_label =tk.Label(text="Name")
name_label.grid(column=0, row=1)

year_label = tk.Label(text="Year")
year_label.grid(column=0, row=2)

month_label = tk.Label(text="Month")
month_label.grid(column=0,row=3)

day_label = tk.Label(text="Day")
day_label.grid(column=0, row=4)




# entry is out input field where the user will type in their response

name_entry = tk.Entry()
name_entry.grid(column=1, row=1)

year_entry = tk.Entry()
year_entry.grid(column=1, row=2)

month_entry = tk.Entry()
month_entry.grid(column=1, row=3)

date_entry= tk.Entry()
date_entry.grid(column=1, row=4)

def calculate_age():
    # get the user input for the year field
    print(year_entry.get())
    print(month_entry.get())
    print(date_entry.get())
    # datetime.date object is expecting 3 args
    # create Person object then get the year, month, date field from form
    # these 3 fields are in str format bc it user input, convert to int
    person = Person(name_entry.get(), datetime.date(
                                            int(year_entry.get()),
                                            int(month_entry.get()), 
                                            int(date_entry.get())))
    print(person.age())

    # print sophie's age to window instead of printing to terminal
    # add text box on window
    text_answer = tk.Text(master=window, height=20, width=30)
    # set position of answer
    text_answer.grid(column=1, row=5)

    answer_text = "{name} is {age} years old".format(name=person.name, age=person.age())
    # insert command makes text_answer appear on window
    # END puts text towards the bottom of window
    text_answer.insert(tk.END, answer_text)

# add calculate button
# bind calculate button to calculate age function
calculate_button = tk.Button(text="Calculate Now", command=calculate_age)
calculate_button.grid(column=1, row=6)



#create Person Class

class Person:

    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def age(self):
        today = datetime.date.today()
        #(1940, 8, 20).year would return 1940
        age = today.year - self.birthdate.year
        return age

# open image and shrink to 100 x 100 and making sure not to lose resolution
image = Image.open('/Users/Home/Desktop/Create Apps OOP/cover.jpg')
image.thumbnail((100,100), Image.ANTIALIAS)
# turn image into TK image
photo = ImageTk.PhotoImage(image)
# make image label
label_image = tk.Label(image=photo)
# position label image
label_image.grid(column=1, row=0)


#(1940, 8, 20).month would return 8
Zoey = Person("Zoey", datetime.date(1940, 8, 20))
#print (Zoey.name)
#print (Zoey.birthdate)
#print(Zoey.age())

window.mainloop()

#IN SUMMARY
# 1. Make Person class (with init method, etc)
# 2. Make class method to calculate age 
# 3. Create Window
# 4. Create labels and entry field and set their position
# 5. Get values from entry field and make person object
# 6. Create a text box to print out age using str formating
# 7. Create Calculate Button and bind it to the calculate age method




