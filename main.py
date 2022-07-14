# Monthly expenses
monthly_expenses = {
    'rent': 1200,
    'utilities': 300,
    'transport': 450,
    'food': 600,
    'entertainment': 110,
    'clothing': 220,
    'health': 30,
    'internet': 60,
    'education': 200,
    'other': 100
}

# Calculate the total expenses
def total_expenses(monthly_expenses: dict) -> int:
    """
    Calculate the total expenses
    Args:
        monthly_expenses: dictionary of monthly expenses
    Returns:
        total_expenses: total expenses
    """
    total = 0
    for k in monthly_expenses.keys():
        total += monthly_expenses[k]
    return total
print(total_expenses(monthly_expenses))
# Find the least expensive expense
def least_expensive(monthly_expenses: dict) -> str:
    """
    Find the least expensive expense
    Args:
        monthly_expenses: dictionary of monthly expenses
    Returns:
        least_expensive: least expensive expense
    """
    min_v = list(monthly_expenses.values())[0]
    ans = list(monthly_expenses.keys())[0]
    for k,v in monthly_expenses.items():
        if min_v>v:
            min_v = v
            ans = k
    return ans
print(least_expensive(monthly_expenses))
# Find the most expensive expense
def most_expensive(monthly_expenses: dict) -> str:
    """
    Find the most expensive expense
    Args:
        monthly_expenses: dictionary of monthly expenses
    Returns:
        most_expensive: most expensive expense
    """
    mac_v = list(monthly_expenses.values())[0]
    ans = list(monthly_expenses.keys())[0]
    for k,v in monthly_expenses.items():
        if mac_v<v:
            mac_v = v
            ans = k
    return ans 
print(most_expensive(monthly_expenses))    