import csv
from datetime import datetime

# Global variables
expense_file = "expenses.csv"

# Function to add an expense
def add_expense():
    date = input("Enter the date (YYYY-MM-DD) [Leave blank for today]: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    amount = input("Enter the amount spent: ")
    description = input("Enter a brief description of the expense: ")
    category = input("Enter the category (e.g., food, transportation, entertainment): ")

    with open(expense_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, description, category])

    print("Expense added successfully!")

# Function to display all expenses
def view_expenses():
    print("\n--- All Expenses ---")
    with open(expense_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Date: {row[0]}, Amount: {row[1]}, Description: {row[2]}, Category: {row[3]}")
    print("---------------------\n")

# Function to view summary by category
def view_category_summary():
    categories = {}
    with open(expense_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            category = row[3]
            amount = float(row[1])
            categories[category] = categories.get(category, 0) + amount
    
    print("\n--- Category-wise Summary ---")
    for category, total in categories.items():
        print(f"{category}: {total}")
    print("-----------------------------\n")

# Function to display monthly summary
def view_monthly_summary():
    monthly = {}
    with open(expense_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            date = row[0]
            month = date[:7]  # Extract YYYY-MM
            amount = float(row[1])
            monthly[month] = monthly.get(month, 0) + amount
    
    print("\n--- Monthly Summary ---")
    for month, total in monthly.items():
        print(f"{month}: {total}")
    print("----------------------\n")

# Error handling for invalid input
def get_valid_input(prompt, options):
    while True:
        choice = input(prompt).lower()
        if choice in options:
            return choice
        else:
            print(f"Invalid choice. Please choose from {options}.")

# Main function
def main():
    print("Welcome to the Expense Tracker!")
    
    # Initialize CSV file if it doesn't exist
    try:
        with open(expense_file, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Description", "Category"])
    except FileExistsError:
        pass

    while True:
        print("\nMenu:")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. View category-wise summary")
        print("4. View monthly summary")
        print("5. Exit")
        
        choice = get_valid_input("Enter your choice: ", ['1', '2', '3', '4', '5'])

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            view_category_summary()
        elif choice == '4':
            view_monthly_summary()
        elif choice == '5':
            print("Exiting the Expense Tracker. Goodbye!")
            break

if __name__ == "__main__":
    main()
