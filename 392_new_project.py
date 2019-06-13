# Import Python's built-in csv module
import csv

def main():
    max_func()





def max_func():
    # Use DictReader
    # It creates an object that puts the values in each row to a key given by an optional parameter for fieldnames
    try:
        csv_file = csv.DictReader(open(r"C:\Users\Michael\Downloads\Records.csv"))
    except FileNotFoundError:
        print("Wrong file or file path")


    # Declares some variables to be used for comparison
    max_profit_amount = float(0.00)
    num_max_profit = int(0)
    max_profit_counter = -1

    # For each row of csv_file assign profit to the value of the row's Total Profit
    # Add one to the max_profit_counter which keeps track of the index
    # Index is set to -1 to account for the headers
    for row in csv_file:
        profit = float(row['Total Profit'])
        max_profit_counter += 1

        # If the current iterated row's 'Total Profit' is greater than the max_profit_amount(initially zero)
        # Assign the max_profit_amount to the current number being iterated
        # For the row that meets the if-condition, assign num_max_profit the row's Order ID
        if profit > max_profit_amount:
            max_profit_amount = profit
            num_max_profit = row["Order ID"]
            index_max_profit = max_profit_counter

    def print_max():
        # Below prints out the variables and formats the profit as a currency
        print("ORDER STATISTICS")
        print("******************************************************************")

        print(f"The max profit is: ", '$' + format(max_profit_amount, ',.2f'))
        print(f"Found in order #:   {num_max_profit}")
        print(f"At index value:     {index_max_profit}\n")

    print_max()

    return max_profit_amount





# Reestablish the variable csv_file
csv_file = csv.DictReader(open(r"C:\Users\Michael\Downloads\Records.csv"))

num_min_profit = int(0)
min_profit_counter = -1
#calls the value returned from the previous max function as it needs to use it for comparison
formin_max_profit_amount = max_func()

for row in csv_file:
    profit = float(row['Total Profit'])
    min_profit_counter += 1

    # Essentially the same as the min_profit_amount if block from above but...
    # Uses the formin_max_profit_amount to only change the value if it is smaller than profit being iterated
    if profit < formin_max_profit_amount:
        formin_max_profit_amount = profit
        num_min_profit = row["Order ID"]
        index_min_profit = min_profit_counter

# Below prints out the variables and formats the profit as a currency
print(f"The min profit is: ", '$' + format(formin_max_profit_amount, ',.2f'))
print(f"Found in order #:   {num_min_profit}")
print(f"At index value:     {index_min_profit}\n")






user_input_variable = input("Please enter an Order ID to locate: ")

# Reestablish the variable csv_file
csv_file = csv.DictReader(open(r"C:\Users\Michael\Downloads\Records.csv"))

# Tries to execute the following block
try:
    # For each in row in csv_file
    # If the row's Order ID matches the user input variable
    # Assigns the current rows Ship Date and Total Revenue to the appropriate variables
    for row in csv_file:
        if row['Order ID'] == user_input_variable:
            shipdate_input_variable = row['Ship Date']
            revenue_input_variable = float(row['Total Revenue'])

    # Below prints out the variables and formats the revenue as a currency
    print(f"Order ID:           {user_input_variable}")
    print(f"Ship Date:          {shipdate_input_variable}")
    print("Total Revenue:     ", '$' + format(revenue_input_variable, ',.2f'))

# Looks for a NameError since if no Order ID is found it will then attempt
# to print shipdate_input_variable which will not be assigned if Order Id is wrong
# Warns the user exception occurs and continues
except NameError:
    print("You have entered an invalid Order ID")
    pass



main()
