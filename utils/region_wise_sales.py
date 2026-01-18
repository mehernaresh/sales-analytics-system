def region_wise_sales(transactions):
    """
    Analyzes sales by region.

    Parameters:
        transactions (list): list of transaction dictionaries

    Returns:
        dict: region statistics in format:
        {
            'North': {
                'total_sales': 450000.0,
                'transaction_count': 15,
                'percentage': 29.13
            },
            ...
        }

    Requirements:
    - Calculate total sales per region
    - Count transactions per region
    - Calculate percentage of total sales
    - Sort by total_sales in descending order
    """

    region_stats = {}
    total_sales = 0.0

    # Aggregate by region
    for txn in transactions:
        region = txn["Region"]
        amount = txn["Quantity"] * txn["UnitPrice"]

        if region not in region_stats:
            region_stats[region] = {"total_sales": 0.0, "transaction_count": 0}

        region_stats[region]["total_sales"] += amount
        region_stats[region]["transaction_count"] += 1
        total_sales += amount

    # Calculate percentages
    for region, stats in region_stats.items():
        stats["percentage"] = round((stats["total_sales"] / total_sales) * 100, 2)

    # Sort by total_sales descending
    sorted_stats = dict(
        sorted(region_stats.items(), key=lambda x: x[1]["total_sales"], reverse=True)
    )

    return sorted_stats