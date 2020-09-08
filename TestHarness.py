# ---------------------------------------------------------- #
# Title: Listing 12
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ---------------------------------------------------------- #
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from DataClasses import Person as P
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")


# Test Person Class
objP1 = P("Jim", "Baker")
objP2 = P("Lee", "Hudson")
lstTableP = [objP1, objP2]
for row in lstTableP:
    print(row.to_string(), type(row))

# Test Employee Class
objE1 = Emp(1, "Bob", "Smith")
objE2 = Emp(2, "Sue", "Jones")
lstTableE = [objE1, objE2]
for row in lstTableE:
    print(row.to_string(), type(row))

# Test processing module
lstTable = []
Fp.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string(), type(row))

# Test IO classes
Eio.print_menu_items()
Eio.print_current_list_items(lstTable)
print(Eio.input_employee_data())
print(Eio.input_menu_options())

