def top_selling_products(transactions, n=5):
    """
    Finds top n products by total quantity sold.

    Parameters:
        transactions (list): list of transaction dictionaries
        n (int): number of top products to return (default=5)

    Returns:
        list of tuples in format:
        [
            (ProductName, TotalQuantity, TotalRevenue),
            ...
        ]

    Requirements:
    - Aggregate by ProductName
    - Calculate total quantity sold
    - Calculate total revenue for each product
    - Sort by TotalQuantity descending
    - Return top n products
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

    # Convert to list of tuples
    product_list = [
        (product, stats["quantity"], stats["revenue"])
        for product, stats in product_stats.items()
    ]

    # Sort by quantity descending
    product_list.sort(key=lambda x: x[1], reverse=True)

    return product_list[:n]