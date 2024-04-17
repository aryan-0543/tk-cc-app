# Credit Card Management System

This is a Python application built using Tkinter and SQLite for managing credit card data. The application provides functionality for inserting, updating, deleting, retrieving, and viewing all data stored in the database.

## Multiple Window GUI Application
This application demonstrates a simple multiple window GUI built using Tkinter in Python. It consists of a main login window and additional windows for various functionalities.

### Features
Login Window: Allows users to log in with their username and password.
Main Application Window: After successful login, users can access the main application window where they can perform various tasks.

### Functionality
The application provides the following functionality:

Login: Users can log in using their username and password.
Main Application: Upon successful login, users can access the main application window.  



## Application Features

- **Insert Data**: Add new records to the database.
- **Update Data**: Modify existing records in the database.
- **Delete Data**: Remove records from the database.
- **Retrieve Data**: Fetch specific records from the database.
- **View All Data**: Display all records stored in the database.

## Table Details

### BRANCH Table
- `branch_id`: Unique identifier for each branch.
- `branch_name`: Name of the branch.
- `branch_address`: Address of the branch.
- `branch_manager`: Manager of the branch.

### USER1 Table
- `user_id`: Unique identifier for each user.
- `user_name`: Name of the user.
- `user_mob`: Mobile number of the user.
- `user_mail`: Email address of the user.
- `user_address`: Address of the user.
- `user_branch_id`: Foreign key referencing the `branch_id` in the BRANCH table.

### CREDIT_CARD Table
- `crc_name`: Name of the credit card.
- `crc_id`: Unique identifier for each credit card.
- `crc_bal`: Balance amount on the credit card.
- `crc_type`: Type of the credit card.
- `crc_user_id`: Foreign key referencing the `user_id` in the USER1 table.

### LIMITS Table
- `limit_user_id`: Foreign key referencing the `user_id` in the USER1 table.
- `limit_bal`: Balance limit for the user.
- `limit_crc_id`: Foreign key referencing the `crc_id` in the CREDIT_CARD table.

### APPLICATIONS Table
- `app_num`: Application number.
- `app_user_id`: Foreign key referencing the `user_id` in the USER1 table.
- `app_type`: Type of application.

## Purpose

This database schema is designed to manage information related to branches, users, credit cards, credit limits, and applications within an organization. The tables are structured to maintain data integrity and enforce relationships between entities through the use of primary keys and foreign key constraints.

The schema allows for the tracking of branch details, user information, credit card details, credit limits, and applications submitted by users. By linking tables through foreign key relationships, it ensures referential integrity and facilitates efficient data retrieval and management.

## Usage

To use this database schema, you can execute the provided SQL statements using a compatible database management system (DBMS) or query tool. The schema creation process involves executing each CREATE TABLE statement in the specified order to create the necessary tables and define the columns and constraints.

Once the schema is created, you can start populating the tables with relevant data by executing appropriate INSERT INTO statements.

To query the data, you can use SQL statements like SELECT, INSERT, UPDATE, and DELETE to perform operations on the tables and retrieve the desired information.

It is important to ensure that the necessary database privileges are granted to the user executing the SQL statements to avoid any permission-related issues.

## Database Relationships

The database schema establishes the following relationships between tables:

- The USER1 table has a foreign key constraint referencing the BRANCH table, indicating that each user belongs to a specific branch.
- The CREDIT_CARD table has a foreign key constraint referencing the USER1 table, indicating that each credit card is associated with a specific user.
- The LIMITS table has a foreign key constraint referencing the CREDIT_CARD table, indicating that each credit limit is associated with a specific credit card.
- The APPLICATIONS table has a foreign key constraint referencing the USER1 table, indicating that each application is submitted by a specific user.

These relationships help maintain data consistency and enable data retrieval across related entities.


## Window Output

The application provides a graphical user interface (GUI) built using Tkinter. Upon running the application, a window is displayed with various fields, labels, and buttons for performing different operations. The main class name used in the application is `CreditCardApp`.

### Fields
- Input fields are provided for entering data such as branch ID, branch name, user ID, user name, credit card ID, etc.

### Labels
- Labels are used to provide descriptive text for each input field, indicating what information should be entered.

### Buttons
- Buttons are provided for executing various actions such as inserting data, updating data, deleting data, retrieving data, and viewing all data.

## Usage

1. Clone the repository.
2. Install the required dependencies:
   - Python (latest version)
   - Tkinter: Tkinter is included with Python. No separate installation is required.
3. Run the main script (`credit_card_gui.py`) to launch the application.



## Contribution

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
