name = input("Enter Employee Name: ")
monthly_salary = int(input("Enter Monthly Salary of Employee: "))
present_day = int(input("Enter Total Present Days: "))
overtime_hour = int(input("Enter Overtime Hours: "))

working_day = 26
duty_hours = 8
per_day_pay = monthly_salary/working_day
per_hour_pay = per_day_pay/duty_hours



if(present_day>working_day or present_day<0):
    print("Error present day cannot be more than working day")
elif(overtime_hour<0):
    print("Error: Invalid overtime hours cannot be negative")
else:
    absent_days = working_day - present_day
    deduction = round(absent_days*per_day_pay)
    overtime_pay = round(overtime_hour * per_hour_pay * 1.5)
    final_salary = monthly_salary-deduction+overtime_pay

    print("\n--- Employee Salary Details ---")
    print("Name: ",name)
    print("Monthly Salary: ₹",monthly_salary)
    print("Working Days: ",working_day)
    print("Present Days: ",present_day)
    print("Absent Days: ",absent_days)
    print("Salary Deduction: ",(deduction))
    print("Overtime Hours: ",overtime_hour)
    print("Overtime Pay: ",overtime_pay)
    print("Final Salary: ₹",(final_salary))


