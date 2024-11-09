import pandas as pd


def get_line_data(ticker = None, country = None, sector = None, exchange = None, y_axis = None):
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


    if ticker:
        df_filtered = df_filtered[df_filtered['Ticker'] == ticker]

    if country:
        df_filtered = df_filtered[df_filtered['Country'] == country]

    if sector:
        df_filtered = df_filtered[df_filtered['Sector'] == sector]

    if exchange:
        df_filtered = df_filtered[df_filtered['EXCHANGE'] == exchange]



    if y_axis:
        df_filtered = df_filtered[['Date', y_axis]]


    return df_filtered