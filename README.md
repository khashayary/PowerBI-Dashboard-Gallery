# Power BI Dashboard Gallery

**KAY POWER HUB | Practical Business Analytics with Microsoft Power BI**

A growing collection of reproducible Power BI business analytics examples, developed for public learning and community reuse. This initial release contains a complete synthetic retail sales dataset, a documented DAX library, and instructions to build a Retail Sales Analytics dashboard from scratch.

## Featured project: Retail Sales Analytics

**Business question:** Which products, regions, customer segments, and sales channels contribute most to revenue and gross profit, and how is performance changing over time?

### Project contents

| File | Purpose |
| --- | --- |
| `data/retail_sales_synthetic.csv` | 960 synthetic order records across 2024 and 2025 |
| `docs/BUILD_GUIDE.md` | Guided Power BI report construction |
| `docs/DATA_DICTIONARY.md` | Schema, definitions, and business rules |
| `docs/BUSINESS_INSIGHTS.md` | Sample findings calculated from the provided CSV |
| `dax/measures.dax` | Reusable DAX measures and a calendar table definition |
| `assets/README.md` | Instructions for adding a real dashboard screenshot |

### Recommended report pages

1. **Executive Overview:** Total Sales, Gross Profit, Gross Margin, Orders, Sales by Month, Sales by Region.
2. **Product Performance:** Sales and Gross Profit by Product Category and Product.
3. **Customer and Channel:** Customer Segment and Sales Channel performance.

### Get started

1. Download the repository or the CSV file.
2. Open Power BI Desktop and select **Get data > Text/CSV**.
3. Import `data/retail_sales_synthetic.csv` and name the table **Sales**.
4. Confirm the column types and create the calendar relationship described in [the build guide](docs/BUILD_GUIDE.md).
5. Add the measures from [`dax/measures.dax`](dax/measures.dax).
6. Build and validate the visualizations using [the build guide](docs/BUILD_GUIDE.md).
7. Save your report as a `.pbix` or `.pbip` file and contribute it to this repository if you would like to publish an editable dashboard.

**Release status:** The sample dataset, DAX measures, and instructions are provided. A completed Power BI report file and screenshots are **not yet included**. This avoids implying that a dashboard has already been built or published.

### Reuse and contributions

The dataset is entirely synthetic. The repository can be used for classroom activities, Power BI practice, and community learning. You can propose improvements or additional examples through GitHub Issues and Pull Requests.

**Maintainer:** Khashayar Yazdani | **Community initiative:** KAY POWER HUB  
[LinkedIn](https://www.linkedin.com/in/khashayary/) | [GitHub profile](https://github.com/khashayary)

Licensed under the [MIT License](LICENSE).
