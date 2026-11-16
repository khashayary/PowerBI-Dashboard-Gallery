# Retail Sales Analytics | Release 02

**KAY POWER HUB | Power BI Dashboard Gallery**

This update extends the existing [Power BI Dashboard Gallery](https://github.com/khashayary/PowerBI-Dashboard-Gallery) with three data accurate dashboard design previews, a Power BI theme, extra DAX, a detailed visual construction guide, verified totals, and a repeatable dataset validation script.

### Contents

* `assets/dashboard-preview-executive.png`: executive dashboard design preview
* `assets/dashboard-preview-products.png`: product performance design preview
* `assets/dashboard-preview-channels.png`: customer and channel design preview
* `themes/KAY_POWER_HUB_Retail_Analytics.json`: ready to import Power BI color theme
* `dax/additional_measures.dax`: optional extra DAX measures
* `docs/REPORT_BUILD_GUIDE.md`: visual by visual Power BI build instructions
* `docs/VERIFIED_METRICS.json`: totals calculated from the original repository CSV
* `tools/validate_retail_data.py`: standard library dataset validation script
* `README_INSERT.md`: Markdown section for the repository README

### How to use

Copy the extracted files into the *root of your existing repository*, keeping the directory structure. The existing `data/retail_sales_synthetic.csv` and base DAX file should remain unchanged. Paste `README_INSERT.md` into the repository's root `README.md`, or link to it.

### Honest status

The PNG files are **design previews** produced outside Power BI using the verified synthetic data, not actual Power BI screenshots. A Power BI `.pbix` or `.pbip` must be completed and saved in Power BI Desktop before you may accurately describe this project as containing a fully functional Power BI report.

### Validation

Net Sales RM 294,773.58 | Gross Profit RM 112,185.58 | Orders 960 | Gross Margin 38.06%.
