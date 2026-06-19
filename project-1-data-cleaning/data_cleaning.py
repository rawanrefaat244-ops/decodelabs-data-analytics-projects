from pathlib import Path
import pandas as pd


DATA_FILE = Path(__file__).with_name("Dataset for Data Analytics.xlsx")
OUTPUT_FILE = Path(__file__).with_name("cleaned_dataset.xlsx")


def load_dataset(file_path):
    df = pd.read_excel(file_path)
    return df


def inspect_dataset(df):
    print("\nDataset Preview:")
    print(df.head())

    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumn names")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())


def audit_dataset(df):
    print("\nDuplicate OrderID Values:")
    print(df["OrderID"].duplicated().sum())

    print("\nDuplicate TrackingNumber Values:")
    print(df["TrackingNumber"].duplicated().sum())

    print("\nInvalid Dates:")
    invalid_dates = df["Date"].isnull().sum()
    print(invalid_dates)

    print("\nTotalPrice Mismatches:")
    expected_total = df["Quantity"] * df["UnitPrice"]
    mismatches = (df["TotalPrice"].round(2) != expected_total.round(2)).sum()
    print(mismatches)

    print("\nUnique Product Values:")
    print(df["Product"].unique())

    print("\nUnique PaymentMethod Values:")
    print(df["PaymentMethod"].unique())

    print("\nUnique OrderStatus Values:")
    print(df["OrderStatus"].unique())

    print("\nUnique ReferralSource Values:")
    print(df["ReferralSource"].unique())


def clean_dataset(df):
    cleaned_df = df.copy()

    cleaned_df = cleaned_df.drop_duplicates()

    cleaned_df["CouponCode"] = cleaned_df["CouponCode"].fillna("No Coupon")
    cleaned_df["CouponCode"] = cleaned_df["CouponCode"].astype("string").str.strip()

    cleaned_df.loc[
        cleaned_df["CouponCode"].str.lower() != "no coupon",
        "CouponCode"
    ] = cleaned_df["CouponCode"].str.upper()

    cleaned_df["Date"] = pd.to_datetime(cleaned_df["Date"], errors="coerce").dt.strftime("%Y-%m-%d")

    id_columns = ["OrderID", "CustomerID", "TrackingNumber"]
    for column in id_columns:
        cleaned_df[column] = cleaned_df[column].astype("string").str.strip().str.upper()

    text_columns = [
        "Product",
        "ShippingAddress",
        "PaymentMethod",
        "OrderStatus",
        "ReferralSource"
    ]

    for column in text_columns:
        cleaned_df[column] = cleaned_df[column].astype("string").str.strip().str.title()

    cleaned_df["Quantity"] = pd.to_numeric(cleaned_df["Quantity"], errors="coerce").astype("int64")
    cleaned_df["ItemsInCart"] = pd.to_numeric(cleaned_df["ItemsInCart"], errors="coerce").astype("int64")

    cleaned_df["UnitPrice"] = pd.to_numeric(cleaned_df["UnitPrice"], errors="coerce").round(2)
    cleaned_df["TotalPrice"] = pd.to_numeric(cleaned_df["TotalPrice"], errors="coerce").round(2)

    return cleaned_df


def save_cleaned_dataset(df, output_file):
    df.to_excel(output_file, index=False)
    print(f"\nCleaned dataset saved successfully as: {output_file.name}")


def validate_cleaned_dataset(cleaned_df):
    print("\nFinal Validation Report:")

    print("\nMissing Values After Cleaning:")
    print(cleaned_df.isnull().sum())

    print("\nDuplicates Rows After Cleaning:")
    print(cleaned_df.duplicated().sum())

    print("\nDuplicate OrderID Values After Cleaning:")
    print(cleaned_df["OrderID"].duplicated().sum())

    print("\nDuplicate TrackingNumber Values After Cleaning:")
    print(cleaned_df["TrackingNumber"].duplicated().sum())

    print("\nInvalid Dates After Cleaning:")
    invalid_dates = pd.to_datetime(cleaned_df["Date"], errors="coerce").isnull().sum()
    print(invalid_dates)

    print("\nTotalPrice Mismatches After Cleaning:")
    expected_total = cleaned_df["Quantity"] * cleaned_df["UnitPrice"]
    mismatches = (cleaned_df["TotalPrice"].round(2) != expected_total.round(2)).sum()
    print(mismatches)


def main():
    df = load_dataset(DATA_FILE)

    inspect_dataset(df)
    audit_dataset(df)

    cleaned_df = clean_dataset(df)

    print("\nCleaned Dataset Missing Values:")
    print(cleaned_df.isnull().sum())

    print("\nCleaned Dataset Preview:")
    print(cleaned_df.head())

    validate_cleaned_dataset(cleaned_df)

    save_cleaned_dataset(cleaned_df, OUTPUT_FILE)


if __name__ == "__main__":
    main()