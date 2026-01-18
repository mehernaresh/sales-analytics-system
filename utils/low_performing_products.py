def low_performing_products(transactions, threshold=10):
    """
    Identifies products with low sales.

    Parameters:
        transactions (list): list of transaction dictionaries
        threshold (int): minimum quantity threshold (default=10)

    Returns:
        list of tuples in format:
        [
            (ProductName, TotalQuantity, TotalRevenue),
            ...
        ]

    Requirements:
    - Find products with total quantity < threshold
    - Include total quantity and revenue
    - Sort by TotalQuantity ascending
    """

    product_stats = {}

    # Aggregate by ProductName
    for txn in transactions:
        product = txn["ProductName"]
        qty = txn["Quantity"]
        revenue = txn["Quantity"] * txn["UnitPrice"]

        if product not in product_stats:
            product_stats[product] = {"quantity": 0, "revenue": 0.0}

        product_stats[product]["quantity"] += qty
        product_stats[product]["revenue"] += revenue

    # Filter products below threshold
    low_products = [
        (product, stats["quantity"], stats["revenue"])
        for product, stats in product_stats.items()
        if stats["quantity"] < threshold
    ]

    # Sort by total quantity ascending
    low_products.sort(key=lambda x: x[1])

    return low_products