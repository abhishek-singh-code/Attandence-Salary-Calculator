name = input("Enter Employee Name: ")
monthly_salary = int(input("Enter Monthly Salary of Employee: "))
absent_days = int(input("Enter Total Absent Days: "))

working_day = 26
duty_hours = 8
present_day = working_day - absent_days
per_day_pay = monthly_salary/working_day
per_hour_pay = per_day_pay/duty_hours


if(absent_days>working_day or absent_days<0):
    print("Error: Absent days must be between 0 and 26")

else:
    overtime_hour = int(input("Enter Overtime Hours: "))
    if(overtime_hour<0):
        print("Error : Overtime Hour cannot be negative")
    else:
        deduction = round(absent_days*per_day_pay)
        overtime_pay = round(overtime_hour * per_hour_pay * 1.5)
        final_salary = monthly_salary-deduction+overtime_pay
        print("\n--- Employee Salary Details ---")
        print("Name: ",name)
        print("Monthly Salary: ₹",monthly_salary)
        print("Working Days: ",working_day)
        print("Present Days: ",present_day)
        if(absent_days>0):
            print("Absent Days: ",absent_days)
            print("Salary Deduction: ",(deduction))
        if(overtime_hour>0):
            print("Overtime Hours: ",overtime_hour)
            print("Overtime Pay: ",overtime_pay)
        
        print("Final Salary: ₹",(final_salary))



