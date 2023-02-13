import tkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import random
import pyperclip
import json


#______search_____
def search():
    pass_entry.delete(0, tkinter.END)
    website = web_entry.get()
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
            if website in data:
                password = data[website]['password']
                pass_entry.insert(0, password)

            elif len(website) ==0:
                password = "Input website"
                pass_entry.insert(0, password)
            else:
                password = "Website does not exist"
                pass_entry.insert(0, password)




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def random_pass():
    pass_entry.delete(0, tkinter.END)
    # Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))] + \
                    [random.choice(symbols) for _ in range(random.randint(2, 4))] + \
                    [random.choice(numbers) for _ in range(random.randint(2, 4))]
    random.shuffle(password_list)
    password = ''.join([str(i) for i in password_list])
    pyperclip.copy(password)
    pass_entry.insert(0, str(password))


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = web_entry.get()
    email_addr = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email_addr,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Empty fields", message="fields cannot be left empty")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
        finally:
            pass_entry.delete(0, tkinter.END)
            web_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Widget Examples")
window.config(padx=70, pady=70)
# ____image_____-
canvas = Canvas(width=200, height=200)
img1 = Image.open("logo.png")
myimg = ImageTk.PhotoImage(img1)
canvas.create_image(100, 100, image=myimg)
canvas.grid(row=0, column=1, sticky=W)

# ______________________webentry__________________________________
web_entry = Entry(width=35)
web_entry.focus()
print(web_entry.get())
web_entry.grid(row=1, column=1, columnspan=2, sticky=W, padx=2, pady=2)

# _____________websitelabel___
web_label = Label()
web_label.config(text="Website:")
web_label.grid(row=1, column=0, sticky=E)

# ____emailentry_____
email_entry = Entry(width=55)
email_entry.insert(END, string="viperthereone@gmail.com")
print(email_entry.get())
email_entry.grid(row=2, column=1, sticky=W, columnspan=2, padx=2, pady=2)

# _____________emaillabel___
email_label = Label()
email_label.config(text="Email/Username:")
email_label.grid(row=2, column=0)

# ____passwordentry_____
pass_entry = Entry(width=35)
print(pass_entry.get())
pass_entry.grid(row=3, column=1, sticky=W, padx=2, pady=2)

# _____________passwordlabel_______________
password_label = Label()
password_label.config(text="Password:")
password_label.grid(row=3, column=0, sticky=E)

# _____generbutton____
pass_button = Button(width=17)
pass_button.config(text="Generate Password", font=("Arial", 8, "normal"), command=random_pass)
pass_button.grid(row=3, column=2, sticky=E, columnspan=2, padx=2, pady=2)

# _____addbutton____
add_button = Button(width=54)
add_button.config(text="add", font=("Arial", 8, "normal"), command=save_pass)
add_button.grid(row=4, column=1, sticky=W, columnspan=2, padx=2, pady=2)


#_____searchbuttopn____
add_button = Button(width=17)
add_button.config(text="Search", font=("Arial", 8, "normal"), command=search)
add_button.grid(row=1, column=2, sticky=W, columnspan=2, padx=2, pady=2)


window.mainloop()
