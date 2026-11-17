# DataCo Supply Chain Analytics

Data analytics and business intelligence portfolio analyzing DataCo supply-chain sales, profitability, shipping performance and delivery risks with **Python, SQL, Excel and Power BI**.

## Status
The Python and SQL source scripts are available in this repository. The uploaded project ZIP also contains Excel datasets, visualization screenshots, a Power BI dashboard (.pbix) and a PDF report; **those binary assets are not yet published here**.

## Project workflow
Raw data → data inspection and cleaning → Python visualizations → MySQL business queries → Power BI dashboards → business recommendations.

## Business questions
- How does late-delivery risk vary by shipping mode?
- Which markets generate the highest profit?
- Which product categories have negative average profit per order?
- Who are the top 10 customers by revenue?
- How does profit change by month?

## Repository files
- [Python analysis](03_Python/end%20to%20end%20project.py): pandas-based inspection, column removal, missing-value handling and exploratory charts.
- [MySQL queries](05_SQL/dataco_supply_chain_Analysis.sql): shipping performance, market/category profitability, top customers and monthly trends.
- [Python dependencies](requirements.txt).

## Power BI dashboard (from supplied project documentation)
The ZIP includes a three-page dashboard: Executive Overview, Shipping Performance and Root Cause Drill-Down. The supplied README reports total revenue of $36.78M, total profit of $3.97M, approximately 66K orders and a 54.83% late-delivery rate. These figures are taken from the supplied project documentation, not independently recalculated here.

## Reproducing the analysis
Run `pip install -r requirements.txt`. Obtain an authorized copy of the **DataCo SMART Supply Chain** dataset, then adjust the Excel filename and sheet name in the Python script for your local data. The MySQL queries expect a table named `datacosupplychain_clean_sql`.

**Data privacy:** The uploaded raw Excel sample includes customer contact/address fields and a column labeled `Customer Password`. It has not been published. Any samples must be reviewed and sanitized before public upload.

## Credits
The source ZIP's README credits **Thawfeeqa S.** as author. That original attribution is preserved here pending clarification of ownership and reuse permissions. If you are adapting this as a portfolio project, document your own independent work clearly.
