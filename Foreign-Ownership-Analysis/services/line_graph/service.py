import pandas as pd
import numpy as np

def get_line_data(df_merged = None, ticker = None, country = None, sector = None, exchange = None, y_axis = None, start_date = None, end_date = None):
    
    if df_merged is not None:
        df_filtered = df_merged

    else:
        file_name = 'raw_data/EFG FO Data.xlsx'

        # Load data from the "EFG FO" and "Ticker info" sheets.
        df_efo = pd.read_excel(file_name, sheet_name = 0)
        df_ticker_info = pd.read_excel(file_name, sheet_name = 1)
        

        # Drop na records
        df_efo = df_efo[~df_efo['FO MTD'].isna()]

        # Merge two dfs
        df_merged = df_efo.merge(df_ticker_info, on='Ticker', how='outer')


        # Drop na records
        df_filtered = df_merged[~df_merged.isna().any(axis=1)]



    if len(ticker) > 0:
        df_filtered = df_filtered[df_filtered['Ticker'].isin(ticker)]

    if len(country) > 0:
        df_filtered = df_filtered[df_filtered['Country'].isin(country)]

    if len(sector) > 0:
        df_filtered = df_filtered[df_filtered['Sector'].isin(sector)]

    if len(exchange) > 0:
        df_filtered = df_filtered[df_filtered['EXCHANGE'].isin(exchange)]


    if start_date and start_date != 'Invalid Date':

        df_filtered = df_filtered[df_filtered['Date'] >= str(start_date)]


    if end_date and end_date != 'Invalid Date':
        df_filtered = df_filtered[df_filtered['Date'] <= str(end_date)]


    df_filtered = df_filtered.reset_index()
    df_filtered = df_filtered.rename(columns={'index': 'id'})


    return df_filtered.to_json(orient = "records")