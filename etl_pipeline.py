import pandas as pd
from sqlalchemy import create_engine
import requests

def extract_data():
    # Example: Read data from a CSV file
    print("Extracting data...")
    data = pd.read_csv('source_data.csv')
    return data

def transform_data(data):
    print("Transforming data...")
    # Example: Clean and process the data
    data = data.dropna()
    data.loc[:, 'date'] = pd.to_datetime(data['date'])
    return data

def load_data(data):
    print("Loading data...")
    # Example: Save to a database
    engine = create_engine('sqlite:///output_data.db')  # Replace with your database
    data.to_sql('processed_data', engine, if_exists='replace', index=False)

def etl_pipeline():
    data = extract_data()
    transformed_data = transform_data(data)
    load_data(transformed_data)
    print("ETL process completed!")

if __name__ == "__main__":
    etl_pipeline()