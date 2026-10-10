# Business Sales Performance Analytics

A Python-based data analytics project completed for **Future Interns — Data Science & Analytics, Task 1**.

## Project Overview

This project demonstrates how sales data can be analyzed to understand revenue trends, product performance, category performance, regional sales, and key business performance indicators (KPIs).

**Important:** The project uses synthetic sample data generated for demonstration purposes. The results do not represent actual company sales.

## Objectives

- Calculate key sales and profitability metrics.
- Examine daily and weekly revenue trends.
- Identify products contributing the most revenue and sales volume.
- Compare category-level revenue and profitability.
- Analyze regional sales performance.
- Produce visualizations, summary datasets, and actionable analytical recommendations.

## Technology Stack

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly

## Key Results

| Metric | Result |
|---|---:|
| Total revenue | ₹1,825,283.00 |
| Total profit | ₹730,113.20 |
| Transaction records | 3,000 |
| Average order value | ₹608.43 |
| Profit margin | 40.00% |
| Unique customers | 1,286 |
| Revenue per customer | ₹1,419.35 |

### Main Findings

- **Top product by revenue:** Laptop — ₹708,800.00.
- **Top category by revenue:** Electronics — ₹1,033,200.00.
- **Top region by revenue:** East — ₹322,972.00.

All figures above are calculated from synthetic sample data.

## Project Structure

```text
FUTURE_DS_01/
├── data/
│   └── processed/
│       ├── cleaned_sales_data.csv
│       ├── product_analysis.csv
│       ├── category_analysis.csv
│       └── regional_analysis.csv
├── notebooks/
│   └── Task1_Sales_Analytics.ipynb
├── visualizations/
│   ├── revenue_trends.png
│   ├── top_products.png
│   ├── category_performance.png
│   └── regional_performance.png
├── reports/
│   └── Analysis_Report.md
├── requirements.txt
└── README.md
```

Optional interactive dashboards may also be included if generated successfully.

## How to Run

1. Install Python and Jupyter Notebook.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Launch Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

6. Open `notebooks/Task1_Sales_Analytics.ipynb`.
7. Run the notebook cells sequentially using **Shift + Enter**.

## Deliverables

- Executable Jupyter Notebook
- Revenue trend visualizations
- Product performance visualization
- Category performance visualization
- Regional performance visualization
- Exported CSV datasets
- Business analysis report

## Limitations

The data is synthetic and designed for educational demonstration. Findings cannot be generalized to a real business without validation against actual sales records. Recommendations are exploratory and would require further testing.

## Author

Future Interns — Data Science & Analytics  
Task 1: Business Sales Performance Analytics
