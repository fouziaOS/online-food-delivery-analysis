"""Main analysis: tables, charts and insights. Run from the project root: python src/analysis.py"""
import pandas as pd, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt, os
os.makedirs("outputs/charts", exist_ok=True); os.makedirs("outputs/tables", exist_ok=True)
df = pd.read_csv("data/food_orders.csv")
df.groupby("cuisine")["order_value_bdt"].agg(["count", "mean", "sum"]).round(2).to_csv("outputs/tables/revenue_by_cuisine.csv")
df.groupby("area")["delivery_time_min"].mean().round(2).rename("avg_delivery_min").to_csv("outputs/tables/delivery_time_by_area.csv")
df.groupby("is_weekend")["order_value_bdt"].agg(["count", "mean"]).round(2).to_csv("outputs/tables/weekend_vs_weekday.csv")
df.groupby("cuisine")["rating"].mean().round(2).rename("avg_rating").to_csv("outputs/tables/rating_by_cuisine.csv")
df[["order_value_bdt", "delivery_time_min", "discount_pct", "rating"]].corr().round(2).to_csv("outputs/tables/correlation_matrix.csv")
plt.figure(figsize=(8, 4.5)); df.groupby("cuisine")["order_value_bdt"].sum().sort_values().plot(kind="barh", color="#c55a11")
plt.title("Total Revenue by Cuisine"); plt.xlabel("BDT"); plt.tight_layout(); plt.savefig("outputs/charts/revenue_by_cuisine.png"); plt.close()
plt.figure(figsize=(8, 4.5)); df.groupby("area")["delivery_time_min"].mean().plot(kind="bar", color="#2e75b6")
plt.title("Average Delivery Time by Area"); plt.ylabel("Minutes"); plt.tight_layout(); plt.savefig("outputs/charts/delivery_time_by_area.png"); plt.close()
plt.figure(figsize=(8, 4.5)); plt.hist(df["delivery_time_min"], bins=18, color="#548235")
plt.title("Distribution of Delivery Times"); plt.xlabel("Minutes"); plt.tight_layout(); plt.savefig("outputs/charts/delivery_time_distribution.png"); plt.close()
plt.figure(figsize=(8, 4.5)); plt.scatter(df["delivery_time_min"], df["rating"], alpha=0.4, color="#7030a0")
plt.title("Delivery Time vs Rating"); plt.xlabel("Minutes"); plt.ylabel("Rating"); plt.tight_layout(); plt.savefig("outputs/charts/delivery_vs_rating.png"); plt.close()
top_cuisine = df.groupby("cuisine")["order_value_bdt"].sum().idxmax()
slow_area = df.groupby("area")["delivery_time_min"].mean().idxmax()
c = df["delivery_time_min"].corr(df["rating"])
wk = df.groupby("is_weekend")["order_value_bdt"].mean()
ins = f"""# Key Insights — Online Food Delivery Analysis

- Dataset: {len(df)} orders, total revenue **{df['order_value_bdt'].sum():,.0f} BDT**.
- Top cuisine by revenue: **{top_cuisine}**.
- Slowest delivery area: **{slow_area}** ({df.groupby('area')['delivery_time_min'].mean().max():.1f} minutes on average).
- Correlation between delivery time and rating: **{c:.2f}** (slower delivery, lower rating).
- Average order value on weekends: **{wk.get(1, 0):,.0f} BDT** vs weekdays **{wk.get(0, 0):,.0f} BDT**.
"""
open("outputs/insights.md", "w").write(ins)
print(ins)
