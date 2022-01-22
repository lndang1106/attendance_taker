# Attendence Taker
> A Python project for my Basics of Programming course at JAMK

This is a program for employees of a company (let's call it Toyota company) to take attendance on their own everyday. There are five main features in this program:

1. Taking attendance: employees enter today's date and if it matches today's date, the value corresponding to the key (staff number) in the ToyotaOy dictionary will be changed to today's date. If employees do not enter anything, the program will show a message reminding them to take attendance later.

2. Check if an employee took attendance today: tell employees whether they took attendance today or not, just in case they have bad memory and also to make sure that the program ran correctly.

3. View today's absent employees (only manager* can do this): this feature will show staff number of employees who were absent or did not take attendance today. Only manager can use this feature out of consideration for other employees' privacy.

4. Reset attendance list (only manager can do this): this feature will remove the value of keys in dictionary, which means all employees will become absent. Permission to use this feature is limited only to the manager to prevent unsolicited incidents.

5. Save today's attendance list (only manager can do this): this feature will write attendance list to a txt file. For example, the manager can save today's attendance list and then reset so that the program will be ready for another working day. Permission to use this feature is limited only to the manager to prevent unsolicited incidents.

(*) The manager that I assigned in this program is the employee with staff number 2110.

Every time the program is started, the first thing it does is to ask for employee's staff number. If the employee entered their staff number incorrectly more than 5 times, the program will automatically stop. After entering staff number, the employee will choose what to do (among those 5 actions above).