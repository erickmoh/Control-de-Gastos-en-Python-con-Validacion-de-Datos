def get_number(message):
    while True:
        try:
            value = float(input(message))
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please try again.")


def calculate_expenses(rent, food, transportation):
    return rent + food + transportation


def show_results(income, expenses):
    remaining = income - expenses
    print("\n--- RESULTS ---")
    print(f"Monthly income: ${income:.2f}")
    print(f"Total expenses: ${expenses:.2f}")
    print(f"Remaining balance: ${remaining:.2f}")

    if remaining < 0:
        print("⚠️ You are in deficit. Reduce expenses.")
    elif remaining < income * 0.2:
        print("⚠️ Low savings. Consider adjusting your expenses.")
    else:
        print("✅ Good financial management.")


def main():
    print("=== EXPENSE TRACKER ===")

    income = get_number("Enter monthly income: ")
    rent = get_number("Enter rent expense: ")
    food = get_number("Enter food expense: ")
    transportation = get_number("Enter transportation expense: ")

    expenses = calculate_expenses(rent, food, transportation)
    show_results(income, expenses)


if __name__ == "__main__":
    main()