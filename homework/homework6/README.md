# Cleaning Functions
- fill_missing_median(df, columns) : Description: Fills missing values in the given columns with the median value of that column.
- drop_missing(df, threshold) : Description: Removes rows in the DataFrame where the proportion of missing values exceeds the specified threshold (e.g., 0.5 = 50%).
- normalize_data(df, columns) : Description: Scales the specified columns to a range using min-max normalization
# Assumptions
- Filling missing values with median: The median is less sensitive to outliers compared to the mean, making it a robust choice for skewed data or when some values are extreme. This ensures imputation does not distort column distributions.
- Threshold for dropping rows: Rows with over 50% missing data are unlikely to provide reliable information. Dropping these rows avoids introducing excessive bias from imputation and helps retain meaningful records. 
- Normalization: Certain numerical columns (e.g., age, income, score) are scaled to range using min-max normalization. This avoids disproportionate influence of any one feature in subsequent analysis