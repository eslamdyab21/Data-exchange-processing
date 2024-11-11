import pandas as pd


def get_line_selections():
    file_name = 'raw_data/EFG FO Data.xlsx'
    data = {}

    # Load data from the "EFG FO" and "Ticker info" sheets.
    df_efo = pd.read_excel(file_name, sheet_name = 0)
    df_ticker_info = pd.read_excel(file_name, sheet_name = 1)
    

    # Drop na records
    df_efo = df_efo[~df_efo['FO MTD'].isna()]

    # Merge two dfs
    df_merged = df_efo.merge(df_ticker_info, on='Ticker', how='outer')


    # Drop na records
    df_merged = df_merged[~df_merged.isna().any(axis=1)]

    data['Tickers'] = list(df_merged['Ticker'].unique())
    data['Countries'] = list(df_merged['Country'].unique())
    data['Sectors'] = list(df_merged['Sector'].unique())
    data['Exchanges'] = list(df_merged['EXCHANGE'].unique())
    data['y_axis'] = ['FO WTD', 'FO MTD', 'FO YTD', 'Foreign Headroom', 'FO%']

    return data