name = input("Enter Employee Name: ")
monthly_salary = int(input("Enter monthly salary of employee: "))
working_day = 26
present_day = int(input("Enter total present days: "))

if(present_day>working_day):
    print("Error present day cannot be more than working day")
else:
    absent_days = working_day - present_day
    per_day_salary = monthly_salary/working_day
    deduction = round(absent_days*per_day_salary)
    final_salary = monthly_salary-deduction

    print("\n--- Employee Salary Details ---")
    print("Name: ",name)
    print("Monthly Salary: ₹",monthly_salary)
    print("Working Days: ",working_day)
    print("Present days: ",present_day)
    print("Absent days: ",absent_days)
    print("Salary Deduction: ",(deduction))
    print("Final Salary: ₹",(final_salary))


