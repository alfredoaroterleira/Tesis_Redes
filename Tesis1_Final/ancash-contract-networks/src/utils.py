def load_excel_data(file_path):
    import pandas as pd
    df = pd.read_excel(file_path)
    return df

def clean_data(df):
    # Implement data cleaning steps here
    # For example: handling missing values, renaming columns, etc.
    return df

def extract_yearly_data(df):
    yearly_data = {}
    df['Year'] = df['Fecha'].dt.year
    for year in df['Year'].unique():
        yearly_data[year] = df[df['Year'] == year]
    return yearly_data

def get_unique_companies(df):
    return df['RUC'].unique()