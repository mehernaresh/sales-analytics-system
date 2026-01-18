def customer_analysis(transactions):
    """
    Analyzes customer purchase patterns.

    Parameters:
        transactions (list): list of transaction dictionaries

    Returns:
        dict: customer statistics in format:
        {
            'C001': {
                'total_spent': 95000.0,
                'purchase_count': 3,
                'avg_order_value': 31666.67,
                'products_bought': ['Laptop', 'Mouse', 'Keyboard']
            },
            ...
        }

    Requirements:
    - Calculate total amount spent per customer
    - Count number of purchases
    - Calculate average order value
    - List unique products bought
    - Sort by total_spent descending
    """

    customer_stats = {}

    # Aggregate by CustomerID
    for txn in transactions:
        cust_id = txn["CustomerID"]
        amount = txn["Quantity"] * txn["UnitPrice"]
        product = txn["ProductName"]

        if cust_id not in customer_stats:
            customer_stats[cust_id] = {
                "total_spent": 0.0,
                "purchase_count": 0,
                "products_bought": set(),
            }

        customer_stats[cust_id]["total_spent"] += amount
        customer_stats[cust_id]["purchase_count"] += 1
        customer_stats[cust_id]["products_bought"].add(product)

    # Finalize stats
    for cust_id, stats in customer_stats.items():
        stats["avg_order_value"] = round(
            stats["total_spent"] / stats["purchase_count"], 2
        )
        stats["products_bought"] = sorted(list(stats["products_bought"]))

    # Sort by total_spent descending
    sorted_stats = dict(
        sorted(customer_stats.items(), key=lambda x: x[1]["total_spent"], reverse=True)
    )

    return sorted_stats