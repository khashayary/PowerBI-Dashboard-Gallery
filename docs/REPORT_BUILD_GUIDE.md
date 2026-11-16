# Retail Sales Analytics: Build Three Report Pages in Power BI Desktop

This package supplements the existing public KAY POWER HUB Power BI Dashboard Gallery repository. It was developed using the same 960 synthetic order records for 2024 and 2025, and the numbers shown in the preview images are calculated from that dataset.

Important: PNG images are **illustrative, data accurate dashboard design previews** generated outside Power BI. They are **not** screenshots of a finished Power BI report. No `.pbix` or `.pbip` file is included yet.

## 1. Get started

1. Open the original repository `https://github.com/khashayary/PowerBI-Dashboard-Gallery` and download `data/retail_sales_synthetic.csv`.
2. Open Power BI Desktop. Choose **Get data > Text/CSV** and load the file.
3. In Power Query, set the query name to **Sales**. Verify `OrderDate` is Date, `Units` is Whole number and numeric price/cost fields are Decimal numbers. Select **Close & Apply**.
4. Use the existing `dax/measures.dax` in the repository to create the Date table and base measures. Create a single direction, one to many relationship from `'Date'[Date]` to `Sales[OrderDate]`.
5. Optionally create the additional measures in `dax/additional_measures.dax` from this package, one measure at a time.
6. In **View > Themes > Browse for themes**, select `themes/KAY_POWER_HUB_Retail_Analytics.json`.
7. Set your report canvas to 16:9 and use the preview images as layout references, not as proof the report is complete.

## 2. Page 1: Executive Overview

Four cards:

| Card | Measure | Full dataset validation |
| --- | --- | --- |
| Net Sales | `[Total Sales]` | RM 294,773.58 |
| Gross Profit | `[Gross Profit]` | RM 112,185.58 |
| Gross Margin | `[Gross Margin %]` | 38.06% |
| Orders | `[Orders]` | 960 |

Visuals:

1. **Monthly line chart:** `Date[Year Month]` on X axis and `[Total Sales]` on Y axis; set `Date[Year]` as legend to compare the series only if X axis is changed to `Date[Month Name]` sorted by Month Number. Alternatively use `Date[Year Month]` as a continuous two year timeline without a legend. The design preview compares years by month.
2. **Sales by Region:** clustered bar chart. Y axis `Sales[Region]`, X axis `[Total Sales]`.
3. **Sales by Category:** clustered bar chart. Y axis `Sales[Category]`, X axis `[Total Sales]`.
4. **Sales by Channel:** donut chart. Legend `Sales[Channel]`, Values `[Total Sales]`.
5. Add a Year slicer from `Date[Year]` for interactive filtering.

## 3. Page 2: Product Performance

1. KPI cards for `[Units Sold]`, `[Gross Profit]`, and category count (use `DISTINCTCOUNT ( Sales[Category] )` as a separate measure if desired).
2. Bar chart using `Sales[Category]` and `[Total Sales]`.
3. Bar chart using `Sales[Product]` and `[Total Sales]`; apply a **Top N = 5** visual filter for products.
4. Bar chart using `Sales[Category]` and `[Gross Profit]`.
5. Bar chart using `Sales[Category]` and `[Gross Margin %]`.
6. Add Region and Year slicers.

## 4. Page 3: Customers and Channels

1. Cards for Sales Channels `DISTINCTCOUNT ( Sales[Channel] )`, Customer Segments `DISTINCTCOUNT ( Sales[CustomerSegment] )`, `[Average Order Value]` and optionally Online Sales.
2. Bar chart: `[Total Sales]` by `Sales[Channel]`.
3. Bar chart: `[Total Sales]` by `Sales[CustomerSegment]`.
4. Bar chart: `[Average Order Value]` by `Sales[Channel]`.
5. Bar chart: `[Gross Margin %]` by `Sales[Channel]`.

## 5. Quality checks

1. With slicers cleared, 960 orders, 2,780 units and total sales RM 294,773.58 must appear.
2. Gross profit equals net sales minus COGS: RM 112,185.58.
3. 2024 net sales: RM 147,117.28. 2025 net sales: RM 147,656.30. Growth approximately 0.37%.
4. West is the largest revenue region at RM 80,421.12.
5. Home is the largest product category at RM 137,268.78.
6. Online sales total RM 157,255.84.
7. Compare with `docs/VERIFIED_METRICS.json` if any totals differ. Check all slicers and filters.

## 6. Save for GitHub

In Power BI Desktop, choose **File > Save as**. Save as a standard `.pbix` file or a source control friendly Power BI Project (`.pbip`) if supported by your installed Desktop version. For a PBIP project, commit its full companion folders, not merely the `.pbip` pointer file.

Place the actual report in your existing repository under `reports/`. Export one screenshot from the real report to `assets/retail-sales-powerbi-screenshot.png`. Never label the supplied design previews as actual Power BI screenshots.

Add a clear status note in the repository README and a short section summarizing what users can learn. Link the real report, sample CSV, DAX files, theme and screenshot. Include reproduction instructions.
