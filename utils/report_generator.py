import os
from datetime import datetime
from utils.total_revenue import calculate_total_revenue
from utils.region_wise_sales import region_wise_sales
from utils.top_selling_products import top_selling_products
from utils.customer_analysis import customer_analysis
from utils.daily_sales_trend import daily_sales_trend
from utils.peak_sales_day import find_peak_sales_day
from utils.low_performing_products import low_performing_products

def generate_sales_report(transactions, enriched_transactions, output_file="output/sales_report.txt"):
    """
    Generates a comprehensive formatted text report.

    Report Includes (in order):
    1. HEADER
    2. OVERALL SUMMARY
    3. REGION-WISE PERFORMANCE
    4. TOP 5 PRODUCTS
    5. TOP 5 CUSTOMERS
    6. DAILY SALES TREND
    7. PRODUCT PERFORMANCE ANALYSIS
    8. API ENRICHMENT SUMMARY
    """

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # HEADER
    report_lines = []
    report_lines.append("=" * 43)
    report_lines.append("          SALES ANALYTICS REPORT")
    report_lines.append(f"        Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append(f"        Records Processed: {len(transactions)}")
    report_lines.append("=" * 43)
    report_lines.append("")

    # OVERALL SUMMARY
    total_revenue = calculate_total_revenue(transactions)
    total_transactions = len(transactions)
    avg_order_value = round(total_revenue / total_transactions, 2) if total_transactions else 0
    dates = sorted(set(txn["Date"] for txn in transactions))
    date_range = f"{dates[0]} to {dates[-1]}" if dates else "N/A"

    report_lines.append("OVERALL SUMMARY")
    report_lines.append("-" * 44)
    report_lines.append(f"Total Revenue:        ₹{total_revenue:,.2f}")
    report_lines.append(f"Total Transactions:   {total_transactions}")
    report_lines.append(f"Average Order Value:  ₹{avg_order_value:,.2f}")
    report_lines.append(f"Date Range:           {date_range}")
    report_lines.append("")

    # REGION-WISE PERFORMANCE
    region_stats = region_wise_sales(transactions)
    report_lines.append("REGION-WISE PERFORMANCE")
    report_lines.append("-" * 44)
    report_lines.append("Region    Sales         % of Total  Transactions")
    for region, stats in region_stats.items():
        report_lines.append(
            f"{region:<8} ₹{stats['total_sales']:,.0f}   {stats['percentage']}%      {stats['transaction_count']}"
        )
    report_lines.append("")

    # TOP 5 PRODUCTS
    top_products = top_selling_products(transactions, n=5)
    report_lines.append("TOP 5 PRODUCTS")
    report_lines.append("-" * 44)
    report_lines.append("Rank  Product Name       Quantity   Revenue")
    for i, (name, qty, revenue) in enumerate(top_products, start=1):
        report_lines.append(f"{i:<5} {name:<18} {qty:<9} ₹{revenue:,.0f}")
    report_lines.append("")

    # TOP 5 CUSTOMERS
    customer_stats = customer_analysis(transactions)
    report_lines.append("TOP 5 CUSTOMERS")
    report_lines.append("-" * 44)
    report_lines.append("Rank  Customer ID   Total Spent   Orders")
    for i, (cust_id, stats) in enumerate(customer_stats.items(), start=1):
        if i > 5: break
        report_lines.append(
            f"{i:<5} {cust_id:<12} ₹{stats['total_spent']:,.0f}   {stats['purchase_count']}"
        )
    report_lines.append("")

    # DAILY SALES TREND
    daily_stats = daily_sales_trend(transactions)
    report_lines.append("DAILY SALES TREND")
    report_lines.append("-" * 44)
    report_lines.append("Date         Revenue       Transactions   Unique Customers")
    for date, stats in daily_stats.items():
        report_lines.append(
            f"{date:<12} ₹{stats['revenue']:,.0f}   {stats['transaction_count']:<12} {stats['unique_customers']}"
        )
    report_lines.append("")

    # PRODUCT PERFORMANCE ANALYSIS
    peak_day = find_peak_sales_day(transactions)
    low_products = low_performing_products(transactions)
    avg_per_region = {
        region: round(stats["total_sales"] / stats["transaction_count"], 2)
        for region, stats in region_stats.items()
    }

    report_lines.append("PRODUCT PERFORMANCE ANALYSIS")
    report_lines.append("-" * 44)
    report_lines.append(f"Best Selling Day: {peak_day[0]} (Revenue ₹{peak_day[1]:,.0f}, Transactions {peak_day[2]})")
    if low_products:
        report_lines.append("Low Performing Products:")
        for product, qty, revenue in low_products:
            report_lines.append(f"  {product:<15} Qty: {qty:<3} Revenue: ₹{revenue:,.0f}")
    else:
        report_lines.append("No low performing products found.")
    report_lines.append("Average Transaction Value per Region:")
    for region, avg_val in avg_per_region.items():
        report_lines.append(f"  {region:<8} ₹{avg_val:,.2f}")
    report_lines.append("")

    # API ENRICHMENT SUMMARY
    enriched_count = sum(1 for txn in enriched_transactions if txn.get("API_Match"))
    success_rate = round((enriched_count / len(enriched_transactions)) * 100, 2) if enriched_transactions else 0
    failed_products = [txn["ProductID"] for txn in enriched_transactions if not txn.get("API_Match")]

    report_lines.append("API ENRICHMENT SUMMARY")
    report_lines.append("-" * 44)
    report_lines.append(f"Total Products Enriched: {enriched_count}")
    report_lines.append(f"Success Rate: {success_rate}%")
    if failed_products:
        report_lines.append("Products Not Enriched:")
        for pid in failed_products:
            report_lines.append(f"  {pid}")
    else:
        report_lines.append("All products enriched successfully.")
    report_lines.append("")

    # Save to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    print(f"Sales report successfully generated at {output_file}")