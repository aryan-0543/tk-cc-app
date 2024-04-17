import tkinter as tk
import sqlite3
from tkinter import messagebox


class LoginApp:
    def __init__(self, master):
        self.master = master
        master.title("Login")
        

        self.label_username = tk.Label(master, text="Username:")
        self.label_username.grid(row=0, column=0, padx=10, pady=5)
        self.entry_username = tk.Entry(master)
        self.entry_username.grid(row=0, column=1, padx=10, pady=5)

        self.label_password = tk.Label(master, text="Password:")
        self.label_password.grid(row=1, column=0, padx=10, pady=5)
        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.grid(row=1, column=1, padx=10, pady=5)

        self.button_login = tk.Button(master, text="Login", command=self.login)
        self.button_login.grid(row=2, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Replace with your authentication logic
        if username == "admin" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
            # Open the main application window after successful login
            self.open_main_app()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def open_main_app(self):
        # Close the login window and open the main application window
        self.master.destroy()
        root = tk.Tk()
        app = CreditCardApp(root)
        root.mainloop()


class CreditCardApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Credit Card Management System")

        # Connect to the database
        self.conn = sqlite3.connect('credit_card_database.db')
        self.c = self.conn.cursor()

        # Create tables if they don't exist
        self.create_tables()

        # Create labels and entry fields for BRANCH table
        self.label_branch_id = tk.Label(master, text="Branch ID:")
        self.label_branch_id.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.entry_branch_id = tk.Entry(master)
        self.entry_branch_id.grid(row=0, column=1, padx=10, pady=5)

        self.label_branch_name = tk.Label(master, text="Branch Name:")
        self.label_branch_name.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.entry_branch_name = tk.Entry(master)
        self.entry_branch_name.grid(row=1, column=1, padx=10, pady=5)

        self.label_branch_address = tk.Label(master, text="Branch Address:")
        self.label_branch_address.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.entry_branch_address = tk.Entry(master)
        self.entry_branch_address.grid(row=2, column=1, padx=10, pady=5)

        self.label_branch_manager = tk.Label(master, text="Branch Manager:")
        self.label_branch_manager.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.entry_branch_manager = tk.Entry(master)
        self.entry_branch_manager.grid(row=3, column=1, padx=10, pady=5)

        # Create labels and entry fields for USER1 table
        self.label_user_id = tk.Label(master, text="User ID:")
        self.label_user_id.grid(row=0, column=2, sticky="w", padx=10, pady=5)
        self.entry_user_id = tk.Entry(master)
        self.entry_user_id.grid(row=0, column=3, padx=10, pady=5)

        self.label_user_name = tk.Label(master, text="User Name:")
        self.label_user_name.grid(row=1, column=2, sticky="w", padx=10, pady=5)
        self.entry_user_name = tk.Entry(master)
        self.entry_user_name.grid(row=1, column=3, padx=10, pady=5)

        self.label_user_mob = tk.Label(master, text="User Mobile:")
        self.label_user_mob.grid(row=2, column=2, sticky="w", padx=10, pady=5)
        self.entry_user_mob = tk.Entry(master)
        self.entry_user_mob.grid(row=2, column=3, padx=10, pady=5)

        self.label_user_mail = tk.Label(master, text="User Mail:")
        self.label_user_mail.grid(row=3, column=2, sticky="w", padx=10, pady=5)
        self.entry_user_mail = tk.Entry(master)
        self.entry_user_mail.grid(row=3, column=3, padx=10, pady=5)

        self.label_user_address = tk.Label(master, text="User Address:")
        self.label_user_address.grid(row=4, column=2, sticky="w", padx=10, pady=5)
        self.entry_user_address = tk.Entry(master)
        self.entry_user_address.grid(row=4, column=3, padx=10, pady=5)

        self.label_user_branch_id = tk.Label(master, text="User Branch ID:")
        self.label_user_branch_id.grid(row=5, column=2, sticky="w", padx=10, pady=5)
        self.entry_user_branch_id = tk.Entry(master)
        self.entry_user_branch_id.grid(row=5, column=3, padx=10, pady=5)

        # Create labels and entry fields for CREDIT_CARD table
        self.label_crc_name = tk.Label(master, text="Credit Card Name:")
        self.label_crc_name.grid(row=0, column=4, sticky="w", padx=10, pady=5)
        self.entry_crc_name = tk.Entry(master)
        self.entry_crc_name.grid(row=0, column=5, padx=10, pady=5)

        self.label_crc_id = tk.Label(master, text="Credit Card ID:")
        self.label_crc_id.grid(row=1, column=4, sticky="w", padx=10, pady=5)
        self.entry_crc_id = tk.Entry(master)
        self.entry_crc_id.grid(row=1, column=5, padx=10, pady=5)

        self.label_crc_bal = tk.Label(master, text="Credit Card Balance:")
        self.label_crc_bal.grid(row=2, column=4, sticky="w", padx=10, pady=5)
        self.entry_crc_bal = tk.Entry(master)
        self.entry_crc_bal.grid(row=2, column=5, padx=10, pady=5)

        self.label_crc_type = tk.Label(master, text="Credit Card Type:")
        self.label_crc_type.grid(row=3, column=4, sticky="w", padx=10, pady=5)
        self.entry_crc_type = tk.Entry(master)
        self.entry_crc_type.grid(row=3, column=5, padx=10, pady=5)

        self.label_crc_user_id = tk.Label(master, text="Credit Card User ID:")
        self.label_crc_user_id.grid(row=4, column=4, sticky="w", padx=10, pady=5)
        self.entry_crc_user_id = tk.Entry(master)
        self.entry_crc_user_id.grid(row=4, column=5, padx=10, pady=5)

        # Create labels and entry fields for LIMITS table
        self.label_limit_user_id = tk.Label(master, text="Limit User ID:")
        self.label_limit_user_id.grid(row=0, column=6, sticky="w", padx=10, pady=5)
        self.entry_limit_user_id = tk.Entry(master)
        self.entry_limit_user_id.grid(row=0, column=7, padx=10, pady=5)

        self.label_limit_bal = tk.Label(master, text="Limit Balance:")
        self.label_limit_bal.grid(row=1, column=6, sticky="w", padx=10, pady=5)
        self.entry_limit_bal = tk.Entry(master)
        self.entry_limit_bal.grid(row=1, column=7, padx=10, pady=5)

        self.label_limit_crc_id = tk.Label(master, text="Limit Credit Card ID:")
        self.label_limit_crc_id.grid(row=2, column=6, sticky="w", padx=10, pady=5)
        self.entry_limit_crc_id = tk.Entry(master)
        self.entry_limit_crc_id.grid(row=2, column=7, padx=10, pady=5)

        # Create labels and entry fields for APPLICATIONS table
        self.label_app_num = tk.Label(master, text="Application Number:")
        self.label_app_num.grid(row=0, column=8, sticky="w", padx=10, pady=5)
        self.entry_app_num = tk.Entry(master)
        self.entry_app_num.grid(row=0, column=9, padx=10, pady=5)

        self.label_app_user_id = tk.Label(master, text="Application User ID:")
        self.label_app_user_id.grid(row=1, column=8, sticky="w", padx=10, pady=5)
        self.entry_app_user_id = tk.Entry(master)
        self.entry_app_user_id.grid(row=1, column=9, padx=10, pady=5)

        self.label_app_type = tk.Label(master, text="Application Type:")
        self.label_app_type.grid(row=2, column=8, sticky="w", padx=10, pady=5)
        self.entry_app_type = tk.Entry(master)
        self.entry_app_type.grid(row=2, column=9, padx=10, pady=5)
        

        # Create buttons for inserting data for each table
        self.button_insert_branch = tk.Button(master, text="Insert Branch", command=self.insert_branch_data)
        self.button_insert_branch.grid(row=6, column=0, columnspan=2, pady=10, padx=10, sticky="we")

        self.button_insert_user = tk.Button(master, text="Insert User", command=self.insert_user_data)
        self.button_insert_user.grid(row=6, column=2, columnspan=2, pady=10, padx=10, sticky="we")

        self.button_insert_credit_card = tk.Button(master, text="Insert Credit Card", command=self.insert_credit_card_data)
        self.button_insert_credit_card.grid(row=6, column=4, columnspan=2, pady=10, padx=10, sticky="we")

        self.button_insert_limits = tk.Button(master, text="Insert Limits", command=self.insert_limits_data)
        self.button_insert_limits.grid(row=6, column=6, columnspan=2, pady=10, padx=10, sticky="we")

        self.button_insert_applications = tk.Button(master, text="Insert Applications", command=self.insert_applications_data)
        self.button_insert_applications.grid(row=6, column=8, columnspan=2, pady=10, padx=10, sticky="we")
        



        # Create buttons for updating data for each table
        self.button_update_branch = tk.Button(master, text="Update Branch", command=self.update_branch_data)
        self.button_update_branch.grid(row=7, column=0, columnspan=2, pady=10, padx=10, sticky="we")

        self.button_update_user = tk.Button(master, text="Update User", command=self.update_user_data)
        self.button_update_user.grid(row=7, column=2, columnspan=2, pady=10, padx=10, sticky="we")

        self.button_update_credit_card = tk.Button(master, text="Update Credit Card", command=self.update_credit_card_data)
        self.button_update_credit_card.grid(row=7, column=4, columnspan=2, pady=10, padx=10, sticky="we")

        self.button_update_limits = tk.Button(master, text="Update Limits", command=self.update_limits_data)
        self.button_update_limits.grid(row=7, column=6, columnspan=2, pady=10, padx=10, sticky="we")

        self.button_update_applications = tk.Button(master, text="Update Applications", command=self.update_applications_data)
        self.button_update_applications.grid(row=7, column=8, columnspan=2, pady=10, padx=10, sticky="we")


        # Create buttons for deleting data for each table
        self.button_delete_branch = tk.Button(master, text="Delete Branch", command=self.delete_branch_data)
        self.button_delete_branch.grid(row=8, column=0, columnspan=2, pady=10, padx=10, sticky="we")

        self.button_delete_user = tk.Button(master, text="Delete User", command=self.delete_user_data)
        self.button_delete_user.grid(row=8, column=2, columnspan=2, pady=10, padx=10, sticky="we")

        self.button_delete_credit_card = tk.Button(master, text="Delete Credit Card", command=self.delete_credit_card_data)
        self.button_delete_credit_card.grid(row=8, column=4, columnspan=2, pady=10, padx=10, sticky="we")

        self.button_delete_limits = tk.Button(master, text="Delete Limits", command=self.delete_limits_data)
        self.button_delete_limits.grid(row=8, column=6, columnspan=2, pady=10, padx=10, sticky="we")

        self.button_delete_applications = tk.Button(master, text="Delete Applications", command=self.delete_applications_data)
        self.button_delete_applications.grid(row=8, column=8, columnspan=2, pady=10, padx=10, sticky="we")



        # Create buttons for retrieving data for each table
        self.button_retrieve_branch = tk.Button(master, text="Retrieve Branch", command=lambda: self.retrieve_data("BRANCH", "branch_id", self.entry_branch_id, self.entry_branch_name, self.entry_branch_address, self.entry_branch_manager))
        self.button_retrieve_branch.grid(row=9, column=0, columnspan=2, pady=10, padx=10, sticky="we")

        self.button_retrieve_user = tk.Button(master, text="Retrieve User", command=lambda: self.retrieve_data("USER1", "user_id", self.entry_user_id, self.entry_user_name, self.entry_user_mob, self.entry_user_mail, self.entry_user_address, self.entry_user_branch_id))
        self.button_retrieve_user.grid(row=9, column=2, columnspan=2, pady=10, padx=10, sticky="we")

        self.button_retrieve_credit_card = tk.Button(master, text="Retrieve Credit Card", command=lambda: self.retrieve_data("CREDIT_CARD", "crc_id", self.entry_crc_id, self.entry_crc_bal, self.entry_crc_type, self.entry_crc_user_id))
        self.button_retrieve_credit_card.grid(row=9, column=4, columnspan=2, pady=10, padx=10, sticky="we")

        self.button_retrieve_limits = tk.Button(master, text="Retrieve Limits", command=lambda: self.retrieve_data("LIMITS", "limit_user_id", self.entry_limit_user_id, self.entry_limit_bal, self.entry_limit_crc_id))
        self.button_retrieve_limits.grid(row=9, column=6, columnspan=2, pady=10, padx=10, sticky="we")

        self.button_retrieve_applications = tk.Button(master, text="Retrieve Applications", command=lambda: self.retrieve_data("APPLICATIONS", "app_num", self.entry_app_num, self.entry_app_user_id, self.entry_app_type))
        self.button_retrieve_applications.grid(row=9, column=8, columnspan=2, pady=10, padx=10, sticky="we")


        # Create a Text widget to display the data
        self.text_view_all = tk.Text(master, height=20, width=100)
        self.text_view_all.grid(row=11, column=0, columnspan=10, pady=10, padx=10, sticky="we")

        # Create a button for viewing all data
        self.button_view_all = tk.Button(master, text="View All Data", command=self.view_all_data)
        self.button_view_all.grid(row=10, column=0, columnspan=10, pady=10, padx=10, sticky="we")



    def create_tables(self):
        try:
            self.c.execute('''CREATE TABLE IF NOT EXISTS BRANCH (
                                branch_id INT PRIMARY KEY,
                                branch_name CHAR(20) NOT NULL,
                                branch_address CHAR(25) NOT NULL,
                                branch_manager CHAR(25) NOT NULL
                            )''')
            self.c.execute('''CREATE TABLE IF NOT EXISTS USER1 (
                                user_id INT PRIMARY KEY,
                                user_name CHAR(25) NOT NULL,
                                user_mob INT NOT NULL,
                                user_mail VARCHAR(30) NOT NULL,
                                user_address VARCHAR(50) NOT NULL,
                                user_branch_id INT NOT NULL,
                                FOREIGN KEY (user_branch_id) REFERENCES BRANCH(branch_id) ON DELETE CASCADE ON UPDATE CASCADE
                            )''')
            self.c.execute('''CREATE TABLE IF NOT EXISTS CREDIT_CARD (
                                crc_name VARCHAR(25) NOT NULL,
                                crc_id INT PRIMARY KEY,
                                crc_bal INT NOT NULL,
                                crc_type VARCHAR(15) NOT NULL,
                                crc_user_id INT NOT NULL,
                                FOREIGN KEY (crc_user_id) REFERENCES USER1(user_id) ON DELETE CASCADE ON UPDATE CASCADE
                            )''')
            self.c.execute('''CREATE TABLE IF NOT EXISTS LIMITS (
                                limit_user_id INT PRIMARY KEY,
                                limit_bal INT NOT NULL,
                                limit_crc_id INT NOT NULL,
                                FOREIGN KEY (limit_crc_id) REFERENCES CREDIT_CARD(crc_id) ON DELETE CASCADE ON UPDATE CASCADE
                            )''')
            self.c.execute('''CREATE TABLE IF NOT EXISTS APPLICATIONS (
                                app_num INT PRIMARY KEY,
                                app_user_id INT NOT NULL,
                                app_type VARCHAR(20) NOT NULL,
                                FOREIGN KEY (app_user_id) REFERENCES USER1(user_id) ON DELETE CASCADE ON UPDATE CASCADE
                            )''')
            self.conn.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Error", str(e))

    def insert_branch_data(self):
        branch_id = self.entry_branch_id.get()
        branch_name = self.entry_branch_name.get()
        branch_address = self.entry_branch_address.get()
        branch_manager = self.entry_branch_manager.get()

        if branch_id and branch_name and branch_address and branch_manager:
            try:
                self.c.execute("INSERT INTO BRANCH VALUES (?, ?, ?, ?)", (branch_id, branch_name, branch_address, branch_manager))
                self.conn.commit()
                messagebox.showinfo("Success", "Data inserted successfully.")
            except sqlite3.Error as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "All fields are required.")

    def insert_user_data(self):
        user_id = self.entry_user_id.get()
        user_name = self.entry_user_name.get()
        user_mob = self.entry_user_mob.get()
        user_mail = self.entry_user_mail.get()
        user_address = self.entry_user_address.get()
        user_branch_id = self.entry_user_branch_id.get()

        if user_id and user_name and user_mob and user_mail and user_address and user_branch_id:
            try:
                self.c.execute("INSERT INTO USER1 VALUES (?, ?, ?, ?, ?, ?)", (user_id, user_name, user_mob, user_mail, user_address, user_branch_id))
                self.conn.commit()
                messagebox.showinfo("Success", "Data inserted successfully.")
            except sqlite3.Error as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "All fields are required.")


    def insert_credit_card_data(self):
        crc_name = self.entry_crc_name.get()
        crc_id = self.entry_crc_id.get()
        crc_bal = self.entry_crc_bal.get()
        crc_type = self.entry_crc_type.get()
        crc_user_id = self.entry_crc_user_id.get()

        if crc_name and crc_id and crc_bal and crc_type and crc_user_id:
            try:
                self.c.execute("INSERT INTO CREDIT_CARD VALUES (?, ?, ?, ?, ?)", (crc_name, crc_id, crc_bal, crc_type, crc_user_id))
                self.conn.commit()
                messagebox.showinfo("Success", "Data inserted successfully.")
            except sqlite3.Error as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "All fields are required.")

    def insert_limits_data(self):
        limit_user_id = self.entry_limit_user_id.get()
        limit_bal = self.entry_limit_bal.get()
        limit_crc_id = self.entry_limit_crc_id.get()

        if limit_user_id and limit_bal and limit_crc_id:
            try:
                self.c.execute("INSERT INTO LIMITS VALUES (?, ?, ?)", (limit_user_id, limit_bal, limit_crc_id))
                self.conn.commit()
                messagebox.showinfo("Success", "Data inserted successfully.")
            except sqlite3.Error as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "All fields are required.")

    def insert_applications_data(self):
        app_num = self.entry_app_num.get()
        app_user_id = self.entry_app_user_id.get()
        app_type = self.entry_app_type.get()

        if app_num and app_user_id and app_type:
            try:
                self.c.execute("INSERT INTO APPLICATIONS VALUES (?, ?, ?)", (app_num, app_user_id, app_type))
                self.conn.commit()
                messagebox.showinfo("Success", "Data inserted successfully.")
            except sqlite3.Error as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "All fields are required.")

    #update functions for each table

    def update_branch_data(self):
        branch_id = self.entry_branch_id.get()
        branch_name = self.entry_branch_name.get()
        branch_address = self.entry_branch_address.get()
        branch_manager = self.entry_branch_manager.get()

        if branch_id:
            try:
                self.c.execute("UPDATE BRANCH SET branch_name=?, branch_address=?, branch_manager=? WHERE branch_id=?", (branch_name, branch_address, branch_manager, branch_id))
                self.conn.commit()
                messagebox.showinfo("Success", "Data updated successfully.")
            except sqlite3.Error as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please enter Branch ID.")

    def update_user_data(self):
        user_id = self.entry_user_id.get()
        user_name = self.entry_user_name.get()
        user_mob = self.entry_user_mob.get()
        user_mail = self.entry_user_mail.get()
        user_address = self.entry_user_address.get()
        user_branch_id = self.entry_user_branch_id.get()

        if user_id:
            try:
                self.c.execute("UPDATE USER1 SET user_name=?, user_mob=?, user_mail=?, user_address=?, user_branch_id=? WHERE user_id=?", (user_name, user_mob, user_mail, user_address, user_branch_id, user_id))
                self.conn.commit()
                messagebox.showinfo("Success", "Data updated successfully.")
            except sqlite3.Error as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please enter User ID.")

    def update_credit_card_data(self):
        crc_id = self.entry_crc_id.get()
        crc_bal = self.entry_crc_bal.get()
        crc_type = self.entry_crc_type.get()
        crc_user_id = self.entry_crc_user_id.get()

        if crc_id:
            try:
                self.c.execute("UPDATE CREDIT_CARD SET crc_bal=?, crc_type=?, crc_user_id=? WHERE crc_id=?", (crc_bal, crc_type, crc_user_id, crc_id))
                self.conn.commit()
                messagebox.showinfo("Success", "Data updated successfully.")
            except sqlite3.Error as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please enter Credit Card ID.")

    def update_limits_data(self):
        limit_user_id = self.entry_limit_user_id.get()
        limit_bal = self.entry_limit_bal.get()
        limit_crc_id = self.entry_limit_crc_id.get()

        if limit_user_id:
            try:
                self.c.execute("UPDATE LIMITS SET limit_bal=?, limit_crc_id=? WHERE limit_user_id=?", (limit_bal, limit_crc_id, limit_user_id))
                self.conn.commit()
                messagebox.showinfo("Success", "Data updated successfully.")
            except sqlite3.Error as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please enter User ID.")

    def update_applications_data(self):
        app_num = self.entry_app_num.get()
        app_user_id = self.entry_app_user_id.get()
        app_type = self.entry_app_type.get()

        if app_num:
            try:
                self.c.execute("UPDATE APPLICATIONS SET app_user_id=?, app_type=? WHERE app_num=?", (app_user_id, app_type, app_num))
                self.conn.commit()
                messagebox.showinfo("Success", "Data updated successfully.")
            except sqlite3.Error as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please enter Application Number.")


    #delete functions for each table
    def delete_branch_data(self):
        branch_id = self.entry_branch_id.get()

        if branch_id:
            try:
                self.c.execute("DELETE FROM BRANCH WHERE branch_id=?", (branch_id,))
                self.conn.commit()
                messagebox.showinfo("Success", "Data deleted successfully.")
            except sqlite3.Error as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please enter Branch ID.")

    def delete_user_data(self):
        user_id = self.entry_user_id.get()

        if user_id:
            try:
                self.c.execute("DELETE FROM USER1 WHERE user_id=?", (user_id,))
                self.conn.commit()
                messagebox.showinfo("Success", "Data deleted successfully.")
            except sqlite3.Error as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please enter User ID.")

    def delete_credit_card_data(self):
        crc_id = self.entry_crc_id.get()

        if crc_id:
            try:
                self.c.execute("DELETE FROM CREDIT_CARD WHERE crc_id=?", (crc_id,))
                self.conn.commit()
                messagebox.showinfo("Success", "Data deleted successfully.")
            except sqlite3.Error as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please enter Credit Card ID.")

    def delete_limits_data(self):
        limit_user_id = self.entry_limit_user_id.get()

        if limit_user_id:
            try:
                self.c.execute("DELETE FROM LIMITS WHERE limit_user_id=?", (limit_user_id,))
                self.conn.commit()
                messagebox.showinfo("Success", "Data deleted successfully.")
            except sqlite3.Error as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please enter User ID.")

    def delete_applications_data(self):
        app_num = self.entry_app_num.get()

        if app_num:
            try:
                self.c.execute("DELETE FROM APPLICATIONS WHERE app_num=?", (app_num,))
                self.conn.commit()
                messagebox.showinfo("Success", "Data deleted successfully.")
            except sqlite3.Error as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please enter Application Number.")

    #retrieve functions for all tables

    def retrieve_branch_data(self):
        branch_id = self.entry_branch_id.get()

        if branch_id:
            try:
                self.c.execute("SELECT * FROM BRANCH WHERE branch_id=?", (branch_id,))
                data = self.c.fetchone()
                if data:
                    self.entry_branch_name.delete(0, tk.END)
                    self.entry_branch_address.delete(0, tk.END)
                    self.entry_branch_manager.delete(0, tk.END)
                    
                    self.entry_branch_name.insert(tk.END, data[1])
                    self.entry_branch_address.insert(tk.END, data[2])
                    self.entry_branch_manager.insert(tk.END, data[3])
                else:
                    messagebox.showinfo("Error", "No data found for Branch ID: {}".format(branch_id))
            except sqlite3.Error as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please enter Branch ID.")

    def retrieve_user_data(self):
        user_id = self.entry_user_id.get()

        if user_id:
            try:
                self.c.execute("SELECT * FROM USER1 WHERE user_id=?", (user_id,))
                data = self.c.fetchone()
                if data:
                    self.entry_user_name.delete(0, tk.END)
                    self.entry_user_mob.delete(0, tk.END)
                    self.entry_user_mail.delete(0, tk.END)
                    self.entry_user_address.delete(0, tk.END)
                    self.entry_user_branch_id.delete(0, tk.END)
                    
                    self.entry_user_name.insert(tk.END, data[1])
                    self.entry_user_mob.insert(tk.END, data[2])
                    self.entry_user_mail.insert(tk.END, data[3])
                    self.entry_user_address.insert(tk.END, data[4])
                    self.entry_user_branch_id.insert(tk.END, data[5])
                else:
                    messagebox.showinfo("Error", "No data found for User ID: {}".format(user_id))
            except sqlite3.Error as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please enter User ID.")

    def retrieve_credit_card_data(self):
        crc_id = self.entry_crc_id.get()

        if crc_id:
            try:
                self.c.execute("SELECT * FROM CREDIT_CARD WHERE crc_id=?", (crc_id,))
                data = self.c.fetchone()
                if data:
                    self.entry_crc_bal.delete(0, tk.END)
                    self.entry_crc_type.delete(0, tk.END)
                    self.entry_crc_user_id.delete(0, tk.END)
                    
                    self.entry_crc_bal.insert(tk.END, data[2])
                    self.entry_crc_type.insert(tk.END, data[3])
                    self.entry_crc_user_id.insert(tk.END, data[4])
                else:
                    messagebox.showinfo("Error", "No data found for Credit Card ID: {}".format(crc_id))
            except sqlite3.Error as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please enter Credit Card ID.")

    def retrieve_limits_data(self):
        limit_user_id = self.entry_limit_user_id.get()

        if limit_user_id:
            try:
                self.c.execute("SELECT * FROM LIMITS WHERE limit_user_id=?", (limit_user_id,))
                data = self.c.fetchone()
                if data:
                    self.entry_limit_bal.delete(0, tk.END)
                    self.entry_limit_crc_id.delete(0, tk.END)
                    
                    self.entry_limit_bal.insert(tk.END, data[1])
                    self.entry_limit_crc_id.insert(tk.END, data[2])
                else:
                    messagebox.showinfo("Error", "No data found for User ID: {}".format(limit_user_id))
            except sqlite3.Error as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please enter User ID.")

    def retrieve_applications_data(self):
        app_num = self.entry_app_num.get()

        if app_num:
            try:
                self.c.execute("SELECT * FROM APPLICATIONS WHERE app_num=?", (app_num,))
                data = self.c.fetchone()
                if data:
                    self.entry_app_user_id.delete(0, tk.END)
                    self.entry_app_type.delete(0, tk.END)
                    
                    self.entry_app_user_id.insert(tk.END, data[1])
                    self.entry_app_type.insert(tk.END, data[2])
                else:
                    messagebox.showinfo("Error", "No data found for Application Number: {}".format(app_num))
            except sqlite3.Error as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please enter Application Number.")


        
    #"View All" button
    def view_all_data(self):
        try:
            # Fetch all data from each table
            self.c.execute("SELECT * FROM BRANCH")
            branch_data = self.c.fetchall()

            self.c.execute("SELECT * FROM USER1")
            user_data = self.c.fetchall()

            self.c.execute("SELECT * FROM CREDIT_CARD")
            credit_card_data = self.c.fetchall()

            self.c.execute("SELECT * FROM LIMITS")
            limits_data = self.c.fetchall()

            self.c.execute("SELECT * FROM APPLICATIONS")
            applications_data = self.c.fetchall()

            # Display data in the Text widget
            self.text_view_all.delete(1.0, tk.END)  # Clear previous data
            self.text_view_all.insert(tk.END, f"Branch Data: {branch_data}\n\n")
            self.text_view_all.insert(tk.END, f"User Data: {user_data}\n\n")
            self.text_view_all.insert(tk.END, f"Credit Card Data: {credit_card_data}\n\n")
            self.text_view_all.insert(tk.END, f"Limits Data: {limits_data}\n\n")
            self.text_view_all.insert(tk.END, f"Applications Data: {applications_data}\n\n")
        except sqlite3.Error as e:
            messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
