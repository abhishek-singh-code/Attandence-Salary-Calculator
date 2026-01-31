
employee = {
        101:{"Name": "Santosh Paswan", "Salary": 18000},
        102:{"Name": "Mithun", "Salary": 15000},
        103:{"Name": "Birender", "Salary": 17500}

};

working_day = 26
duty_hours = 8

emp_id = int(input("Enter Employee Id: "))
if(emp_id not in employee):
    print("❌ Error: Employee ID not found")
else:
    name = employee[emp_id]["Name"]
    monthly_salary = employee[emp_id]["Salary"]

    print(f"\nEmployee Name   : {name}")
    print(f"Monthly Salary  : ₹{monthly_salary}")

absent_days = int(input("Enter Total Absent Days: "))

if(absent_days>working_day or absent_days<0):
    print("\nError: Absent days must be between 0 and 26")

else:
    overtime_hour = int(input("Enter Overtime Hours: "))
    if(overtime_hour<0):
        print("\nError : Overtime Hour cannot be negative")
    else:
        present_day = working_day - absent_days
        per_day_pay = monthly_salary/working_day
        per_hour_pay = per_day_pay/duty_hours

        deduction = round(absent_days*per_day_pay)
        overtime_pay = round(overtime_hour * per_hour_pay * 1.5)
        final_salary = monthly_salary-deduction+overtime_pay

        print("\n" + "-" * 35)
        print("     Employee Salary Details")
        print("-" * 35)

        print(f"Employee Name     : {name}")
        print(f"Monthly Salary    : ₹{monthly_salary}")
        print(f"Working Days      : {working_day}")
        print(f"Present Days      : {present_day}")
        
        if(absent_days>0):
            print(f"Absent Days       : {absent_days}")
            print(f"Salary Deduction  : {deduction}")
        
        if(overtime_hour>0):
            print(f"Overtime Hours    : {overtime_hour}")
            print(f"Overtime Pay      : {overtime_pay}")
        print("-" * 35)
        print(f"Final Salary      : ₹{final_salary}")
        print("-" * 35)




