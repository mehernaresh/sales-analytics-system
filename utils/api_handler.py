import requests
import re

# ============================================================
# Task 3.1: Fetch Product Details
# ============================================================

BASE_URL = "https://dummyjson.com/products"

def fetch_all_products():
    """
    Fetches all products from DummyJSON API.

    Returns:
        list of product dictionaries in format:
        [
            {
                'id': 1,
                'title': 'iPhone 9',
                'category': 'smartphones',
                'brand': 'Apple',
                'price': 549,
                'rating': 4.69
            },
            ...
        ]

    Requirements:
    - Fetch all available products (use limit=120 to be able to map with product ID)
    - Handle connection errors with try-except
    - Return empty list if API fails
    - Print status message (success/failure)
    """
    try:
        response = requests.get(f"{BASE_URL}?limit=120")
        response.raise_for_status()
        data = response.json()
        products = data.get("products", [])
        print(f"Successfully fetched {len(products)} products.")

        # Extract only required fields
        cleaned_products = [
            {
                "id": p["id"],
                "title": p["title"],
                "category": p["category"],
                "brand": p.get("brand", ""),
                "price": p["price"],
                "rating": p["rating"],
            }
            for p in products
        ]

        print(f"Successfully cleaned {len(cleaned_products)} products.")
        return cleaned_products

    except Exception as e:
        print(f"Failed to fetch products: {e}")
        return []


def create_product_mapping(api_products):
    """
    Creates a mapping of product IDs to product info.

    Parameters:
        api_products (list): list of product dictionaries from fetch_all_products()

    Returns:
        dict: mapping of product IDs to info in format:
        {
            1: {'title': 'iPhone 9', 'category': 'smartphones', 'brand': 'Apple', 'rating': 4.69},
            2: {'title': 'iPhone X', 'category': 'smartphones', 'brand': 'Apple', 'rating': 4.44},
            ...
        }
    """
    product_mapping = {
        product["id"]: {
            "title": product["title"],
            "category": product["category"],
            "brand": product["brand"],
            "rating": product["rating"],
        }
        for product in api_products
    }

    return product_mapping


# ============================================================
# Task 3.2: Enrich Sales Data
# ============================================================

def enrich_sales_data(transactions, product_mapping):
    """
    Enriches transaction data with API product information.

    Parameters:
        transactions (list): list of transaction dictionaries
        product_mapping (dict): dictionary from create_product_mapping()

    Returns:
        list of enriched transaction dictionaries

    Enrichment Logic:
    - Extract numeric ID from ProductID (P101 → 101, P5 → 5)
    - If ID exists in product_mapping, add API fields
    - If ID doesn't exist, set API_Match to False and other fields to None
    - Handle all errors gracefully
    - Save enriched data to 'data/enriched_sales_data.txt'
    """

    enriched_transactions = []

    for txn in transactions:
        enriched_txn = txn.copy()

        try:
            # Extract numeric ID from ProductID (e.g., P101 -> 101)
            match = re.search(r"\d+", txn["ProductID"])
            product_id_num = int(match.group()) if match else None

            if product_id_num and product_id_num in product_mapping:
                api_info = product_mapping[product_id_num]
                enriched_txn["API_Category"] = api_info.get("category")
                enriched_txn["API_Brand"] = api_info.get("brand")
                enriched_txn["API_Rating"] = api_info.get("rating")
                enriched_txn["API_Match"] = True
            else:
                enriched_txn["API_Category"] = None
                enriched_txn["API_Brand"] = None
                enriched_txn["API_Rating"] = None
                enriched_txn["API_Match"] = False

        except Exception:
            # Graceful error handling
            enriched_txn["API_Category"] = None
            enriched_txn["API_Brand"] = None
            enriched_txn["API_Rating"] = None
            enriched_txn["API_Match"] = False

        enriched_transactions.append(enriched_txn)

    # Save enriched data to file
    save_enriched_data(enriched_transactions)

    return enriched_transactions


def save_enriched_data(enriched_transactions, filename="data/enriched_sales_data.txt"):
    """
    Saves enriched transactions back to file.

    Expected File Format:
    TransactionID|Date|ProductID|ProductName|Quantity|UnitPrice|CustomerID|Region|API_Category|API_Brand|API_Rating|API_Match

    Requirements:
    - Create output file with all original + new fields
    - Use pipe delimiter
    - Handle None values appropriately
    """

    header = [
        "TransactionID", "Date", "ProductID", "ProductName",
        "Quantity", "UnitPrice", "CustomerID", "Region",
        "API_Category", "API_Brand", "API_Rating", "API_Match"
    ]

    try:
        with open(filename, "w", encoding="utf-8") as f:
            # Write header
            f.write("|".join(header) + "\n")

            # Write each transaction
            for txn in enriched_transactions:
                row = [
                    str(txn.get("TransactionID", "")),
                    str(txn.get("Date", "")),
                    str(txn.get("ProductID", "")),
                    str(txn.get("ProductName", "")),
                    str(txn.get("Quantity", "")),
                    str(txn.get("UnitPrice", "")),
                    str(txn.get("CustomerID", "")),
                    str(txn.get("Region", "")),
                    str(txn.get("API_Category", "")) if txn.get("API_Category") is not None else "",
                    str(txn.get("API_Brand", "")) if txn.get("API_Brand") is not None else "",
                    str(txn.get("API_Rating", "")) if txn.get("API_Rating") is not None else "",
                    str(txn.get("API_Match", "")),
                ]
                f.write("|".join(row) + "\n")

        print(f"Enriched data successfully saved to {filename}")

    except Exception as e:
        print(f"Failed to save enriched data: {e}")