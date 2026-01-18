def calculate_total_revenue(transactions):
    """
    Calculates total revenue from all transactions.

    Parameters:
        transactions (list): list of transaction dictionaries

    Returns:
        float: total revenue (sum of Quantity * UnitPrice)
    """

    total = sum(txn["Quantity"] * txn["UnitPrice"] for txn in transactions)
    return total