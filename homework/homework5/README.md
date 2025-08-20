## Data Storage

- Raw data is stored in CSV format in `data/raw/` for broad compatibility.
- Processed data is stored in Parquet format in `data/processed/` for faster reads/writes and space efficiency.
- Folder locations are controlled by environment variables in the `.env` file (`DATA_DIR_RAW`, `DATA_DIR_PROCESSED`).
- Utilities (`write_df`, `read_df`) automatically choose the method based on file extension.
- Validation function ensures loaded data matches the original DataFrame’s shape and types.
