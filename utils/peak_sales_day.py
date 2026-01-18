def find_peak_sales_day(transactions):
    """
    Identifies the date with highest revenue.

    Parameters:
        transactions (list): list of transaction dictionaries

    Returns:
        tuple: (date, revenue, transaction_count)

    Expected Output Format:
        ('2024-12-15', 185000.0, 12)
    """

    daily_stats = {}

    # Aggregate by Date
    for txn in transactions:
        date = txn["Date"]
        amount = txn["Quantity"] * txn["UnitPrice"]

        if date not in daily_stats:
            daily_stats[date] = {"revenue": 0.0, "transaction_count": 0}

        daily_stats[date]["revenue"] += amount
        daily_stats[date]["transaction_count"] += 1

    # Find peak sales day
    peak_date, peak_data = max(daily_stats.items(), key=lambda x: x[1]["revenue"])

    return (peak_date, peak_data["revenue"], peak_data["transaction_count"])