import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans a DataFrame by:
      1. Dropping rows where all values are NaN
      2. Removing duplicate rows
      3. Filling missing numeric values with the median
      4. Filling missing categorical/string values with 'Unknown'
      5. Normalizing text columns (strip, lowercase)
    """
    # Drop rows where all values are NaN
    df = df.dropna(how='all')

    # Remove duplicate rows
    df = df.drop_duplicates()

    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            # Fill missing numeric values with median
            df[col] = df[col].fillna(df[col].median())
        else:
            # Fill missing strings with 'Unknown' and normalize text
            df[col] = df[col].fillna("Unknown").astype(str).str.strip().str.lower()

    return df
# src/cleaning.py

import pandas as pd

def drop_missing(df: pd.DataFrame, how: str = 'all') -> pd.DataFrame:
    """
    Drop rows or columns with missing values.
    
    Parameters:
        df: pd.DataFrame
        how: 'all' to drop rows/columns where all values are NaN,
             'any' to drop if any value is NaN
        
    Returns:
        pd.DataFrame with rows/columns dropped
    """
    return df.dropna(how=how)

def fill_missing_median(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing numeric values with the median of their column.
    
    Parameters:
        df: pd.DataFrame
        
    Returns:
        pd.DataFrame with numeric NaNs filled
    """
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].median())
    return df

def normalize_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize string/categorical columns by stripping whitespace
    and converting to lowercase. Also fill missing string values with 'Unknown'.
    
    Parameters:
        df: pd.DataFrame
        
    Returns:
        pd.DataFrame with normalized text
    """
    for col in df.columns:
        if not pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna('Unknown').astype(str).str.strip().str.lower()
    return df

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows from the DataFrame.
    
    Parameters:
        df: pd.DataFrame
        
    Returns:
        pd.DataFrame without duplicates
    """
    return df.drop_duplicates()

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Full cleaning pipeline:
    1. Drop empty rows
    2. Remove duplicates
    3. Fill missing numeric values
    4. Normalize text
    """
    df = drop_missing(df, how='all')
    df = remove_duplicates(df)
    df = fill_missing_median(df)
    df = normalize_data(df)
    return df
