import pandas as pd
import numpy as np
import os

def prepare_data() -> pd.DataFrame:
    '''
    Processes and prepares data if prepared data doesn't already exist
    '''
    if os.files.exists('data_management/data/processed_data.csv'):
        print('Loaded data from memory')
        return pd.read_csv('data_management/data/processed_data.csv')
    else:
        print('Processing new data')
        df1 = pd.read_csv('data_management/data/1949770_38.91_-101.50_2019.csv')
        df2 = pd.read_csv('data_management/data/1949770_38.91_-101.50_2020.csv')
        combined_df = pd.concat([df1, df2], ignore_index=True)

        # Select relevant variables
        # This includes wind speed at 100m, surface air pressure, and airtemperature at 2m
        df_selected = combined_df[['Year', 'Month', 'Day', 'wind speed at 100m (m/s)', 'surface air pressure (Pa)', 'air temperature at 2m (C)']]

        # Calculate air density using the ideal gas law
        R = 287.05  # gas constant for dry air in J/(kg·K)
        df_selected['Temperature (K)'] = df_selected['air temperature at 2m (C)'] + 273.15
        df_selected['Air Density (kg/m^3)'] = df_selected['surface air pressure (Pa)'] / (R * df_selected['Temperature (K)'])

        # Filling missing values with the mean of the column - can experiment with zero
        df_selected.fillna(df_selected.mean(), inplace=True)
        print(df_selected.describe())
        print(f"Null values remaining: {df_selected.isnull().sum()}")

        print('Data saved to memory')
        df_selected.to_csv('data_management/data/processed_data.csv', index=False)
        return df_selected