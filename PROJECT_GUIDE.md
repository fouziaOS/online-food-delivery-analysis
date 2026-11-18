# PROJECT GUIDE — Online Food Delivery Analysis

A complete explanation of this project for beginners: what it is, what every file
and column means, how the code works step by step, and how to explain it in a viva.

## 1. What is this project?
Analyzing 550 food delivery orders — cuisines, delivery times, ratings and revenue by area. It is a full data-analysis workflow: create data → clean and explore it →
group and summarize → draw charts → write honest insights. Dataset size: 550 orders.

## 2. Files in this project
- `README.md` — project summary with the key results and chart images.
- `PROJECT_GUIDE.md` — this guide.
- `requirements.txt` — the Python libraries needed (pandas, numpy, matplotlib).
- `src/generate_dataset.py` — builds the dataset with NumPy random numbers (fixed seed = same data every run).
- `src/analysis.py` — the main analysis code.
- `src/ml_model.py` — the Machine Learning code (trains 2 models and compares them).
- `data/food_orders.csv` — the dataset (created by generate_dataset.py).
- `online-food-delivery-analysis.ipynb` — the same analysis as a Jupyter notebook.
- `outputs/charts/` — chart images:
- `delivery_time_by_area.png`
- `delivery_time_distribution.png`
- `delivery_vs_rating.png`
- `revenue_by_cuisine.png`
- `outputs/tables/` — summary tables (CSV):
- `correlation_matrix.csv`
- `delivery_time_by_area.csv`
- `rating_by_cuisine.csv`
- `revenue_by_cuisine.csv`
- `weekend_vs_weekday.csv`
- `outputs/insights.md` — the key findings in plain words.

## 3. Dataset columns explained
| Column | Meaning |
|---|---|
| date | Order date |
| cuisine | Cuisine type |
| area | Delivery area |
| items | Number of items |
| order_value_bdt | Order value in BDT |
| delivery_time_min | Delivery time in minutes |
| discount_pct | Discount percentage |
| is_weekend | 1 if weekend, 0 if weekday |
| rating | Customer rating (1–5) |

## 4. How to run it (step by step)
1. Open a terminal inside this project folder.
2. Install the libraries: `pip install -r requirements.txt`
3. Create the data: `python src/generate_dataset.py`
4. Run the analysis: `python src/analysis.py`
5. Look inside `outputs/` — charts, tables and insights are created there.
6. Or open `online-food-delivery-analysis.ipynb` in Jupyter and run the cells one by one.

## 5. How the code works
**generate_dataset.py** — sets a fixed NumPy seed, chooses categories with realistic
probabilities, builds numeric columns from related formulas (so the data behaves like
real life), assembles a Pandas DataFrame and saves it as CSV.

**analysis.py** — loads the CSV with Pandas, then:
1. `groupby(...)` summaries → saved as tables in `outputs/tables/`.
2. A correlation matrix for the numeric columns.
3. Four Matplotlib charts → saved in `outputs/charts/`.
4. The most important numbers are written into `outputs/insights.md`.

## 6. Key results
# Key Insights — Online Food Delivery Analysis

- Dataset: 550 orders, total revenue **523,572 BDT**.
- Top cuisine by revenue: **Biryani**.
- Slowest delivery area: **Mirpur** (44.8 minutes on average).
- Correlation between delivery time and rating: **-0.45** (slower delivery, lower rating).
- Average order value on weekends: **968 BDT** vs weekdays **946 BDT**.

## 6b. The Machine Learning model
Predict the delivery time (`delivery_time_min`) from items, order value, discount, weekend, cuisine and area.
The code splits the data into 80% training and 20% testing, trains both models,
and compares them honestly on the test part only:
| Model | R² / Accuracy | RMSE |
|---|---|---|
| Linear Regression | 0.802 | 3.62 minutes |
| Random Forest | 0.713 | 4.36 minutes |

Best model: **Linear Regression**. Linear Regression predicts delivery time within about **3.6 minutes** on average (R² = 0.802) — delivery time here grows almost linearly with area distance and item count.
Key ideas: features (inputs) vs target (what we predict); train/test split so the
model is judged on data it has never seen; R² (how much variation the model explains)
and RMSE (average prediction error, in the target's own unit).

## 7. How to read the charts
- **Bar charts** compare groups (which group is biggest / most expensive / slowest).
- **Line charts** show change over time or hour — look for peaks.
- **Histograms** show how values are spread (most common range, rare extremes).
- **Scatter plots** show relationships between two numbers — an upward or downward
  cloud means the two move together (check the correlation value in the tables).

## 8. Viva / interview questions
**Q: What hurts ratings the most?**
A: Long delivery time — its correlation with rating is clearly negative in this data.

**Q: Why compare weekend vs weekday?**
A: Ordering behaviour changes on weekends; restaurants can plan offers and rider capacity around it.

**Q: Which cuisine should a new restaurant choose?**
A: The top-revenue cuisine here, balanced against competition and cost.

**Q: Why did the simple Linear Regression win here?**
A: The relationship is mostly additive (base time per area + time per item), which is exactly what linear models capture best.

## 9. Honest note
The data is synthetic (computer-generated with realistic patterns), made for learning
and portfolio demonstration. The workflow, code and analysis method are exactly what
would be used with real data.
