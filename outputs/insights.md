# Key Insights — Online Food Delivery Analysis

- Dataset: 550 orders, total revenue **523,572 BDT**.
- Top cuisine by revenue: **Biryani**.
- Slowest delivery area: **Mirpur** (55.9 minutes on average).
- Correlation between delivery time and rating: **-0.43** (slower delivery, lower rating).
- Average order value on weekends: **968 BDT** vs weekdays **946 BDT**.

## Machine Learning — prediction model
Predict the delivery time (`delivery_time_min`) from items, order value, discount, weekend, cuisine and area.

| Model | R² / Accuracy | RMSE |
|---|---|---|
| Linear Regression | 0.802 | 3.62 minutes |
| Random Forest | 0.713 | 4.36 minutes |

**Best model: Linear Regression.** Linear Regression predicts delivery time within about **3.6 minutes** on average (R² = 0.802) — delivery time here grows almost linearly with area distance and item count.

Run it yourself: `python src/ml_model.py` (needs scikit-learn, already in `requirements.txt`).
Results are saved in `outputs/tables/model_results.csv`.
