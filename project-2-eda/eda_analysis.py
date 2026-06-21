from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


DATA_FILE = Path(__file__).with_name("Dataset for Data Analytics.xlsx")
CHARTS_DIR = Path(__file__).with_name("charts")


def load_dataset(file_path):
    df = pd.read_excel(file_path)
    return df


def inspect_dataset(df):
    print("\nDataset Preview:")
    print(df.head())

    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())


def prepare_dataset(df):
    prepared_df = df.copy()

    prepared_df["CouponCode"] = prepared_df["CouponCode"].fillna("No Coupon")

    prepared_df["Date"] = pd.to_datetime(prepared_df["Date"], errors="coerce")

    return prepared_df


def descriptive_statistics(df):
    print("\nDescriptive Statistics for Numeric Columns:")
    numeric_columns = ["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]

    print(df[numeric_columns].describe())

    print("\nMean Values:")
    print(df[numeric_columns].mean())

    print("\nMedian Values:")
    print(df[numeric_columns].median())

    print("\nCount Values:")
    print(df[numeric_columns].count())


def categorical_analysis(df):
    categorical_columns = [
        "Product",
        "PaymentMethod",
        "OrderStatus",
        "ReferralSource",
        "CouponCode"
    ]

    print("\nCategorical Column Analysis:")

    for column in categorical_columns:
        print(f"\n{column} Counts:")

        counts = df[column].value_counts()

        for category, count in counts.items():
            print(f"{category}: {count}")


def product_revenue_analysis(df):
    print("\nRevenue by Product:")

    revenue_by_product = df.groupby("Product")["TotalPrice"].sum().sort_values(ascending=False)

    for product, revenue in revenue_by_product.items():
        print(f"{product}: {revenue:.2f}")

    print("\nAverage Order Value by Product:")

    average_order_value = df.groupby("Product")["TotalPrice"].mean().sort_values(ascending=False)

    for product, average_value in average_order_value.items():
        print(f"{product}: {average_value:.2f}")


def trend_analysis(df):
    print("\nMonthly Revenue Trend:")

    monthly_data = df.copy()
    monthly_data["Month"] = monthly_data["Date"].dt.to_period("M")

    monthly_revenue = monthly_data.groupby("Month")["TotalPrice"].sum()

    for month, revenue in monthly_revenue.items():
        print(f"{month}: {revenue:.2f}")

    print("\nMonthly Order Count:")

    monthly_order_count = monthly_data.groupby("Month")["OrderID"].count()

    for month, order_count in monthly_order_count.items():
        print(f"{month}: {order_count}")

    print("\nMonthly Average Order Value:")

    monthly_average_order_value = monthly_data.groupby("Month")["TotalPrice"].mean()

    for month, average_value in monthly_average_order_value.items():
        print(f"{month}: {average_value:.2f}") 


def outlier_detection(df):
    numeric_columns = ["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]

    print("\nOutlier Detection Using IQR Method:")

    for column in numeric_columns:
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]

        print(f"\n{column}:")
        print(f"Q1: {q1:.2f}")
        print(f"Q3: {q3:.2f}")
        print(f"IQR: {iqr:.2f}")
        print(f"Lower Bound: {lower_bound:.2f}")
        print(f"Upper Bound: {upper_bound:.2f}")
        print(f"Number of Outliers: {len(outliers)}")

        if len(outliers) > 0:
            print("\nTop Outlier Rows:")
            print(
                outliers[
                    ["OrderID", "Date", "Product", "Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]
                ].sort_values(by=column, ascending=False).head()
            )


def correlation_analysis(df):
    numeric_columns = ["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]

    print("\nCorrelation Analysis:")

    correlation_matrix = df[numeric_columns].corr()

    print(correlation_matrix)

    print("\nCorrelation with TotalPrice:")

    total_price_correlation = correlation_matrix["TotalPrice"].sort_values(ascending=False)

    for column, correlation in total_price_correlation.items():
        print(f"{column}: {correlation:.2f}")


def create_charts(df):
    CHARTS_DIR.mkdir(exist_ok=True)

    print("\nCreating Charts:")

    revenue_by_product = df.groupby("Product")["TotalPrice"].sum().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    revenue_by_product.plot(kind="bar")
    plt.title("Revenue by Product")
    plt.xlabel("Product")
    plt.ylabel("Total Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "revenue_by_product.png")
    plt.close()

    print("Saved: revenue_by_product.png")

    monthly_data = df.copy()
    monthly_data["Month"] = monthly_data["Date"].dt.to_period("M").astype(str)

    monthly_revenue = monthly_data.groupby("Month")["TotalPrice"].sum()

    plt.figure(figsize=(12, 6))
    monthly_revenue.plot(kind="line", marker="o")
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "monthly_revenue_trend.png")
    plt.close

    print("Saved: monthly_revenue_trend.png")

    plt.figure(figsize=(10, 6))
    df["TotalPrice"].plot(kind="hist", bins=20)
    plt.title("TotalPrice Distribution")
    plt.xlabel("TotalPrice")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "total_price_distribution.png")
    plt.close()

    print("Saved: total_price_distribution.png")



def main():
    df = load_dataset(DATA_FILE)

    inspect_dataset(df)

    prepared_df = prepare_dataset(df)

    descriptive_statistics(prepared_df)

    categorical_analysis(prepared_df)

    product_revenue_analysis(prepared_df)

    trend_analysis(prepared_df)

    outlier_detection(prepared_df)

    correlation_analysis(prepared_df)

    create_charts(prepared_df)


if __name__ == "__main__":
    main()