# Credit Card Management System

This is a Python application built using Tkinter and SQLite for managing credit card data. The application provides functionality for inserting, updating, deleting, retrieving, and viewing all data stored in the database.

## Features

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


