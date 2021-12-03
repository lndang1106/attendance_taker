import sys
import datetime
import os.path

# Greetings and current date pop up when the program starts
print("WELCOME TO TOYOTA LIMITED COMPANY!\n")
time = datetime.datetime.now()
today = time.strftime("%B %d")
print("Today is", today)

# Dictionary to save attendance data
ToyotaOy = {
    2110: "",
    2130: "",
    1210: "",
    1213: "",
}
# Dictionary that includes employees' information
ToyotaOy_Info = {
    2110: "",
    2130: "",
    1210: "",
    1213: "",
}

# Loop to ask for employee's staff number
for i in range(5):
    try:
        staff_number = int(input("Please enter your staff number: "))
        date_present = ToyotaOy[staff_number] # This is to check if the entered staff number exists
    except:
        print("Please enter a valid staff number!")
    else:
        break
    if i == 4:
        sys.exit("You entered your staff number incorrectly 5 times!")

# Class that contains employees' information
class StaffInfo:
    def __init__(self, name = "", title = "", salary = 0):
        self.name = name
        self.title = title
        self.salary = salary

    def __str__(self):
        return "Name: " + self.name + "\nTitle: " + self.title + "\nMonthly salary: " + str(self.salary) + " €"
# Each object is then saved to Toyota_Info dictionary
ToyotaOy_Info[2110] = StaffInfo("Dang", "Manager", 4500)
ToyotaOy_Info[2130] = StaffInfo("Onni", "Marketer", 3200)
ToyotaOy_Info[1210] = StaffInfo("Marry", "Accountant", 3000)
ToyotaOy_Info[1213] = StaffInfo("Paul", "Janitor", 2100)

# Functions (or features / options) 
def attend():
    time = datetime.datetime.now()
    today_mmdd = time.strftime("%m %d") 
    print("Please enter in \"mm dd\" format, both month and date are 2-digit numbers, for example 01 01 or 12 31")
    take_attendance = input("Which date do you want to take attendance? ")
    if take_attendance == str(today_mmdd):
        ToyotaOy[staff_number] = take_attendance
        print("Attendance taken successfully!")
    elif take_attendance == "":
        print("Remember to take attendance every workday!")
    else:
        print("You can only take attandence for today and please make sure you entered a valid date in correct format (for example 01 01 or 12 31)!")

def check():
    time = datetime.datetime.now()
    today_MMMdd = time.strftime("%B %d") # Date in first 3 letters and 2 digits form (Jan 01, Dec 31)
    if ToyotaOy[staff_number] != "":
        print("Employee " + str(staff_number) + " has already taken attendance today, on " + str(today_MMMdd) + ".")
    else:
        print(staff_number, "employee has NOT taken attendance today!")

def view_absent_emp():
    absent_emp = []
    for employee in ToyotaOy:
        if ToyotaOy[employee] == "":
            absent_emp.append(employee)
        else:
            pass
    print("Employees who are absent / have not taken attendance today:", absent_emp)

def reset():
    for employee in ToyotaOy:
        ToyotaOy[employee] = ""
    print("Attendance list reset successfully!")

def save():
    attendance_list = "\nToday is " + str(today) + "." + "\n" + str(ToyotaOy).replace(", ", "\n").replace("{", "").replace("}", "") + "\n"
    manager_comment = input("Manager's comment before saving today's attendance list: ")

    path = os.path.expanduser("~/ToyotaOy")
    if not os.path.exists(path): os.makedirs(path)
    path += "/"

    filename = "AttendanceList.txt"
    file = open(path + filename, "a") # Write to the end of a file
    file.write(attendance_list)
    file.write(manager_comment)
    file.close()
    print("Attendance list saved successfully!")

# Ask for employee's option(s): what they want to do with the program
while True:
    print("\nYou have logged in as employee with staff number " + str(staff_number) + ".")
    print("A. Take attendance")
    print("B. Check if you took attendance today")
    print("C. View employee's information") # Employees can only view their own information
    print("D. View today's absent employees") # Limited to only manager
    print("E. Reset attendance list") # Limited to only manager
    print("F. Save today's attendance list") # Limited to only manager
    command = input("Please choose one of the options above and press Enter to continue (or press Enter without choosing to enter another staff number): ")
    print("\n")
    if command == "A" or command == "a":
        attend()
    elif command == "B" or command == "b":
        check()
    elif command == "C" or command == "c":
        print("Employee " + str(staff_number) + "'s information:")
        print(ToyotaOy_Info[staff_number])
    elif command == "D" or command == "d":
        if staff_number == 2110: # if ... else condition to limit the permission to only manager
            view_absent_emp()
        else:
            print("You are not authorized to do this!")
    elif command == "E" or command == "e":
        if staff_number == 2110:
            confirm = (input("Do you want to reset attendance list? (Y/N): ")) # Ask for confirmation before resetting
            if confirm == "Y" or confirm == "y":
                reset()
            elif confirm == "N" or confirm == "n":
                print("Today's attendance list has not been reset.")
            else:
                print("Please enter a valid confirmation!")
        else:
            print("You are not authorized to do this!")
    elif command == "F" or command == "f":
        if staff_number == 2110:
            confirm = (input("Do you want to save today's attendance list? (Y/N): ")) # Ask for confirmation before saving
            if confirm == "Y" or confirm == "y":
                save()
            elif confirm == "N" or confirm == "n":
                print("Today's attendance list has not been saved.")
            else:
                print("Please enter a valid confirmation!")
        else:
            print("You are not authorized to do this!")
    elif command == "": # If an employee presses Enter when asked to choose an option, they will be disconnected
        for i in range(5):
            try: # They will have to enter their staff number again or another employee can enter their staff number to continue using the program
                staff_number = int(input("Please enter your staff number: "))
                date_present = ToyotaOy[staff_number]
            except:
                print("Please enter a valid staff number!")
            else:
                break
            if i == 4:
                sys.exit("You entered your staff number incorrectly 5 times!")
    elif command == "X" or command == "x": # If an employee enters X when asked to choose an option, the program will be shut down
        sys.exit("Program stopped!") 
    else:
        print("Please choose a valid option or enter X to close the program!")