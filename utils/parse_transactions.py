def parse_transactions(raw_lines):
    """
    Parses raw lines into clean list of dictionaries.

    Returns:
        list of dictionaries with keys:
        ['TransactionID', 'Date', 'ProductID', 'ProductName',
         'Quantity', 'UnitPrice', 'CustomerID', 'Region']

    Requirements:
    - Split by pipe delimiter '|'
    - Handle commas within ProductName (remove or replace)
    - Remove commas from numeric fields and convert to proper types
    - Convert Quantity to int
    - Convert UnitPrice to float
    - Skip rows with incorrect number of fields
    """

    transactions = []

    for line in raw_lines:
        parts = line.split("|")

        # Skip rows with incorrect number of fields
        if len(parts) != 8:
            continue

        txn_id, date, product_id, product_name, qty_str, price_str, customer_id, region = parts

        # Clean ProductName: remove commas
        product_name = product_name.replace(",", " ").strip()

        # Clean numeric fields: remove commas, convert to proper types
        try:
            quantity = int(qty_str.replace(",", "").strip())
            unit_price = float(price_str.replace(",", "").strip())
        except ValueError:
            # Skip if numeric conversion fails
            continue

        # Build transaction dictionary
        transaction = {
            "TransactionID": txn_id.strip(),
            "Date": date.strip(),
            "ProductID": product_id.strip(),
            "ProductName": product_name,
            "Quantity": quantity,
            "UnitPrice": unit_price,
            "CustomerID": customer_id.strip(),
            "Region": region.strip(),
        }

        transactions.append(transaction)

    return transactions