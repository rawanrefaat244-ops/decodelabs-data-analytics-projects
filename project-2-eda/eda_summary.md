# Exploratory Data Analysis Report

## Project
DecodeLabs Data Analytics Project 2: Exploratory Data Analysis (EDA)

## Dataset
Dataset for Data Analytics.xlsx

## Project Objective
The objective of this project is to perform Exploratory Data Analysis (EDA) on an e-commerce order dataset to understand patterns, trends, distributions, outliers, and relationships between variables.

This analysis focuses on descriptive statistics, categorical distributions, product revenue, monthly revenue trends, outlier detection, correlation analysis, and visualizations.

---

## Dataset Overview

The dataset contains:

- Total rows: 1200
- Total columns: 14
- Duplicate rows: 0
- Missing values: 309 missing values in `CouponCode`
- Date column format: valid datetime format
- Numeric columns: `Quantity`, `UnitPrice`, `ItemsInCart`, `TotalPrice`
- Categorical columns: `Product`, `PaymentMethod`, `OrderStatus`, `ReferralSource`, `CouponCode`

Missing values in `CouponCode` were filled with `No Coupon` for analysis purposes, so coupon usage could be included in the categorical analysis.

---

## Descriptive Statistics Summary

The numeric columns analyzed were:

- `Quantity`
- `UnitPrice`
- `ItemsInCart`
- `TotalPrice`

### Key Findings

- Average quantity per order: 2.95
- Median quantity per order: 3
- Average unit price: 356.41
- Median unit price: 364.21
- Average items in cart: 5.49
- Median items in cart: 5
- Average total price: 1053.97
- Median total price: 823.62
- Maximum total price: 3456.40

The mean `TotalPrice` is higher than the median, which suggests that the `TotalPrice` distribution is right-skewed. This means most orders are in the lower or middle price range, while some high-value orders pull the average upward.

---

## Categorical Analysis

### Product Counts

- Printer: 181
- Tablet: 179
- Chair: 178
- Laptop: 173
- Desk: 170
- Monitor: 163
- Phone: 156

Printer appeared most frequently, while Phone appeared least frequently. However, the product distribution is fairly balanced, and no single product dominates the dataset strongly by order count.

### Payment Method Counts

- Online: 258
- Cash: 246
- Credit Card: 234
- Debit Card: 232
- Gift Card: 230

Online payment was the most common payment method, but the distribution across payment methods is relatively balanced.

### Order Status Counts

- Cancelled: 250
- Returned: 247
- Pending: 237
- Shipped: 235
- Delivered: 231

Cancelled and Returned orders were slightly higher than Delivered orders. This may require further business investigation because a high number of cancelled or returned orders could affect customer satisfaction and revenue performance.

### Referral Source Counts

- Instagram: 259
- Email: 250
- Google: 241
- Facebook: 228
- Referral: 222

Instagram generated the highest number of orders, while Referral generated the lowest number of orders.

### Coupon Code Counts

- FREESHIP: 313
- No Coupon: 309
- WINTER15: 292
- SAVE10: 286

FREESHIP was the most used coupon code. A large number of orders were also placed without any coupon.

---

## Product Revenue Analysis

### Revenue by Product

- Chair: 195620.11
- Printer: 195612.61
- Laptop: 192126.56
- Tablet: 186568.95
- Monitor: 175651.41
- Desk: 167459.93
- Phone: 151722.39

Chair generated the highest total revenue, while Phone generated the lowest total revenue.

Printer had the highest order count, but Chair slightly generated more total revenue than Printer. This shows that order count alone is not enough to understand product performance.

### Average Order Value by Product

- Laptop: 1110.56
- Chair: 1098.99
- Printer: 1080.73
- Monitor: 1077.62
- Tablet: 1042.28
- Desk: 985.06
- Phone: 972.58

Laptop had the highest average order value, even though it did not have the highest total revenue or the highest order count. This suggests that Laptop orders are typically more valuable per order.

---

## Monthly Trend Analysis

Monthly revenue, order count, and average order value were analyzed using the `Date` column.

### Key Findings

- Highest monthly revenue: June 2024 with 68068.54
- Highest monthly order count: June 2024 with 53 orders
- High-performing month: May 2023 with revenue of 63836.84 and average order value of 1302.79
- Lowest monthly revenue: April 2023 with 27751.71
- Lowest monthly order count: January 2025 with 27 orders
- Lowest monthly average order value: March 2025 with 800.01

June 2024 was the strongest month because it had both the highest revenue and the highest order count.

March 2025 had 49 orders but a relatively low average order value of 800.01. This shows that a high number of orders does not always lead to the highest revenue if the average order value is low.

---

## Outlier Detection

Outliers were detected using the IQR method.

The numeric columns checked were:

- `Quantity`
- `UnitPrice`
- `ItemsInCart`
- `TotalPrice`

### Outlier Results

- Quantity outliers: 0
- UnitPrice outliers: 0
- ItemsInCart outliers: 0
- TotalPrice outliers: 8

For `TotalPrice`:

- Q1: 410.52
- Q3: 1578.47
- IQR: 1167.95
- Lower bound: -1341.41
- Upper bound: 3330.41
- Number of outliers: 8

The detected `TotalPrice` outliers were high-value orders above 3330.41.

These outliers appear to be valid business records rather than errors because they are caused by the combination of high quantity and high unit price. The outliers were identified and investigated but not removed.

---

## Correlation Analysis

Correlation analysis was performed on the numeric columns:

- `Quantity`
- `UnitPrice`
- `ItemsInCart`
- `TotalPrice`

### Correlation with TotalPrice

- TotalPrice: 1.00
- UnitPrice: 0.72
- Quantity: 0.62
- ItemsInCart: 0.39

### Key Findings

`UnitPrice` had the strongest positive correlation with `TotalPrice`, followed by `Quantity`.

This means that higher order values are mainly related to higher unit prices and larger quantities.

`ItemsInCart` had a weaker positive relationship with `TotalPrice`, which suggests that cart size alone does not strongly explain order value. A cart may contain many low-priced items or fewer high-priced items.

Correlation should be treated as a clue, not proof of causation.

---

## Visualizations Created

The following charts were created and saved in the `charts` folder:

- `revenue_by_product.png`
- `monthly_revenue_trend.png`
- `total_price_distribution.png`

### Chart Insights

The revenue by product chart shows that Chair and Printer were the top revenue-generating products.

The monthly revenue trend chart shows clear month-to-month variation, with June 2024 being the strongest month.

The TotalPrice distribution chart shows a right-skewed distribution, where most orders are lower or medium value, while a small number of high-value orders create a long right tail.

---

## Final Observations

1. The dataset is suitable for EDA, with no duplicate rows and valid numeric/date fields.
2. `CouponCode` had missing values, which were handled by labeling them as `No Coupon`.
3. Printer had the highest order count, but Chair generated the highest total revenue.
4. Laptop had the highest average order value.
5. Online was the most common payment method.
6. Cancelled and Returned orders were slightly higher than Delivered orders.
7. Instagram was the leading referral source by order count.
8. FREESHIP was the most frequently used coupon.
9. June 2024 was the strongest month in terms of both revenue and order count.
10. `TotalPrice` had 8 high-value outliers, while other numeric columns had no outliers.
11. `UnitPrice` and `Quantity` were the strongest numeric factors related to `TotalPrice`.

---

## Conclusion

This EDA project helped transform the dataset from a static table into meaningful business insights. The analysis showed product performance, customer behavior patterns, monthly revenue trends, outliers, and relationships between numeric variables.

The most important findings were that Chair generated the highest total revenue, Laptop had the highest average order value, June 2024 was the strongest month, and high `TotalPrice` values were mainly driven by higher unit prices and larger quantities.

Overall, this project demonstrates the use of descriptive statistics, categorical analysis, trend analysis, outlier detection, correlation analysis, and visualization to support data-driven decision making.