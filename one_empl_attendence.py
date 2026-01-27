name = input("Enter employee name: ")
total_working_day = int(input("Enter total working days: "))
total_present_day = int(input("Enter total present days: "))
salary_per_day = int(input("Enter salary per day: "))

if(total_present_day>total_working_day):
    print("Error present day cannot be more than working day")
else:
    salary = total_present_day*salary_per_day
    print("\n--- Employee Salary Details ---")
    print("Name: ",name)
    print("Present days: ",total_present_day)
    print("Total Salary: ₹",salary)


