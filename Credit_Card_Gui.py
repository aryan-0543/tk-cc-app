import tkinter as tk
import sqlite3
from tkinter import messagebox


class WelcomePage:
    def __init__(self, master, db_connection):
        self.master = master
        self.db_connection = db_connection
        master.title("Welcome")
        master.geometry("600x400")
        master.configure(bg="#023047")  # Set background color to a shade of blue

        self.label_welcome = tk.Label(master, text="Welcome to Our App", font=("Arial", 24), fg="white", bg="#023047")
        self.label_welcome.pack(pady=20)

        self.button_create_account = tk.Button(master, text="Create New Account", command=self.open_create_account, bg="#fb8500", fg="black")
        self.button_create_account.pack(pady=10)

        self.button_login = tk.Button(master, text="Login", command=self.open_login, bg="#2ec4b6", fg="black")
        self.button_login.pack(pady=10)

        self.button_quit = tk.Button(master, text="Quit", command=self.quit, bg="#f4a261", fg="black")
        self.button_quit.pack(pady=10)

    def open_create_account(self):
        self.master.withdraw()  # Hide the WelcomePage window
        create_account_window = tk.Toplevel(self.master)  # Create a new window for the CreateAccountPage
        app = CreateAccountPage(create_account_window, self.db_connection)  # Pass the database connection

    def open_login(self):
        self.master.withdraw()  # Hide the WelcomePage window
        login_window = tk.Toplevel(self.master)  # Create a new window for the LoginPage
        app = LoginApp(login_window, self.db_connection)  # Pass the database connection

    def quit(self):
        self.master.destroy()



class CreateAccountPage:
    def __init__(self, master, db_connection):
        self.master = master
        self.db_connection = db_connection
        master.title("Create New Account")
        master.configure(bg="#023047")  # Set background color to a shade of blue

        # Set fixed window size
        master.geometry("600x400")

        # Set column and row configurations to fix size
        for i in range(3):
            master.grid_columnconfigure(i, weight=1, minsize=200)
        for i in range(7):
            master.grid_rowconfigure(i, weight=1, minsize=40)

        self.label_title = tk.Label(master, text="Create New Account", font=("Arial", 24), fg="white", bg="#023047")
        self.label_title.grid(row=0, column=0, columnspan=3, pady=20)

        self.labels = ["First Name:", "Last Name:", "Date of Birth:", "Username:", "Password:", "Mobile No."]
        self.entries = []

        for i, label_text in enumerate(self.labels):
            label = tk.Label(master, text=label_text, bg="#023047", fg="white")
            label.grid(row=i+1, column=0, padx=20, pady=5, sticky="e")
            entry = tk.Entry(master, width=30)  # Set fixed width
            entry.grid(row=i+1, column=1, padx=20, pady=5, sticky="ew")
            self.entries.append(entry)

        self.button_create = tk.Button(master, text="Create Account", command=self.create_account, bg="#fb8500", fg="black")
        self.button_create.grid(row=7, column=0, columnspan=3, pady=10)

        self.button_back = tk.Button(master, text="Back", command=self.back, bg="#f4a261", fg="black")
        self.button_back.grid(row=8, column=0, columnspan=3, pady=10)

    def create_account(self):
        # Retrieve data from entry widgets
        data = [entry.get() for entry in self.entries]
        first_name, last_name, dob, username, password, mobile = data

        try:
            # Insert data into the database
            cursor = self.db_connection.cursor()
            cursor.execute("INSERT INTO Users (first_name, last_name, dob, username, password, mobile) VALUES (?, ?, ?, ?, ?, ?)",
                        (first_name, last_name, dob, username, password, mobile))
            self.db_connection.commit()
            messagebox.showinfo("Account Created", "Account successfully created!")
            
            # Withdraw/hide the current window
            self.master.withdraw()

            # Create a new instance of the welcome page
            welcome_page = WelcomePage(tk.Toplevel(), self.db_connection)

        except Exception as e:
            messagebox.showerror("Error", str(e))


    def back(self):
        self.master.withdraw()  # Hide the CreateAccountPage window
        welcome_window = tk.Toplevel(self.master)  # Create a new window for the WelcomePage
        app = WelcomePage(welcome_window, self.db_connection)  # Pass the database connection

class LoginApp:
    def __init__(self, master, db_connection):
        self.master = master
        self.db_connection = db_connection
        master.title("Login")
        master.configure(bg="#023047")  # Set background color to a shade of blue

        # Set fixed window size
        master.geometry("300x200")

        # Set column and row configurations to fix size
        for i in range(2):
            master.grid_columnconfigure(i, weight=1, minsize=100)
        for i in range(4):
            master.grid_rowconfigure(i, weight=1, minsize=40)

        # Center the window on the screen
        window_width = 300
        window_height = 200
        position_right = int(master.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(master.winfo_screenheight() / 2 - window_height / 2)
        master.geometry(f"300x200+{position_right}+{position_down}")

        self.label_login = tk.Label(master, text="Login", font=("Arial", 16), bg="#023047", fg="white")
        self.label_login.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        self.label_username = tk.Label(master, text="Username:", bg="#023047", fg="white")
        self.label_username.grid(row=1, column=0, padx=10, pady=5, sticky='e')

        self.entry_username = tk.Entry(master, width=20)  # Set fixed width
        self.entry_username.grid(row=1, column=1, padx=10, pady=5)

        self.label_password = tk.Label(master, text="Password:", bg="#023047", fg="white")
        self.label_password.grid(row=2, column=0, padx=10, pady=5, sticky='e')

        self.entry_password = tk.Entry(master, show="*", width=20)  # Set fixed width
        self.entry_password.grid(row=2, column=1, padx=10, pady=5)

        self.button_login = tk.Button(master, text="Login", command=self.login, bg="#fb8500", fg="black")
        self.button_login.grid(row=3, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM USERS WHERE username=? AND password=?", (username, password))
            user = cursor.fetchone()

            if user:
                messagebox.showinfo("Login Successful", "Welcome back, " + username + "!")
                self.open_main_app()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")

        except sqlite3.Error as e:
            messagebox.showerror("Error", str(e))

    def open_main_app(self):
        self.master.withdraw()

        # Open the main menu window as a Toplevel window
        main_menu_window = tk.Toplevel(self.master)

        # Create an instance of the MainMenu class and pass the database connection
        main_menu = MainMenu(main_menu_window, self.db_connection)




class MainMenu:
    def __init__(self, master, db_connection):
        self.master = master
        master.title("Main Menu")
        self.db_connection = db_connection
        

        # Set background color
        master.configure(bg="#023047")

        master.geometry("600x400")

        # Add heading label
        self.label_heading = tk.Label(master, text="Main Menu", font=("Arial", 24), fg="white", bg="#023047")
        self.label_heading.pack(pady=20)

        # Create buttons for various actions with specified colors
        self.button_new_user = tk.Button(master, text="Create New User", command=self.create_new_user, bg="#fb8500", fg="black")
        self.button_new_user.pack(pady=10)

        self.button_new_credit_card = tk.Button(master, text="New Credit Card", command=self.new_credit_card, bg="#2ec4b6", fg="black")
        self.button_new_credit_card.pack(pady=10)

        self.button_set_limit = tk.Button(master, text="Set Limit", command=self.set_limit, bg="#023047", fg="black")
        self.button_set_limit.pack(pady=10)

        self.button_set_application = tk.Button(master, text="Set Application", command=self.set_application, bg="#023047", fg="black")
        self.button_set_application.pack(pady=10)

        self.button_create_branch = tk.Button(master, text="Create New Branch", command=self.create_new_branch, bg="#f4a261", fg="black")
        self.button_create_branch.pack(pady=10)

        # Create "View All" button
        self.btn_view_all = tk.Button(master, text="View All", command=self.view_all_data)
        self.btn_view_all.pack()
        

        # Create a Text widget to display the data
        self.text_view_all = tk.Text(self.master, height=20, width=100)
        self.text_view_all.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    def view_all_data(self):
        try:
            # Clear previous data
            self.text_view_all.delete(1.0, tk.END)

            # Fetch data from each table
            cursor = self.db_connection.cursor()

            cursor.execute("SELECT * FROM BRANCH")
            branch_data = cursor.fetchall()

            cursor.execute("SELECT * FROM USER1")
            user_data = cursor.fetchall()

            cursor.execute("SELECT * FROM CREDIT_CARD")
            credit_card_data = cursor.fetchall()

            cursor.execute("SELECT * FROM LIMITS")
            limits_data = cursor.fetchall()

            cursor.execute("SELECT * FROM APPLICATIONS")
            applications_data = cursor.fetchall()

            # Display data in the Text widget
            self.text_view_all.insert(tk.END, "Branch Data:\n")
            for row in branch_data:
                self.text_view_all.insert(tk.END, f"{row}\n")

            self.text_view_all.insert(tk.END, "\nUser Data:\n")
            for row in user_data:
                self.text_view_all.insert(tk.END, f"{row}\n")

            self.text_view_all.insert(tk.END, "\nCredit Card Data:\n")
            for row in credit_card_data:
                self.text_view_all.insert(tk.END, f"{row}\n")

            self.text_view_all.insert(tk.END, "\nLimits Data:\n")
            for row in limits_data:
                self.text_view_all.insert(tk.END, f"{row}\n")

            self.text_view_all.insert(tk.END, "\nApplications Data:\n")
            for row in applications_data:
                self.text_view_all.insert(tk.END, f"{row}\n")

        except sqlite3.Error as e:
            messagebox.showerror("Error", str(e))




    def create_new_user(self):
        self.master.withdraw()  # Hide the current window
        new_user_window = tk.Toplevel()
        app = USER1(new_user_window,self.db_connection)  # Assuming your new user window class is named NewUserWindow

    def new_credit_card(self):
        self.master.withdraw()  # Hide the current window
        new_credit_card_window = tk.Toplevel()
        app = CREDIT_CARD(new_credit_card_window,self.db_connection)  # Assuming your credit card window class is named NewCreditCardWindow

    def set_limit(self):
        self.master.withdraw()  # Hide the current window
        set_limit_window = tk.Toplevel()
        app = LIMITS(set_limit_window,self.db_connection)  # Assuming your set limit window class is named SetLimitWindow

    def set_application(self):
        self.master.withdraw()  # Hide the current window
        set_application_window = tk.Toplevel()
        app = APPLICATIONS(set_application_window,self.db_connection)  # Assuming your set application window class is named SetApplicationWindow

    def create_new_branch(self):
        self.master.withdraw()  # Hide the current window
        new_branch_window = tk.Toplevel()
        app = BRANCH(new_branch_window,self.db_connection)  # Assuming your new branch window class is named NewBranchWindow

def create_tables(db_connection):
    cursor = db_connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS USERS (
            user_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            dob DATE NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            mobile INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS USER1 (
            user_id INTEGER PRIMARY KEY,
            user_name TEXT NOT NULL,
            user_mob INTEGER NOT NULL,
            user_mail TEXT NOT NULL,
            user_address TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CREDIT_CARD (
            crc_id INTEGER PRIMARY KEY,
            crc_name TEXT NOT NULL,
            crc_bal INTEGER NOT NULL,
            crc_type TEXT NOT NULL,
            crc_user_id INTEGER NOT NULL,
            FOREIGN KEY (crc_user_id) REFERENCES USER1(user_id) ON DELETE CASCADE ON UPDATE CASCADE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS LIMITS (
            limit_user_id INTEGER PRIMARY KEY,
            limit_bal INTEGER NOT NULL,
            limit_crc_id INTEGER NOT NULL,
            FOREIGN KEY (limit_crc_id) REFERENCES CREDIT_CARD(crc_id) ON DELETE CASCADE ON UPDATE CASCADE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS BRANCH (
            branch_id INT PRIMARY KEY,
            branch_name CHAR(20) NOT NULL,
            branch_address CHAR(25) NOT NULL,
            branch_manager CHAR(25) NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS APPLICATIONs (
            app_num INTEGER PRIMARY KEY,
            app_user_id INTEGER NOT NULL,
            app_type TEXT NOT NULL,
            FOREIGN KEY (app_user_id) REFERENCES USER1(user_id) ON DELETE CASCADE ON UPDATE CASCADE
        )
    """)

    # Commit the changes and close the cursor
    db_connection.commit()
    cursor.close()

class USER1:
    def __init__(self, master, db_connection):
        self.master = master
        self.db_connection = db_connection
        self.c = self.db_connection.cursor()
        master.title("New User")
        master.geometry("400x400")
        master.configure(bg="#023047")  # Set background color

        # Labels and entry fields for user attributes
        labels = ["User ID:", "User Name:", "Mobile:", "Email:", "Address:"]
        self.entries = []
        for i, label_text in enumerate(labels):
            label = tk.Label(master, text=label_text, bg="#023047", fg="white")
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(master, width=30)  # Set fixed width
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            self.entries.append(entry)

        # Buttons for actions
        self.button_create = tk.Button(master, text="Create", command=self.create_user, bg="#fb8500", fg="black")
        self.button_create.grid(row=len(labels), column=0, columnspan=2, pady=10)

        self.button_update = tk.Button(master, text="Update", command=self.update_user, bg="#fb8500", fg="black")
        self.button_update.grid(row=len(labels) + 1, column=0, columnspan=2, pady=10)

        self.button_delete = tk.Button(master, text="Delete", command=self.delete_user, bg="#fb8500", fg="black")
        self.button_delete.grid(row=len(labels) + 2, column=0, columnspan=2, pady=10)

        self.button_back = tk.Button(master, text="Back", command=self.back, bg="#f4a261", fg="black")
        self.button_back.grid(row=len(labels) + 3, column=0, columnspan=2, pady=10)

    def create_user(self):
        # Retrieve data from entry widgets
        data = [entry.get() for entry in self.entries]
        user_id, user_name, mobile, email, address = data
        try:
            # Insert data into the database
            cursor = self.db_connection.cursor()
            cursor.execute("INSERT INTO USER1 VALUES (?, ?, ?, ?, ?)", (user_id, user_name, mobile, email, address))
            self.db_connection.commit()
            messagebox.showinfo("User Created", "User created successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))


    def update_user(self):
        # Retrieve data from entry widgets
        data = [entry.get() for entry in self.entries]
        user_id, user_name, user_mob, user_mail, user_address = data
        try:
            # Update user information in the database
            cursor = self.db_connection.cursor()
            cursor.execute("UPDATE USER1 SET user_name=?, user_mob=?, user_mail=?, user_address=? WHERE user_id=?", 
                        (user_name, user_mob, user_mail, user_address, user_id))
            self.db_connection.commit()
            messagebox.showinfo("User Updated", "User information updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))



    def delete_user(self):
        # Retrieve data from entry widgets
        data = [entry.get() for entry in self.entries]
        user_id = data[0]  # Assuming user_id is the first entry
        try:
            # Delete user from the database
            cursor = self.db_connection.cursor()
            cursor.execute("DELETE FROM USER1 WHERE user_id=?", (user_id,))
            self.db_connection.commit()
            messagebox.showinfo("User Deleted", "User deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def back(self):
        self.master.withdraw()  # Hide the current window
        # Create a new window for the main menu
        main_menu_window = tk.Toplevel()
        app = MainMenu(main_menu_window, self.db_connection)
    # Assuming your main menu class is named MainMenu



class BRANCH:
    def __init__(self, master, db_connection):
        self.master = master
        self.db_connection = db_connection
        self.c = self.db_connection.cursor()
        master.title("Branch")
        master.geometry("400x400")
        master.configure(bg="#023047")  # Set background color

        # Labels and entry fields for branch attributes
        labels = ["Branch ID:", "Branch Name:", "Branch Address:", "Branch Manager:"]
        self.entries = []
        for i, label_text in enumerate(labels):
            label = tk.Label(master, text=label_text, bg="#023047", fg="white")
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(master, width=30)  # Set fixed width
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            self.entries.append(entry)

        # Buttons for actions
        self.button_create = tk.Button(master, text="Create", command=self.create_branch, bg="#fb8500", fg="black")
        self.button_create.grid(row=len(labels), column=0, columnspan=2, pady=10)

        self.button_update = tk.Button(master, text="Update", command=self.update_branch, bg="#fb8500", fg="black")
        self.button_update.grid(row=len(labels) + 1, column=0, columnspan=2, pady=10)

        self.button_delete = tk.Button(master, text="Delete", command=self.delete_branch, bg="#fb8500", fg="black")
        self.button_delete.grid(row=len(labels) + 2, column=0, columnspan=2, pady=10)

        self.button_back = tk.Button(master, text="Back", command=self.back, bg="#f4a261", fg="black")
        self.button_back.grid(row=len(labels) + 3, column=0, columnspan=2, pady=10)

    def create_branch(self):
        # Retrieve data from entry widgets
        data = [entry.get() for entry in self.entries]
        branch_id, branch_name, branch_address, branch_manager = data
        try:
            # Insert data into the database
            cursor = self.db_connection.cursor()
            cursor.execute("INSERT INTO BRANCH VALUES (?, ?, ?, ?)", (branch_id, branch_name, branch_address, branch_manager))
            self.db_connection.commit()
            messagebox.showinfo("Branch Created", "Branch created successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_branch(self):
        # Retrieve data from entry widgets
        data = [entry.get() for entry in self.entries]
        branch_id, branch_name, branch_address, branch_manager = data
        try:
            # Update branch information in the database
            cursor = self.db_connection.cursor()
            cursor.execute("UPDATE BRANCH SET branch_name=?, branch_address=?, branch_manager=? WHERE branch_id=?", 
                           (branch_name, branch_address, branch_manager, branch_id))
            self.db_connection.commit()
            messagebox.showinfo("Branch Updated", "Branch information updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_branch(self):
        # Retrieve data from entry widgets
        data = [entry.get() for entry in self.entries]
        branch_id = data[0]  # Assuming branch_id is the first entry
        try:
            # Delete branch from the database
            cursor = self.db_connection.cursor()
            cursor.execute("DELETE FROM BRANCH WHERE branch_id=?", (branch_id,))
            self.db_connection.commit()
            messagebox.showinfo("Branch Deleted", "Branch deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def back(self):
        self.master.withdraw()  # Hide the current window
        # Create a new window for the main menu
        main_menu_window = tk.Toplevel()
        app = MainMenu(main_menu_window, self.db_connection)



class CREDIT_CARD:
    def __init__(self, master, db_connection):
        self.master = master
        self.db_connection = db_connection
        self.c = self.db_connection.cursor()
        master.title("Credit Card")
        master.geometry("400x400")
        master.configure(bg="#023047")  # Set background color

        # Labels and entry fields for credit card attributes
        labels = ["Credit Card Name:", "Credit Card ID:", "Balance:", "Type:", "User ID:"]
        self.entries = []
        for i, label_text in enumerate(labels):
            label = tk.Label(master, text=label_text, bg="#023047", fg="white")
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(master, width=30)  # Set fixed width
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            self.entries.append(entry)

        # Buttons for actions
        self.button_create = tk.Button(master, text="Create", command=self.create_credit_card, bg="#fb8500", fg="black")
        self.button_create.grid(row=len(labels), column=0, columnspan=2, pady=10)

        self.button_update = tk.Button(master, text="Update", command=self.update_credit_card, bg="#fb8500", fg="black")
        self.button_update.grid(row=len(labels) + 1, column=0, columnspan=2, pady=10)

        self.button_delete = tk.Button(master, text="Delete", command=self.delete_credit_card, bg="#fb8500", fg="black")
        self.button_delete.grid(row=len(labels) + 2, column=0, columnspan=2, pady=10)

        self.button_back = tk.Button(master, text="Back", command=self.back, bg="#f4a261", fg="black")
        self.button_back.grid(row=len(labels) + 3, column=0, columnspan=2, pady=10)

    def create_credit_card(self):
        # Retrieve data from entry widgets
        data = [entry.get() for entry in self.entries]
        crc_name, crc_id, crc_bal, crc_type, crc_user_id = data
        try:
            # Insert data into the database
            cursor = self.db_connection.cursor()
            cursor.execute("INSERT INTO CREDIT_CARD VALUES (?, ?, ?, ?, ?)", (crc_name, crc_id, crc_bal, crc_type, crc_user_id))
            self.db_connection.commit()
            messagebox.showinfo("Credit Card Created", "Credit card created successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_credit_card(self):
        # Retrieve data from entry widgets
        data = [entry.get() for entry in self.entries]
        crc_name, crc_id, crc_bal, crc_type, crc_user_id = data
        try:
            # Update credit card information in the database
            cursor = self.db_connection.cursor()
            cursor.execute("UPDATE CREDIT_CARD SET crc_name=?, crc_bal=?, crc_type=?, crc_user_id=? WHERE crc_id=?", 
                           (crc_name, crc_bal, crc_type, crc_user_id, crc_id))
            self.db_connection.commit()
            messagebox.showinfo("Credit Card Updated", "Credit card information updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_credit_card(self):
        # Retrieve data from entry widgets
        data = [entry.get() for entry in self.entries]
        crc_id = data[0]  # Assuming crc_id is the first entry
        try:
            # Delete credit card from the database
            cursor = self.db_connection.cursor()
            cursor.execute("DELETE FROM CREDIT_CARD WHERE crc_id=?", (crc_id,))
            self.db_connection.commit()
            messagebox.showinfo("Credit Card Deleted", "Credit card deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))


    def back(self):
        self.master.withdraw()  # Hide the current window
        # Create a new window for the main menu
        main_menu_window = tk.Toplevel()
        app = MainMenu(main_menu_window, self.db_connection)


class LIMITS:
    def __init__(self, master, db_connection):
        self.master = master
        self.db_connection = db_connection
        self.c = self.db_connection.cursor()
        master.title("Limits")
        master.geometry("400x400")
        master.configure(bg="#023047")  # Set background color

        # Labels and entry fields for limit attributes
        labels = ["User ID:", "Balance:", "Credit Card ID:"]
        self.entries = []
        for i, label_text in enumerate(labels):
            label = tk.Label(master, text=label_text, bg="#023047", fg="white")
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(master, width=30)  # Set fixed width
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            self.entries.append(entry)

        # Buttons for actions
        self.button_create = tk.Button(master, text="Create", command=self.create_limit, bg="#fb8500", fg="black")
        self.button_create.grid(row=len(labels), column=0, columnspan=2, pady=10)

        self.button_update = tk.Button(master, text="Update", command=self.update_limit, bg="#fb8500", fg="black")
        self.button_update.grid(row=len(labels) + 1, column=0, columnspan=2, pady=10)

        self.button_delete = tk.Button(master, text="Delete", command=self.delete_limit, bg="#fb8500", fg="black")
        self.button_delete.grid(row=len(labels) + 2, column=0, columnspan=2, pady=10)

        self.button_back = tk.Button(master, text="Back", command=self.back, bg="#f4a261", fg="black")
        self.button_back.grid(row=len(labels) + 3, column=0, columnspan=2, pady=10)

    def create_limit(self):
        # Retrieve data from entry widgets
        data = [entry.get() for entry in self.entries]
        limit_user_id, limit_bal, limit_crc_id = data
        try:
            # Insert data into the database
            cursor = self.db_connection.cursor()
            cursor.execute("INSERT INTO LIMITS VALUES (?, ?, ?)", (limit_user_id, limit_bal, limit_crc_id))
            self.db_connection.commit()
            messagebox.showinfo("Limit Created", "Limit created successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_limit(self):
        # Retrieve data from entry widgets
        data = [entry.get() for entry in self.entries]
        limit_user_id, limit_bal, limit_crc_id = data
        try:
            # Update limit information in the database
            cursor = self.db_connection.cursor()
            cursor.execute("UPDATE LIMITS SET limit_bal=? WHERE limit_user_id=? AND limit_crc_id=?", 
                           (limit_bal, limit_user_id, limit_crc_id))
            self.db_connection.commit()
            messagebox.showinfo("Limit Updated", "Limit information updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_limit(self):
        # Retrieve data from entry widgets
        user_id = self.entries[0].get()
        
        try:
            # Delete limit from the database based on user ID
            cursor = self.db_connection.cursor()
            cursor.execute("DELETE FROM LIMITS WHERE limit_user_id=?", (user_id,))
            self.db_connection.commit()
            messagebox.showinfo("Limit Deleted", "Limit deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))




    def back(self):
        self.master.withdraw()  # Hide the current window
        # Create a new window for the main menu
        main_menu_window = tk.Toplevel()
        app = MainMenu(main_menu_window, self.db_connection)


class APPLICATIONS:
    def __init__(self, master, db_connection):
        self.master = master
        self.db_connection = db_connection
        self.c = self.db_connection.cursor()
        master.title("Applications")
        master.geometry("400x400")
        master.configure(bg="#023047")  # Set background color

        # Labels and entry fields for application attributes
        labels = ["Application Number:", "User ID:", "Type:"]
        self.entries = []
        for i, label_text in enumerate(labels):
            label = tk.Label(master, text=label_text, bg="#023047", fg="white")
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(master, width=30)  # Set fixed width
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            self.entries.append(entry)

        # Buttons for actions
        self.button_create = tk.Button(master, text="Create", command=self.create_application, bg="#fb8500", fg="black")
        self.button_create.grid(row=len(labels), column=0, columnspan=2, pady=10)

        self.button_update = tk.Button(master, text="Update", command=self.update_application, bg="#fb8500", fg="black")
        self.button_update.grid(row=len(labels) + 1, column=0, columnspan=2, pady=10)

        self.button_delete = tk.Button(master, text="Delete", command=self.delete_application, bg="#fb8500", fg="black")
        self.button_delete.grid(row=len(labels) + 2, column=0, columnspan=2, pady=10)

        self.button_back = tk.Button(master, text="Back", command=self.back, bg="#f4a261", fg="black")
        self.button_back.grid(row=len(labels) + 3, column=0, columnspan=2, pady=10)

    def create_application(self):
        # Retrieve data from entry widgets
        data = [entry.get() for entry in self.entries]
        app_num, app_user_id, app_type = data
        try:
            # Insert data into the database
            cursor = self.db_connection.cursor()
            cursor.execute("INSERT INTO APPLICATIONS VALUES (?, ?, ?)", (app_num, app_user_id, app_type))
            self.db_connection.commit()
            messagebox.showinfo("Application Created", "Application created successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_application(self):
        # Retrieve data from entry widgets
        data = [entry.get() for entry in self.entries]
        app_num, app_user_id, app_type = data
        try:
            # Update application information in the database
            cursor = self.db_connection.cursor()
            cursor.execute("UPDATE APPLICATIONS SET app_type=? WHERE app_num=? AND app_user_id=?", 
                           (app_type, app_num, app_user_id))
            self.db_connection.commit()
            messagebox.showinfo("Application Updated", "Application information updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_application(self):
        # Retrieve data from the entry widget
        app_num = self.entries[0].get()

        try:
            # Delete application from the database based on the application number
            cursor = self.db_connection.cursor()
            cursor.execute("DELETE FROM APPLICATIONS WHERE app_num=?", (app_num,))
            self.db_connection.commit()
            messagebox.showinfo("Application Deleted", "Application deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))



    def back(self):
        self.master.withdraw()  # Hide the current window
        # Create a new window for the main menu
        main_menu_window = tk.Toplevel()
        app = MainMenu(main_menu_window, self.db_connection)




def main():
    # Connect to the database
    db_connection = sqlite3.connect("your_database_name.db")
    # Create tables
    create_tables(db_connection)


    # Create the Tkinter root window
    root = tk.Tk()

    # Instantiate the WelcomePage class with the database connection
    app = WelcomePage(root, db_connection)

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()