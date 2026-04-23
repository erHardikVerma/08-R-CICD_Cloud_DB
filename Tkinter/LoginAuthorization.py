import tkinter as tk
from tkinter import ttk, messagebox
import pymysql


def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="ebg",
    )


# Main window
root = tk.Tk()
root.title("Login and Signup")
root.geometry("400x400")




# ===== Signup/Login Tabs Syntax Start =====

tabs = ttk.Notebook(root)
tabs.pack(expand=True, fill='both')

# Signup Tab Frame
signup_frame = ttk.Frame(tabs)
tabs.add(signup_frame, text="Signup")

# Login Tab Frame
login_frame = ttk.Frame(tabs)
tabs.add(login_frame, text="Login")

# ===== Signup/Login Tabs Syntax Ends =====



# ===== Signup Tab Widgets =====
tk.Label(signup_frame, text="SignUp").place(x=150, y=20)

tk.Label(signup_frame, text="Enter your name:").place(x=30, y=50)
name = tk.Entry(signup_frame, width=25)
name.place(x=160, y=50)

tk.Label(signup_frame, text="Enter phone number:").place(x=30, y=110)
number = tk.Entry(signup_frame, width=25)
number.place(x=160, y=110)

tk.Label(signup_frame, text="Enter Email id/username:").place(x=30, y=150)
signup_username = tk.Entry(signup_frame, width=25)
signup_username.place(x=160, y=150)

tk.Label(signup_frame, text="Enter Password:").place(x=30, y=180)
signup_password = tk.Entry(signup_frame, width=25, show='*')
signup_password.place(x=160, y=180)

tk.Label(signup_frame, text="Re-enter Password:").place(x=30, y=210)
repassword = tk.Entry(signup_frame, width=25, show='*')
repassword.place(x=160, y=210)




#### ------------ login window new tab ends here (note making tab) ------- ###

def new_win():
    root1 = tk.Toplevel(root)
    root1.title("Create Note and Read Saved One's")
    root1.geometry("400x400")

    # ===== Signup/Login Tabs Syntax Start =====

    logintabs = ttk.Notebook(root1)
    logintabs.pack(expand=True, fill='both')

    # CreateNote Frame
    createnote_frame = ttk.Frame(logintabs)
    logintabs.add(createnote_frame, text="Create Note")

    # readnote Frame
    readnote_frame = ttk.Frame(logintabs)
    logintabs.add(readnote_frame, text="Read Note")

    # ===== CreateNote Tab Widgets =====
    notes_list = []  # store entered text

    tk.Label(createnote_frame, text="Create Note").place(x=150, y=20)

    tk.Label(createnote_frame, text="Enter Title:").place(x=30, y=50)
    title = tk.Entry(createnote_frame, width=25)
    title.place(x=160, y=50)

    tk.Label(createnote_frame, text="Enter Text :").place(x=30, y=80)
    text = tk.Entry(createnote_frame, width=25)
    text.place(x=160, y=80)

    def createnote_submit():
        # Append signup data to data_list
        notes_list.append({
            'title': title.get(),
            'text': text.get(),
        })
        print("Note Saved", notes_list[-1])

        # Clear entries
        title.delete(0, 'end')
        text.delete(0, 'end')

    tk.Button(createnote_frame, text="Submit", command=createnote_submit).place(x=150, y=300)

    # read text window

    def textdisplay_func():
        t = title.get()
        d = text.get()
        print(d)

    tk.Button(readnote_frame, text="View Text", command=textdisplay_func).place(x=150, y=300)


#### ------------ login window new tab ends here (note making tab) ------- ###



def signup_submit():
    signup_name = name.get().strip()
    signup_user = signup_username.get().strip()
    signup_pass = signup_password.get()

    if not signup_name or not signup_user or not signup_pass:
        messagebox.showwarning("Missing Data", "Name, username and password are required.")
        return

    # Basic validation example: check if passwords match
    if signup_pass != repassword.get():
        messagebox.showwarning("Validation Error", "Passwords do not match!")
        return

    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM userdata WHERE username = %s", (signup_user,))
            if cursor.fetchone():
                messagebox.showwarning("Duplicate User", "Username already exists.")
                return

            cursor.execute(
                """
                INSERT INTO userdata (name, username, password)
                VALUES (%s, %s, %s)
                """,
                (
                    signup_name,
                    signup_user,
                    signup_pass,
                ),
            )
        connection.commit()
        messagebox.showinfo("Success", "Signup successful and saved to database.")
    except Exception as err:
        messagebox.showerror("Database Error", f"Could not save signup: {err}")
        return
    finally:
        connection.close()

    # Clear entries
    name.delete(0, 'end')
    number.delete(0, 'end')
    signup_username.delete(0, 'end')
    signup_password.delete(0, 'end')
    repassword.delete(0, 'end')

tk.Button(signup_frame, text="Submit", command=signup_submit).place(x=150, y=300)

# ===== Login Tab Widgets and Logic =====
tk.Label(login_frame, text="Login").place(x=150, y=20)

tk.Label(login_frame, text="Enter your username:").place(x=30, y=60)
login_username = tk.Entry(login_frame, width=25)
login_username.place(x=160, y=60)

tk.Label(login_frame, text="Enter Password:").place(x=30, y=90)
login_password = tk.Entry(login_frame, width=25, show='*')
login_password.place(x=160, y=90)




def login_func():
    u = login_username.get().strip()
    p = login_password.get()

    if not u or not p:
        messagebox.showwarning("Missing Data", "Enter username and password.")
        return

    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT password FROM userdata WHERE username = %s", (u,))
            row = cursor.fetchone()

        if row and row[0] == p:
            messagebox.showinfo("Login", f"Login successful for user: {u}")
            new_win()
        else:
            messagebox.showerror("Login", "Login not successful")
    except Exception as err:
        messagebox.showerror("Database Error", f"Could not verify login: {err}")
    finally:
        connection.close()

tk.Button(login_frame, text="Login", command=login_func).place(x=150, y=300)


root.mainloop()
