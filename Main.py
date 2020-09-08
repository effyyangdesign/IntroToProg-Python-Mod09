# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# <Your Name>,<Today's Date>,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# TODO: Import Modules
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from DataClasses import Person as P
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")


# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body

Choice = ""

# Load data from file into a list of employee objects when script starts

lstFileData = Fp.read_data_from_file("EmployeeData.txt")
while True:
    # Show user a menu of options
    Eio.print_menu_items()
    # Get user's menu option choice
    Choice = Eio.input_menu_options()
    # Show user current data in the list of employee objects

    if Choice == "1":
        Eio.print_current_list_items(lstFileData)
        continue
    # Let user add data to the list of employee objects
    elif Choice == "2":
        Eio.input_employee_data(lstFileData)
        continue
    # let user save current data to file
    elif Choice == "3":
        Fp.save_data_to_file("EmployeeData.txt",lstFileData)
        continue
    # Let user exit program
    elif Choice == "4":
        print("bye")
        break

# Main Body of Script  ---------------------------------------------------- #
