import os
from utils.file_handler import read_sales_data
from utils.parse_transactions import parse_transactions
from utils.validate_filter import validate_and_filter
from utils.total_revenue import calculate_total_revenue
from utils.region_wise_sales import region_wise_sales
from utils.top_selling_products import top_selling_products
from utils.customer_analysis import customer_analysis
from utils.daily_sales_trend import daily_sales_trend
from utils.peak_sales_day import find_peak_sales_day
from utils.low_performing_products import low_performing_products
from utils.api_handler import fetch_all_products, create_product_mapping, enrich_sales_data
from utils.report_generator import generate_sales_report

def main():
    """
    Main execution function
    """

    try:
        # Welcome message
        print("=======================================")
        print("        SALES ANALYTICS SYSTEM")
        print("=======================================")

        # [1/10] Reading sales data
        print("\n[1/10] Reading sales data...")
        transactions_raw = read_sales_data("data/sales_data.txt")
        print(f"✓ Successfully read {len(transactions_raw)} transactions")

        # [2/10] Parsing and cleaning data
        print("\n[2/10] Parsing and cleaning data...")
        transactions = parse_transactions(transactions_raw)
        print(f"✓ Parsed {len(transactions)} records")

        # [3/10] Filter Options Available
        print("\n[3/10] Filter Options Available:")
        regions = sorted(set(txn["Region"] for txn in transactions))
        amounts = [txn["UnitPrice"] for txn in transactions]
        print(f"Regions: {', '.join(regions)}")
        print(f"Amount Range: ₹{min(amounts)} - ₹{max(amounts)}")

        # [4/10] Validating transactions
        print("\n[4/10] Validating transactions...")
        
        choice = input("\nDo you want to filter data? (y/n): ").strip().lower()
        if choice == "y":
            region_choice = input("Enter region to filter (or press Enter to skip): ").strip()
            min_amt = float(input("Enter minimum amount (or press Enter to skip): ").strip())
            max_amt = float(input("Enter maximum amount (or press Enter to skip): ").strip())
            valid_txns, invalid_count = validate_and_filter(transactions, region_choice, min_amt, max_amt)
            print(f"✓ Valid: {len(valid_txns)} | Invalid: {invalid_count}")
        else:
            valid_txns, invalid_count = validate_and_filter(transactions)
            print(f"✓ Valid: {len(valid_txns)} | Invalid: {invalid_count}")

        # [5/10] Performing analysis
        print("\n[5/10] Analyzing sales data...")
        _ = calculate_total_revenue(valid_txns)
        _ = region_wise_sales(valid_txns)
        _ = top_selling_products(valid_txns)
        _ = customer_analysis(valid_txns)
        _ = daily_sales_trend(valid_txns)
        _ = find_peak_sales_day(valid_txns)
        _ = low_performing_products(valid_txns)
        print("✓ Analysis complete")

        # [6/10] Fetching product data
        print("\n[6/10] Fetching product data from API...")
        api_products = fetch_all_products()
        product_mapping = create_product_mapping(api_products)
        print(f"✓ Fetched {len(api_products)} products")

        # [7/10] Enriching sales data
        print("\n[7/10] Enriching sales data...")
        enriched_txns = enrich_sales_data(valid_txns, product_mapping)
        enriched_count = sum(1 for txn in enriched_txns if txn.get("API_Match"))
        success_rate = round((enriched_count / len(enriched_txns)) * 100, 2) if enriched_txns else 0
        print(f"✓ Enriched {enriched_count}/{len(enriched_txns)} transactions ({success_rate}%)")

        # [8/10] Saving enriched data
        print("\n[8/10] Saving enriched data...")
        print("✓ Saved to: data/enriched_sales_data.txt")

        # [9/10] Generating report
        print("\n[9/10] Generating report...")
        generate_sales_report(valid_txns, enriched_txns)
        print("✓ Report saved to: output/sales_report.txt")

        # [10/10] Completion
        print("\n[10/10] Process Complete!")
        print("=======================================")

    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Process terminated gracefully.")

if __name__ == "__main__":
    main()