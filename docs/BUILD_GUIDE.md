# Building the Retail Sales Analytics Dashboard in Power BI

## 1. Import and prepare the data

1. Open Power BI Desktop.
2. Select **Get data > Text/CSV** and select `data/retail_sales_synthetic.csv`.
3. Load or transform the dataset and name the query **Sales**.
4. Set `OrderDate` to **Date**, `Units` to **Whole number**, `DiscountRate`, `UnitPrice`, `UnitCost`, `NetSales`, `COGS`, and `GrossProfit` to **Decimal number**.
5. Confirm row count: **960**. Confirm `OrderID` has no duplicates.

## 2. Create a calendar table

1. Select **Modeling > New table**.
2. Copy the `Date = ADDCOLUMNS(...)` expression from `dax/measures.dax`.
3. In the model view, create a **one-to-many, single-direction** relationship from `Date[Date]` to `Sales[OrderDate]`.
4. Mark the Date table using `Date[Date]`.
5. Sort `Date[Month Name]` by `Date[Month Number]` if using month names without year.

## 3. Add DAX measures

Under **Modeling > New measure**, add each measure from `dax/measures.dax` separately. Format monetary measures as MYR currency; percentages as percentages.

## 4. Build the report

### Page 1: Executive Overview

* Four **card** visuals: Total Sales, Gross Profit, Gross Margin %, Orders.
* One **line chart**: `Date[Year Month]` on X axis, Total Sales on Y axis.
* One **bar chart**: `Sales[Region]` and Total Sales.
* One **slicer**: `Date[Year]`.

### Page 2: Product Performance

* **Bar chart**: Total Sales by `Sales[Category]`.
* **Table**: Product, Total Sales, Gross Profit, Units Sold, Gross Margin %.
* **Slicers**: Year and Region.

### Page 3: Customers and Channels

* **Clustered bar chart**: Total Sales by `Sales[Channel]`.
* **Column chart**: Gross Profit by `Sales[CustomerSegment]`.
* **Table**: Channel, Orders, Average Order Value, Gross Profit.

## 5. Validate calculations

* The total Orders for all dates must be **960**.
* Gross Profit must equal Total Sales minus Total Cost.
* Gross Margin % must equal Gross Profit divided by Total Sales.
* The full-year Sales YoY % for 2025 should be populated, while 2024 has no previous-year comparison.
* Cross-check totals against the companion insights file.

## 6. Publish the visual deliverable

Once you have built the report, save the actual `.pbix` or `.pbip` project, then place a screenshot named `assets/dashboard-preview.png` in the repository. Update `README.md` to embed the screenshot and replace the release status with a factual description of the completed report.

Do not upload corporate customer data, student records, or other confidential information.
