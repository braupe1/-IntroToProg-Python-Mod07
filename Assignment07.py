# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Binary File Assignment,
# ChangeLog (Who,When,What):
# BRaupe,2023.05.28,Created started script
# BRaupe,2023.05.29,Added Try-Except and created Processor Class
# ---------------------------------------------------------------------------- #

import pickle
from datetime import datetime

# Define the name of the file where the data will be saved
filename = 'AppData.dat'

class Processor:
    investment_data = []

    # Function to read data from the file
    @staticmethod
    def read_data():
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)

        except FileNotFoundError:
            print(f"File '{filename}' not found. No data loaded.")
            return []  # return an empty list if the file does not exist

        except EOFError:
            print("File is empty or in an invalid format. Starting with empty data.")
            return []  # return an empty list if the file is empty or in an invalid format

        except Exception as e:
            print("An error occurred while reading the file:", e)
            return []  # return an empty list in case of any other exceptions

    # Function to write data to the file
    @staticmethod
    def write_data():
        with open(filename, 'wb') as f:
            pickle.dump(Processor.investment_data, f)

    @staticmethod
    def enter_new_data():
        # Prompt the user to enter the date and value of their investment
        try:
            date = input("Enter the date (yyyy-mm-dd): ")
            datetime.strptime(date, '%Y-%m-%d')
            value = input("Enter the value of the investment: ")
            value = float(value) # Check if the entered value is a number
        except ValueError:
            print("Incorrect date format or investment value. Date should be YYYY-MM-DD and value should be a number.")
            return

        # Add the new data to the list
        Processor.investment_data.append({"Date": date, "Value": value})

        # Save the data to the file immediately
        Processor.write_data()
        print(f"Data saved successfully to {filename}")
        print("******* The current Date/Investment Values are: *******")
        print("Date", "\t\t\t", "Investment Value")
        # Sort the investment data by date in descending order
        Processor.investment_data.sort(key=lambda x: datetime.strptime(x["Date"], '%Y-%m-%d'), reverse=True)
        for row in Processor.investment_data:
            print(row["Date"], "\t\t", row["Value"])
        print("*******************************************")

def main():
    # Load the existing data when the program starts
    Processor.investment_data = Processor.read_data()

    while True:
        print("\nMenu:")
        print("1. Read data")
        print("2. Enter new data")
        print("3. Exit")
        selection = input("Enter your selection: ")

        if selection == '1':
            print("******* The current Date/Investment Values are: *******")
            print("Date","\t\t\t","Investment Value")
            # Sort the investment data by date in descending order
            Processor.investment_data.sort(key=lambda x: datetime.strptime(x["Date"], '%Y-%m-%d'), reverse=True)
            for row in Processor.investment_data:
                print(row["Date"],"\t\t", row["Value"])
            print("*******************************************")
        elif selection == '2':
            Processor.enter_new_data()
        elif selection == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid selection, please enter 1, 2 or 3.")

if __name__ == '__main__':
    main()
