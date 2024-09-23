monthly_salary = input("Enter your monthly salary: ")
loan_amount = input("Enter your loan amount: ")

min_salary = 30000
max_loan_amount = 10 * monthly_salary

if monthly_salary >= min_salary and loan_amount <= max_loan_amount:
    print("You are eligible for the loan.") 

    months_to_pay = int(input("How many months do you want to pay the loan? "))

# Calculate total amount to repay with interest
    interest_rate = 0.10
    total_amount = loan_amount * (1 + interest_rate)
    monthly_payment = total_amount / months_to_pay

    print(f"Total amount to repay (with 10% interest): {total_amount:.2f}")
    print(f"Monthly payment over {months_to_pay} months: {monthly_payment:.2f}")

else:
    if monthly_salary < min_salary:
            print("You are not approved for the loan: Your salary is below the minimum required salary of 30,000.00.")
    else:
            print("You are not approved for the loan: The loan amount requested exceeds the maximum allowed based on your salary.")