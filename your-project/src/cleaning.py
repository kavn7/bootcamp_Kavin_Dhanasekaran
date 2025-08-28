
"""
Data Cleaning Utilities for CVNA Project
Stage 6: Data Preprocessing Functions
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def fill_missing_median(df, columns=None):
    """
    Fill missing values with median for specified numeric columns

    Args:
        df (pd.DataFrame): Input dataframe
        columns (list): List of columns to process. If None, processes all numeric columns

    Returns:
        pd.DataFrame: DataFrame with missing values filled
    """
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns

    df_copy = df.copy()

    for col in columns:
        if col in df_copy.columns and df_copy[col].dtype in ['int64', 'float64']:
            median_val = df_copy[col].median()
            df_copy[col].fillna(median_val, inplace=True)
            print(f"Filled {df_copy[col].isna().sum()} missing values in {col} with median: {median_val:.4f}")

    return df_copy

def drop_missing(df, threshold=0.5):
    """
    Drop rows or columns with missing values based on threshold

    Args:
        df (pd.DataFrame): Input dataframe
        threshold (float): Threshold for dropping (0.5 = drop if >50% missing)

    Returns:
        pd.DataFrame: DataFrame with missing data removed
    """
    df_copy = df.copy()
    initial_shape = df_copy.shape

    # Drop columns with too many missing values
    missing_col_pct = df_copy.isnull().sum() / len(df_copy)
    cols_to_drop = missing_col_pct[missing_col_pct > threshold].index
    df_copy = df_copy.drop(columns=cols_to_drop)

    # Drop rows with any remaining missing values
    df_copy = df_copy.dropna()

    final_shape = df_copy.shape
    print(f"Shape changed from {initial_shape} to {final_shape}")
    print(f"Dropped {len(cols_to_drop)} columns and {initial_shape[0] - final_shape[0]} rows")

    return df_copy

def normalize_data(df, columns=None, method='standard'):
    """
    Normalize numeric columns using StandardScaler or MinMaxScaler

    Args:
        df (pd.DataFrame): Input dataframe
        columns (list): Columns to normalize. If None, normalizes all numeric columns
        method (str): 'standard' for StandardScaler, 'minmax' for MinMaxScaler

    Returns:
        tuple: (normalized_df, scaler_object)
    """
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns

    df_copy = df.copy()

    if method == 'standard':
        scaler = StandardScaler()
    elif method == 'minmax':
        scaler = MinMaxScaler()
    else:
        raise ValueError("Method must be 'standard' or 'minmax'")

    # Only normalize numeric columns that exist in the dataframe
    valid_columns = [col for col in columns if col in df_copy.columns and 
                     df_copy[col].dtype in ['int64', 'float64']]

    if valid_columns:
        df_copy[valid_columns] = scaler.fit_transform(df_copy[valid_columns])
        print(f"Normalized {len(valid_columns)} columns using {method} scaling")
    else:
        print("No valid numeric columns found for normalization")

    return df_copy, scaler

def detect_and_handle_outliers(df, column, method='iqr', action='flag'):
    """
    Detect and handle outliers in a specific column

    Args:
        df (pd.DataFrame): Input dataframe
        column (str): Column to process
        method (str): 'iqr' or 'zscore'
        action (str): 'flag', 'remove', or 'clip'

    Returns:
        pd.DataFrame: Processed dataframe
    """
    df_copy = df.copy()

    if column not in df_copy.columns:
        print(f"Column {column} not found in dataframe")
        return df_copy

    if method == 'iqr':
        Q1 = df_copy[column].quantile(0.25)
        Q3 = df_copy[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outlier_mask = (df_copy[column] < lower_bound) | (df_copy[column] > upper_bound)

    elif method == 'zscore':
        z_scores = np.abs((df_copy[column] - df_copy[column].mean()) / df_copy[column].std())
        outlier_mask = z_scores > 3

    else:
        raise ValueError("Method must be 'iqr' or 'zscore'")

    outlier_count = outlier_mask.sum()
    print(f"Found {outlier_count} outliers in {column} using {method} method")

    if action == 'flag':
        df_copy[f'{column}_outlier'] = outlier_mask
    elif action == 'remove':
        df_copy = df_copy[~outlier_mask]
        print(f"Removed {outlier_count} outlier rows")
    elif action == 'clip':
        if method == 'iqr':
            df_copy[column] = df_copy[column].clip(lower=lower_bound, upper=upper_bound)
        print(f"Clipped {outlier_count} outlier values")

    return df_copy

# CVNA-specific cleaning functions
def clean_cvna_stock_data(df):
    """
    Apply CVNA-specific cleaning rules to stock data

    Args:
        df (pd.DataFrame): Raw CVNA stock data

    Returns:
        pd.DataFrame: Cleaned stock data
    """
    df_clean = df.copy()

    # Remove any rows where price or volume is 0 or negative
    df_clean = df_clean[(df_clean['close'] > 0) & (df_clean['volume'] > 0)]

    # Handle any remaining missing values
    numeric_cols = ['close', 'volume', 'returns']
    df_clean = fill_missing_median(df_clean, [col for col in numeric_cols if col in df_clean.columns])

    # Flag extreme price movements (>20% single day moves)
    if 'returns' in df_clean.columns:
        df_clean['extreme_move'] = (np.abs(df_clean['returns']) > 0.20).astype(int)

    print(f"CVNA cleaning complete. Final shape: {df_clean.shape}")
    return df_clean

def clean_social_media_data(df):
    """
    Apply specific cleaning rules to social media data

    Args:
        df (pd.DataFrame): Raw social media data

    Returns:
        pd.DataFrame: Cleaned social media data
    """
    df_clean = df.copy()

    # Ensure posts_per_day is at least 1
    df_clean['posts_per_day'] = df_clean['posts_per_day'].clip(lower=1)

    # Ensure engagement_per_day is non-negative
    df_clean['engagement_per_day'] = df_clean['engagement_per_day'].clip(lower=0)

    # Fill any missing values with median
    numeric_cols = ['posts_per_day', 'engagement_per_day', 'unique_users_per_day']
    df_clean = fill_missing_median(df_clean, [col for col in numeric_cols if col in df_clean.columns])

    print(f"Social media cleaning complete. Final shape: {df_clean.shape}")
    return df_clean

if __name__ == "__main__":
    # Example usage
    print("CVNA Data Cleaning Utilities Loaded")
    print("Available functions:")
    print("- fill_missing_median()")
    print("- drop_missing()")  
    print("- normalize_data()")
    print("- detect_and_handle_outliers()")
    print("- clean_cvna_stock_data()")
    print("- clean_social_media_data()")
