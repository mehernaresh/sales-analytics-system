**Sales Analytics System**

Student Name: Meher
Student ID: bitsom_ba_2511026

A modular Python application for analyzing sales transactions, enriching them with product data from the DummyJSON API, and generating comprehensive reports with visualizations.

**Features**

File handling & preprocessing (Part 1)

Sales data processing & analytics (Part 2)

API integration with DummyJSON for product enrichment (Part 3)

Report generation with 8 structured sections (Part 4)

End-to-end main application workflow with user interaction (Part 5)

**Folder Structure**

sales-analytics-system/
│
├── data/
│   ├── sales_data.txt              # Input sales dataset
│   ├── enriched_sales_data.txt     # Generated enriched dataset
│
├── output/
│   ├── sales_report.txt            # Generated comprehensive report
│
├── utils/
│   ├── file_handler.py             # Part 1: File handling & preprocessing
│   ├── total_revenue.py            # Part 2: Sales summary
│   ├── region_wise_sales.py        # Part 2: Region analysis
│   ├── top_selling_products.py     # Part 2: Product analysis
│   ├── customer_analysis.py        # Part 2: Customer analysis
│   ├── daily_sales_trend.py        # Part 2: Date-based analysis
│   ├── peak_sales_day.py           # Part 2: Peak day analysis
│   ├── low_performing_products.py  # Part 2: Low performers
│   ├── api_handler.py              # Part 3: API integration & enrichment
│   └── report_generator.py         # Part 4: Report generation
│
├── main.py                         # Part 5: Main application workflow
├── requirements.txt                # Dependencies
└── README.md                       # Project documentation

**Setup Instructions**

Clone the repository

git clone https://github.com/mehernaresh/sales-analytics-system.git
cd sales-analytics-system

Install dependencies

pip install -r requirements.txt

Ensure input data is present

Place your sales_data.txt file inside the data/ folder.

**Running the Application**

Run the main script:

python main.py

**Expected Console Output (sample)**

=======================================

        SALES ANALYTICS SYSTEM

=======================================

[1/10] Reading sales data...
✓ Successfully read 80 transactions

[2/10] Parsing and cleaning data...
✓ Parsed 80 records

[3/10] Filter Options Available:
Regions: , East, North, South, West
Amount Range: ₹-998.0 - ₹81896.0

[4/10] Validating transactions...

Do you want to filter data? (y/n): y
Enter region to filter (or press Enter to skip): 
Enter minimum amount (or press Enter to skip): 1000
Enter maximum amount (or press Enter to skip): 10000
Available regions: East, North, South, West
Transaction amount range: min=257.0, max=818960.0
Records after amount filter: 28
✓ Valid: 28 | Invalid: 10

[5/10] Analyzing sales data...
✓ Analysis complete

[6/10] Fetching product data from API...
Successfully fetched 120 products.
Successfully cleaned 120 products.
✓ Fetched 120 products

[7/10] Enriching sales data...
Enriched data successfully saved to data/enriched_sales_data.txt
✓ Enriched 28/28 transactions (100.0%)

[8/10] Saving enriched data...
✓ Saved to: data/enriched_sales_data.txt

[9/10] Generating report...
Sales report successfully generated at output/sales_report.txt
✓ Report saved to: output/sales_report.txt

[10/10] Process Complete!

=======================================

**Outputs**

Enriched Sales Data → data/enriched_sales_data.txt

Comprehensive Report → output/sales_report.txt Includes:

===========================================

          SALES ANALYTICS REPORT
        Generated: 2026-01-18 15:06:03
        Records Processed: 28

===========================================

OVERALL SUMMARY
--------------------------------------------
Total Revenue:        ₹120,126.00
Total Transactions:   28
Average Order Value:  ₹4,290.21
Date Range:           2024-12-01 to 2024-12-30

REGION-WISE PERFORMANCE
--------------------------------------------
Region    Sales         % of Total  Transactions
East     ₹36,873   30.7%      6
North    ₹34,596   28.8%      8
West     ₹24,602   20.48%      6
South    ₹24,055   20.02%      8

TOP 5 PRODUCTS
--------------------------------------------
Rank  Product Name       Quantity   Revenue
1     Mouse              59        ₹39,005
2     Wireless Mouse     30        ₹27,598
3     USB Cable          23        ₹5,578
4     Wireless Mouse Gaming 17        ₹15,923
5     Mouse Wireless     8         ₹6,784

TOP 5 CUSTOMERS
--------------------------------------------
Rank  Customer ID   Total Spent   Orders
1     C007         ₹15,976   2
2     C011         ₹10,784   2
3     C026         ₹10,012   2
4     C013         ₹9,652   1
5     C005         ₹9,387   1

DAILY SALES TREND
--------------------------------------------
Date         Revenue       Transactions   Unique Customers
2024-12-01   ₹5,313   2            2
2024-12-02   ₹10,324   2            2
2024-12-03   ₹15,388   3            3
2024-12-07   ₹22,013   3            3
2024-12-08   ₹4,710   2            2
2024-12-09   ₹10,755   3            3
2024-12-10   ₹1,550   1            1
2024-12-16   ₹3,020   1            1
2024-12-22   ₹12,782   3            3
2024-12-24   ₹12,426   3            3
2024-12-25   ₹13,677   2            2
2024-12-29   ₹5,608   2            2
2024-12-30   ₹2,560   1            1

PRODUCT PERFORMANCE ANALYSIS
--------------------------------------------
Best Selling Day: 2024-12-07 (Revenue ₹22,013, Transactions 3)
Low Performing Products:
  Laptop Charger  Qty: 4   Revenue: ₹9,234
  Webcam          Qty: 6   Revenue: ₹16,004
  Mouse Wireless  Qty: 8   Revenue: ₹6,784
Average Transaction Value per Region:
  East     ₹6,145.50
  North    ₹4,324.50
  West     ₹4,100.33
  South    ₹3,006.88

API ENRICHMENT SUMMARY
--------------------------------------------
Total Products Enriched: 28
Success Rate: 100.0%
All products enriched successfully.