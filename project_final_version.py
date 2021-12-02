import sys
import datetime
import os.path

print("WELCOME TO TOYOTA LIMITED COMPANY!\n")
time = datetime.datetime.now()
today = time.strftime("%B %d")
print("Today is", today)

ToyotaOy = {
    2110: "",
    2130: "",
    1210: "",
    1213: "",
}

for i in range(5):
    try:
        staff_number = int(input("Please enter your staff number: "))
        date_present = ToyotaOy[staff_number]
    except:
        print("Please enter a valid staff number!")
    else:
        break
    if i == 4:
        sys.exit("You entered your staff number incorrectly 5 times!")

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
    today_MMMdd = time.strftime("%B %d")
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
    attendance_list = "\nToday is " + str(today) + "\n" + str(ToyotaOy).replace(", ", "\n").replace("{", "").replace("}", "") + "\n"
    manager_comment = input("Manager's comment before saving today's attendance list: ")

    path = os.path.expanduser("~/ToyotaOy")
    if not os.path.exists(path): os.makedirs(path)
    path += "/"

    filename = "AttendanceList.txt"
    file = open(path + filename, "a")
    file.write(attendance_list)
    file.write(manager_comment)
    file.close()

while True:
    print("\nA. Take attendance")
    print("B. Check if you took attendance today")
    print("C. View absent employees today")
    print("D. Reset")
    print("E. Save today's attendance list")
    command = input("Please choose one of the options above and press Enter to continue (or press Enter without choosing to enter another staff number): ")
    print("\n")
    if command == "A" or command == "a":
        attend()
    elif command == "B" or command == "b":
        check()
    elif command == "C" or command == "c":
        if staff_number == 2110:
            view_absent_emp()
        else:
            print("You are not authorized to do this!")
    elif command == "D" or command == "d":
        if staff_number == 2110:
            reset()
        else:
            print("You are not authorized to do this!")
    elif command == "E" or command == "e":
        if staff_number == 2110:
            save()
        else:
            print("You are not authorized to do this!")
    elif command == "":
        for i in range(5):
            try:
                staff_number = int(input("Please enter your staff number: "))
                date_present = ToyotaOy[staff_number]
            except KeyError:
                print("Please enter a valid staff number!")
            else:
                break
            if i == 4:
                sys.exit("You entered your staff number incorrectly 5 times!")
    elif command == "X" or command == "x":
        sys.exit("Program stopped!") 
    else:
        print("Please choose a valid option!")