# Data Cleaning Change Log

## Project
DecodeLabs Data Analytics Project 1: Data Cleaning & Preparation

## Dataset
Dataset for Data Analytics.xlsx

## Project Objective
The objective of this project is to clean and prepare a raw dataset by identifying missing values, checking duplicates, correcting data formats, and validating the final cleaned dataset.

---

## Raw Dataset Summary

- Original rows: 1200
- Original columns: 14
- Missing values found: 309 missing values in `CouponCode`
- Duplicate rows found: 0
- Duplicate `OrderID` values found: 0
- Duplicate `TrackingNumber` values found: 0
- Invalid dates found: 0
- `TotalPrice` mismatches found: 0

---

## Cleaning Actions

| Change ID | Issue Found | Cleaning Action | Reason | Result |
|---|---|---|---|---|
| CH001 | Missing values were found in `CouponCode` | Filled missing values with `No Coupon` | Missing coupon codes most likely mean that the customer did not use a coupon, so deleting these rows would remove valid order records | `CouponCode` missing values reduced from 309 to 0 |
| CH002 | Duplicate rows needed to be checked | Used `drop_duplicates()` to remove fully duplicated rows if present | Duplicate rows can cause inaccurate analysis by counting the same order more than once | Duplicate rows after cleaning: 0 |
| CH003 | `OrderID` uniqueness needed to be verified | Checked duplicate values in `OrderID` | Each order should have a unique order identifier | Duplicate `OrderID` values after cleaning: 0 |
| CH004 | `TrackingNumber` uniqueness needed to be verified | Checked duplicate values in `TrackingNumber` | Each shipment should have a unique tracking number | Duplicate `TrackingNumber` values after cleaning: 0 |
| CH005 | Date format needed standardization | Converted the `Date` column to `YYYY-MM-DD` format | A consistent date format improves readability, sorting, and future analysis | Invalid dates after cleaning: 0 |
| CH006 | Text columns needed formatting consistency | Trimmed extra spaces and standardized text capitalization for selected text columns | Consistent text formatting prevents category duplication caused by spacing or capitalization differences | Text columns were standardized |
| CH007 | Coupon code formatting needed to be preserved | Kept actual coupon codes uppercase while keeping `No Coupon` readable | Coupon codes are usually written in uppercase and should not be converted to title case | Coupon codes such as `SAVE10` and `FREESHIP` remained uppercase |
| CH008 | Numeric columns needed validation | Converted `Quantity`, `ItemsInCart`, `UnitPrice`, and `TotalPrice` to proper numeric formats | Numeric formatting is required for accurate calculations and future analysis | Numeric columns were validated successfully |
| CH009 | `TotalPrice` needed calculation verification | Compared `TotalPrice` with `Quantity × UnitPrice` | This confirms that the financial values are accurate | `TotalPrice` mismatches after cleaning: 0 |

---

## Final Validation Results

- Missing values after cleaning: 0
- Duplicate rows after cleaning: 0
- Duplicate `OrderID` values after cleaning: 0
- Duplicate `TrackingNumber` values after cleaning: 0
- Invalid dates after cleaning: 0
- `TotalPrice` mismatches after cleaning: 0

---

## Output File

The cleaned dataset was exported as:

`cleaned_dataset.xlsx`

---

## Conclusion

The dataset was successfully cleaned and prepared for analysis. Missing coupon code values were handled, duplicates were checked, date formatting was standardized, numeric columns were validated, and the final dataset passed all validation checks.