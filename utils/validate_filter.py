def validate_and_filter(transactions, region=None, min_amount=None, max_amount=None):
    """
    Validates transactions and applies optional filters.

    Parameters:
        transactions (list): list of transaction dictionaries
        region (str): filter by specific region (optional)
        min_amount (float): minimum transaction amount (Quantity * UnitPrice) (optional)
        max_amount (float): maximum transaction amount (optional)

    Returns:
        tuple: (valid_transactions, invalid_count)

    Validation Rules:
    - Quantity must be > 0
    - UnitPrice must be > 0
    - All required fields must be present
    - TransactionID must start with 'T'
    - ProductID must start with 'P'
    - CustomerID must start with 'C'

    Filter Display:
    - Print available regions to user before filtering
    - Print transaction amount range (min/max) to user
    - Show count of records after each filter applied
    """

    required_fields = [
        "TransactionID", "Date", "ProductID", "ProductName",
        "Quantity", "UnitPrice", "CustomerID", "Region"
    ]

    total_input = len(transactions)
    invalid_count = 0
    valid_records = []

    # Step 1: Validation
    for txn in transactions:
        # Check all required fields present
        if not all(field in txn and txn[field] for field in required_fields):
            invalid_count += 1
            continue

        # Check rules
        if txn["Quantity"] <= 0 or txn["UnitPrice"] <= 0:
            invalid_count += 1
            continue
        if not txn["TransactionID"].startswith("T"):
            invalid_count += 1
            continue
        if not txn["ProductID"].startswith("P"):
            invalid_count += 1
            continue
        if not txn["CustomerID"].startswith("C"):
            invalid_count += 1
            continue

        valid_records.append(txn)

    # Step 2: Display available regions
    regions = sorted(set(txn["Region"] for txn in valid_records if txn.get("Region")))
    print(f"Available regions: {', '.join(regions)}")

    # Step 3: Display transaction amount range
    amounts = [txn["Quantity"] * txn["UnitPrice"] for txn in valid_records]
    if amounts:
        print(f"Transaction amount range: min={min(amounts)}, max={max(amounts)}")

    # Step 4: Apply filters
    filtered_by_region = 0
    filtered_by_amount = 0
    filtered_records = valid_records

    if region:
        before = len(filtered_records)
        filtered_records = [txn for txn in filtered_records if txn["Region"] == region]
        filtered_by_region = before - len(filtered_records)
        print(f"Records after region filter ({region}): {len(filtered_records)}")

    if min_amount is not None or max_amount is not None:
        before = len(filtered_records)
        filtered_records = [
            txn for txn in filtered_records
            if (min_amount is None or txn["Quantity"] * txn["UnitPrice"] >= min_amount)
            and (max_amount is None or txn["Quantity"] * txn["UnitPrice"] <= max_amount)
        ]
        filtered_by_amount = before - len(filtered_records)
        print(f"Records after amount filter: {len(filtered_records)}")

    # Step 5: Summary
    filter_summary = {
        "total_input": total_input,
        "invalid": invalid_count,
        "filtered_by_region": filtered_by_region,
        "filtered_by_amount": filtered_by_amount,
        "final_count": len(filtered_records),
    }

    return filtered_records, invalid_count