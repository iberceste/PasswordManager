from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters

    shuffle(password_list)
    password = "".join(password_list)
    pass_entry.insert(END, string=password)
    pyperclip.copy(password)

# password = ""
# for char in password_list:
#    password += char

# ---------------------------- SAVE PASSWORD ------------------------------- #


f = open("password_save.txt", "a")


def save():
    if len(web_entry.get()) == 0 or len(pass_entry.get()) == 0:
        messagebox.showerror(title="Empty entry", message=f"website or password is empty.")
    else:
        is_ok = messagebox.askokcancel(title=web_entry.get(), message=f"These are the details entered: \nEmail: {mail_entry.get()}"
                           f"\nPassword: {pass_entry.get()} \nIs it ok to save?")
        if is_ok:
            f.write("website:")
            f.write(f"{web_entry.get()}  ")
            web_entry.delete(0, END)

            f.write("email:")
            f.write(f"{mail_entry.get()}  ")

            f.write("password:")
            f.write(f"{pass_entry.get()}|  \n")
            pass_entry.delete(0, END)

        else:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=70, bg="black")


canvas = Canvas(width=200, height=200, bg="black", highlightthickness=0)
pass_photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_photo)
canvas.grid(column=1, row=0)

# Label
web_label = Label(text="Website:  ", bg="black", fg="white")
web_label.grid(row=1, column=0)

mail_label = Label(text="Email/Username:", bg="black", fg="white")
mail_label.grid(row=2, column=0)

pass_label = Label(text="Password:", bg="black", fg="white")
pass_label.grid(row=3, column=0,)

# Button
gen_button = Button(text="Generate Password:", command=generate_password)
gen_button.grid(row=3, column=2)

add_button = Button(text="Add", width=29, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# Entry

web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

mail_entry = Entry(width=35)
mail_entry.grid(row=2, column=1, columnspan=2)
mail_entry.insert(0, "ipekunlu18@gmail.com")

pass_entry = Entry(width=16)
pass_entry.grid(row=3, column=1)


window.mainloop()
f.close()
