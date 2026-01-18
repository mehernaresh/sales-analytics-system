def daily_sales_trend(transactions):
    """
    Analyzes sales trends by date.

    Parameters:
        transactions (list): list of transaction dictionaries

    Returns:
        dict: daily statistics in format:
        {
            '2024-12-01': {
                'revenue': 125000.0,
                'transaction_count': 8,
                'unique_customers': 6
            },
            ...
        }

    Requirements:
    - Group by date
    - Calculate daily revenue
    - Count daily transactions
    - Count unique customers per day
    - Sort chronologically
    """

    daily_stats = {}

    # Aggregate by Date
    for txn in transactions:
        date = txn["Date"]
        amount = txn["Quantity"] * txn["UnitPrice"]
        cust_id = txn["CustomerID"]

        if date not in daily_stats:
            daily_stats[date] = {
                "revenue": 0.0,
                "transaction_count": 0,
                "unique_customers": set(),
            }

        daily_stats[date]["revenue"] += amount
        daily_stats[date]["transaction_count"] += 1
        daily_stats[date]["unique_customers"].add(cust_id)

    # Finalize stats: convert sets to counts
    for date, stats in daily_stats.items():
        stats["unique_customers"] = len(stats["unique_customers"])

    # Sort chronologically by date
    sorted_stats = dict(sorted(daily_stats.items(), key=lambda x: x[0]))

    return sorted_stats