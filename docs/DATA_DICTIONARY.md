# Retail Sales Synthetic Dataset: Data Dictionary

The file `data/retail_sales_synthetic.csv` contains **960 fully synthetic orders**, with 40 orders per calendar month from January 2024 through December 2025. Each row represents one order with one product; therefore counting distinct order IDs equals counting order rows.

| Column | Type in Power BI | Definition |
| --- | --- | --- |
| OrderID | Text | Unique synthetic order identifier |
| OrderDate | Date | ISO formatted order date (`YYYY-MM-DD`) |
| Region | Text | North, South, East, or West |
| Channel | Text | Online, Retail, or Partner |
| CustomerSegment | Text | Consumer, Small Business, or Enterprise |
| Category | Text | Technology, Office, Home, or Lifestyle |
| Product | Text | Product name within a category |
| Units | Whole number | Quantity of units purchased |
| UnitPrice | Decimal number | Unit selling price before discount; assumed MYR |
| UnitCost | Decimal number | Unit acquisition cost; assumed MYR |
| DiscountRate | Decimal number | Fraction between 0 and 0.15 (format as percentage) |
| NetSales | Decimal number | Units × UnitPrice × (1 − DiscountRate), rounded to 2 decimals |
| COGS | Decimal number | Units × UnitCost, rounded to 2 decimals |
| GrossProfit | Decimal number | NetSales − COGS |

## Important notes

* Currency is assumed to be Malaysian ringgit (MYR) **only for this teaching example**; the transactions do not represent a real company.
* Data is deterministic, randomly generated, and does not contain personal or customer information.
* This is a simple flat table appropriate for an introductory project. A production semantic model often benefits from separate dimension tables.
* Sales and profit values can be reproduced directly from the CSV, subject to standard rounding.
