
"""
CVNA Data Integration Script - Combining Stock and Social Media Data
Based on existing yfinance CVNA data collection
"""

import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta
import os
from pathlib import Path

class CVNADataIntegrator:
    def __init__(self):
        self.stock_data = None
        self.social_data = None
        self.integrated_data = None
        self.setup_directories()

    def setup_directories(self):
        """Create necessary directories"""
        for dir_name in ['data/raw', 'data/processed', 'src', 'notebooks']:
            os.makedirs(dir_name, exist_ok=True)

    def load_existing_stock_data(self, filepath=None):
        """
        Load your existing CVNA stock data or fetch new data
        """
        if filepath and os.path.exists(filepath):
            print(f"📂 Loading existing stock data from {filepath}")
            df = pd.read_csv(filepath)
            # Ensure proper datetime handling
            if 'timestamp' in df.columns:
                df['date'] = pd.to_datetime(df['timestamp']).dt.date
            elif 'Date' in df.columns:
                df['date'] = pd.to_datetime(df['Date']).dt.date
        else:
            print("🔄 Fetching fresh CVNA data using yfinance...")
            ticker = yf.Ticker("CVNA")
            df = ticker.history(start="2023-01-01").reset_index()
            df = df.rename(columns={
                "Date": "timestamp",
                "Open": "open",
                "High": "high", 
                "Low": "low",
                "Close": "close",
                "Volume": "volume"
            })
            df['date'] = df['timestamp'].dt.date

            # Save the fresh data
            df.to_csv('data/raw/cvna_stock_data.csv', index=False)

        # Calculate additional stock metrics
        df['returns'] = df['close'].pct_change()
        df['volatility'] = df['returns'].rolling(window=20).std()
        df['volume_ma'] = df['volume'].rolling(window=20).mean()
        df['volume_ratio'] = df['volume'] / df['volume_ma'].fillna(df['volume'])

        # Market anomaly detection (returns > 2 standard deviations)
        df['anomaly_flag'] = (np.abs(df['returns']) > 2 * df['returns'].std()).astype(int)

        self.stock_data = df
        print(f"✅ Stock data loaded: {df.shape}")
        return df

    def load_social_media_data(self, filepath='data/raw/cvna_social_media_data.csv'):
        """Load social media data"""
        if os.path.exists(filepath):
            df = pd.read_csv(filepath)
            df['date'] = pd.to_datetime(df['date']).dt.date
            self.social_data = df
            print(f"✅ Social media data loaded: {df.shape}")
            return df
        else:
            print(f"❌ Social media data not found at {filepath}")
            return None

    def integrate_datasets(self):
        """Merge stock and social media data"""
        if self.stock_data is None or self.social_data is None:
            raise ValueError("Both stock and social data must be loaded first")

        # Select key columns from stock data
        stock_cols = ['date', 'close', 'volume', 'returns', 'volatility', 'volume_ratio', 'anomaly_flag']
        stock_subset = self.stock_data[stock_cols].copy()

        # Merge datasets
        integrated = pd.merge(
            stock_subset,
            self.social_data,
            on='date',
            how='inner'
        )

        # Sort by date
        integrated = integrated.sort_values('date').reset_index(drop=True)

        # Create additional derived features
        integrated['price_change'] = integrated['close'].pct_change()
        integrated['volume_spike'] = (integrated['volume_ratio'] > 2).astype(int)

        # Social media derived features
        integrated['engagement_per_post'] = (
            integrated['engagement_per_day'] / integrated['posts_per_day'].clip(lower=1)
        )

        integrated['social_momentum'] = integrated['posts_per_day'].pct_change().fillna(0)

        self.integrated_data = integrated
        print(f"✅ Data integration complete: {integrated.shape}")
        print(f"Date range: {integrated['date'].min()} to {integrated['date'].max()}")

        return integrated

    def save_integrated_data(self, filepath='data/processed/cvna_integrated_dataset.csv'):
        """Save the integrated dataset"""
        if self.integrated_data is not None:
            self.integrated_data.to_csv(filepath, index=False)
            print(f"✅ Integrated dataset saved to {filepath}")

            # Print summary statistics
            print("\n📊 Dataset Summary:")
            print(f"Total records: {len(self.integrated_data)}")
            print(f"Anomaly days: {self.integrated_data['anomaly_flag'].sum()}")
            print(f"Volume spikes: {self.integrated_data['volume_spike'].sum()}")
            print(f"Average daily posts: {self.integrated_data['posts_per_day'].mean():.1f}")

        else:
            print("❌ No integrated data to save")

# Usage example
if __name__ == "__main__":
    integrator = CVNADataIntegrator()

    # Load your existing CVNA stock data (update path as needed)
    stock_data = integrator.load_existing_stock_data('data/cvna.csv')  # Your existing file

    # Load social media data
    social_data = integrator.load_social_media_data()

    # Integrate datasets
    integrated_data = integrator.integrate_datasets()

    # Save integrated data
    integrator.save_integrated_data()

    print("\n🎉 Integration complete!")
