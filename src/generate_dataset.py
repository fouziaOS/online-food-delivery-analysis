"""Generate the dataset for this project (synthetic data, NumPy seed-based)."""
import numpy as np, pandas as pd, os
rng = np.random.default_rng(7)
os.makedirs("data", exist_ok=True)
n = 550
cuisines = ["Biryani", "Fast Food", "Bengali", "Chinese", "Dessert", "Pizza"]
cu_p = [0.24, 0.22, 0.18, 0.14, 0.10, 0.12]
areas = ["Dhanmondi", "Uttara", "Mirpur", "Gulshan", "Banani", "Mohammadpur"]
cuisine = rng.choice(cuisines, n, p=cu_p)
area = rng.choice(areas, n)
dates = pd.date_range("2025-01-01", periods=150, freq="D")
date = pd.Series(rng.choice(dates, n))
items = rng.integers(1, 6, n)
price_map = {"Biryani": 320, "Fast Food": 280, "Bengali": 240, "Chinese": 350, "Dessert": 180, "Pizza": 520}
base = np.array([price_map[c] for c in cuisine])
order_value = np.round(base * items * rng.uniform(0.85, 1.2, n), 2)
area_base = {"Dhanmondi": 30, "Uttara": 36, "Mirpur": 48, "Gulshan": 32, "Banani": 33, "Mohammadpur": 40}
weekend_flag = (date.dt.dayofweek >= 5).astype(int)
delivery = np.round(np.array([area_base[a] for a in area]) + items * 2.2 + weekend_flag * 4 + rng.normal(0, 4, n), 1).clip(15, 85)
discount = rng.choice([0, 0, 0, 10, 15, 20, 25], n)
rating = np.round((4.9 - 0.016 * delivery + rng.normal(0, 0.3, n)).clip(2.0, 5.0), 1)
df = pd.DataFrame({"date": date.dt.date, "cuisine": cuisine, "area": area, "items": items,
                   "order_value_bdt": order_value, "delivery_time_min": delivery,
                   "discount_pct": discount, "is_weekend": weekend_flag,
                   "rating": rating})
df.to_csv("data/food_orders.csv", index=False)
print("Saved", len(df), "orders")
