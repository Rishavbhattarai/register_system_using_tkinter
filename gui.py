from tkinter import *

def main_screen():
    global window
    window  = Tk()
    window.geometry("400x300")
    window.title("Account Login")

    Label(text="Choose login or register", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()

    Button(text="Login", width="300", height="2", command = login).pack()
    Label(text="").pack()
    Button(text="register", width="30", height="2" ).pack()
    Label(text="").pack()

    window.mainloop()


def login():

    login_screen = Toplevel(window)
    login_screen.title("Login")
    login_screen.geometry("400x300")
    Label(login_screen, text="please enter derails below to Login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify =StringVar()
    password_verify=StringVar()

    Label(login_screen, text="Username").pack()
    username_login_entry=Entry(login_screen,textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="Password").pack()
    password_login_entry=Entry(login_screen, textvariable=password_verify)
    password_login_entry.pack()

    Label(login_screen,text="").pack()
    b1=Button(login_screen, text="Login", height=1, width=10, command=login_verification)
    b1.pack()


    login_screen.mainloop()


main_screen()

def login_verifaction():
    print("On working")






#register()
