import tkinter.ttk
import pandas
from datetime import *
from tkinter import *
from tkinter import messagebox
import os.path
from password_generator import generate
import pyperclip

# GLOBALS
WHITE = "#ffffff"
BLACK = "#000000"
MY_FONT = ("Courier", 10)
filename = "passwords.csv"
if os.path.exists(filename):
    my_dataframe_old = pandas.read_csv(filename)
current_time = datetime.now()
email_selection_values = ('email1@yahoo.com', 'email2@gmail.com', 'email3@cybergeek.com')
date = current_time.strftime('%m_%d_%Y')
pandas.set_option('display.max_columns', None)
pandas.set_option('display.max_rows', None)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_a_password():
    password_result = generate()
    password_input.delete(0, END)
    password_input.insert(0, password_result)
    # copy the password_result into the buffer, so you can paste anywhere using [CTRL] + "V"
    pyperclip.copy(password_result)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    my_dataframe_new = pandas.DataFrame(columns=['WEBSITE', 'ACCOUNT', 'EMAIL/USERID', 'PASSWORD', 'DATE'])
    my_dataframe_new['WEBSITE'] = [website_input.get()]
    my_dataframe_new['ACCOUNT'] = [account_input.get()]
    my_dataframe_new['EMAIL/USERID'] = [email_selection.get()]
    my_dataframe_new['PASSWORD'] = [password_input.get()]
    my_dataframe_new['DATE'] = [date]

    # make sure website and account and password is not empty
    if (len(website_input.get()) == 0 or len(account_input.get()) == 0) or len(password_input.get()) == 0:
        messagebox.showinfo(title="Empty Field(s) Detected",
                            message="Please make sure you haven't left any fields empty\n\n"
                                    "website and account,\npassword")
    else:
        # show a pop-up to check if information is correct
        result = messagebox.askokcancel(title=website_input.get(),
                                        message=f"Are the account details Correct? \n\n"
                                                f"ACCOUNT: {account_input.get()}\n"
                                                f"EMAIL/USERID: {email_selection.get()}\n"
                                                f"PASSWORD: {password_input.get()}")
        if result is True:
            if os.path.exists(filename):
                merged = my_dataframe_new.append(my_dataframe_old, ignore_index=True)
                merged = merged.sort_values(by=['WEBSITE'], ascending=True)
                merged.to_csv(filename, index=False)
            else:
                my_dataframe_new.to_csv(filename, index=False)
            os.system(f"start EXCEL.EXE {filename}")

            # Clear values of each input
            website_input.delete(0, END)
            account_input.delete(0, END)
            email_selection.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg=WHITE)
lock_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:", fg=BLACK, bg=WHITE, font=MY_FONT)
website_label.grid(column=0, row=1)
user_label = Label(text="Email/Username:", fg=BLACK, bg=WHITE, font=MY_FONT)
user_label.grid(column=0, row=2)
account_label = Label(text="Account:", fg=BLACK, bg=WHITE, font=MY_FONT)
account_label.grid(column=0, row=3)
password_label = Label(text="Password:", fg=BLACK, bg=WHITE, font=MY_FONT)
password_label.grid(column=0, row=4)

# entries
website_input = Entry(width=35)
website_input.insert(END, string="")
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
email_selection = tkinter.ttk.Combobox(width=35, values=email_selection_values)
email_selection.grid(column=1, row=2, columnspan=2)
account_input = Entry(width=21)
account_input.grid(column=1, row=3)
password_input = Entry(width=21)
password_input.insert(END, string="")
password_input.grid(column=1, row=4)

# buttons
generate_pw = Button(text="Generate Password", highlightthickness=0, command=generate_a_password)
generate_pw.grid(column=2, row=4)
add = Button(text="Add", width=36, highlightthickness=0, command=save)
add.grid(column=1, row=5, columnspan=2)
window.mainloop()
