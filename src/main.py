import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project root (one level above /src)
PROJECT_ROOT = Path(__file__).resolve().parents[1]

CSV_PATH = PROJECT_ROOT / "data" / "superstore.csv"
OUT_DIR = PROJECT_ROOT / "outputs" / "figures"
OUT_DIR.mkdir(parents=True, exist_ok=True)

print("Loading data from:", CSV_PATH)

# Load dataset
df = pd.read_csv(CSV_PATH, encoding="latin-1")

# Basic checks
print("Dataset shape:", df.shape)
print("Columns:")
print(df.columns)

# Convert types
df["Sales"] = df["Sales"].astype(float)
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Monthly sales trend
monthly_sales = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()

# Plot
plt.figure(figsize=(10, 5))
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()

# Save chart
out_path = OUT_DIR / "monthly_sales_trend.png"
plt.savefig(out_path, dpi=200)
print("Saved chart to:", out_path)

plt.show()
