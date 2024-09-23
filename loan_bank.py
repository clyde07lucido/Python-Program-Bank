monthly_salary = input("Enter your monthly salary: ")
loan_amount = input("Enter your loan amount: ")

min_salary = 30000
max_loan_amount = 10 * monthly_salary

if monthly_salary >= min_salary and loan_amount <= max_loan_amount:
    print("You are eligible for the loan.")