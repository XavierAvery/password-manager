# Password Manager

This is a simple password manager application created using Python's Tkinter library. It allows users to generate strong passwords, save them along with corresponding website and email details, and search for passwords saved previously.

## Features
- **Password Generation:** The application can generate strong passwords with random combinations of letters, numbers, and symbols.
- **Password Saving:** Users can save their passwords along with website and email details securely.
- **Password Retrieval:** Users can search for previously saved passwords by entering the website name.

## Requirements
- Python 3.12
- Tkinter library
- pyperclip library

## Installation
1. Clone or download the repository.
2. Ensure you have Python installed on your system.
3. Install Tkinter and pyperclip libraries if not already installed:
    ```
    pip install tk
    pip install pyperclip
    ```
4. Run the application by executing the script.

## Usage
1. Run the script.
2. Enter the website, email/username, and password.
3. Click on the "Add" button to save the details.
4. To generate a password, click on the "Generate Password" button.
5. To search for a saved password, enter the website name and click on the "Search" button.

## File Structure
- **data.json:** JSON file to store the saved password details.
- **logo.png:** Logo image used in the application.

## Note
- Ensure that you remember the master password used to access this application.
- The password details are saved locally on your system. Make sure to keep the data file secure.

## Author
This application is developed by Xavier Avery.

