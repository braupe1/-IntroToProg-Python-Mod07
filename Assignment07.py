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

# Processing  --------------------------------------------------------------- #
class Processor: # Class to group applicable functions
    investment_data = [] # Initialize list to hold investment data set

    # Function to read data from the file
    @staticmethod
    def read_data():
        try: # Pickle binary file processing
            with open(filename, 'rb') as f:
                return pickle.load(f)

        except FileNotFoundError: # Exception if file not loaded
            print(f"File '{filename}' not found. No data loaded.")
            return []  # return an empty list if the file does not exist

        except EOFError: # Exception if file not loaded
            print("File is empty or in an invalid format. Starting with empty data.")
            return []  # return an empty list if the file is empty or in an invalid format

        except Exception as e: # Exception if file not loaded
            print("An error occurred while reading the file:", e)
            return []  # return an empty list in case of any other exceptions

    # Function to write data to the file
    @staticmethod
    def write_data(): # Binary file write this can be a write or append depending upon need
        with open(filename, 'wb') as f:
            pickle.dump(Processor.investment_data, f)

    @staticmethod
    def enter_new_data(): # New data entry capture
        # Prompt the user to enter the date and value of their investment
        try:
            date = input("Enter the date (yyyy-mm-dd): ") # Date input entry
            datetime.strptime(date, '%Y-%m-%d') # Date format
        except ValueError:
            print("Incorrect date format. Date should be YYYY-MM-DD.")
            return
        try:
            value = float(input("Enter the value of the investment: ")) # Dollar value input
        except ValueError:
            print("Investment value must be numeric.")
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

# Presentation (Input/Output)  -------------------------------------------- #
def main():
    # Load the existing data when the program starts
    Processor.investment_data = Processor.read_data()

    while True: # Menu of options display
        print("\nMenu:")
        print("1) Read data")
        print("2) Enter new data")
        print("3) Exit")
        selection = input("Enter your selection: ")

        if selection == '1': # Selection 1 if statement if read data is selected
            print("******* The current Date/Investment Values are: *******") # Format display header
            print("Date","\t\t\t","Investment Value") # Format display header
            # Attempt to sort the investment data by date in descending order
            Processor.investment_data.sort(key=lambda x: datetime.strptime(x["Date"], '%Y-%m-%d'), reverse=True)
            for row in Processor.investment_data: # For loop to display data
                print(row["Date"],"\t\t", row["Value"])
            print("*******************************************")
        elif selection == '2': # Selection 2 for new data entered
            Processor.enter_new_data()
        elif selection == '3': # Exit Selection
            print("Goodbye!")
            break
        else: # Request user to enter values 1-3
            print("Invalid selection, please enter 1, 2 or 3.")

# Main Body of Script  ------------------------------------------------------ #
# Main script call
if __name__ == '__main__':
    main()
