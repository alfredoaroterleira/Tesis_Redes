import pandas as pd

def load_data(file_path):
    """Load contract data from an Excel file."""
    df = pd.read_excel(file_path)
    return df

def process_data(df):
    """Process the contract data for analysis."""
    # Example processing steps
    df['fecha'] = pd.to_datetime(df['fecha'])  # Convert date column to datetime
    df.dropna(subset=['RUC', 'monto'], inplace=True)  # Drop rows with missing RUC or amount
    df['year'] = df['fecha'].dt.year  # Extract year from date
    return df

def save_processed_data(df, output_path):
    """Save the processed data to a CSV file."""
    df.to_csv(output_path, index=False)