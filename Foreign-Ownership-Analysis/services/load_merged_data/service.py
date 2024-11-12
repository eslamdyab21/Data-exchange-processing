import pandas as pd

def load_merged_data():
	file_name = 'raw_data/EFG FO Data.xlsx'

 	# Load data from the "EFG FO" and "Ticker info" sheets.
	df_efo = pd.read_excel(file_name, sheet_name = 0)
	df_ticker_info = pd.read_excel(file_name, sheet_name = 1)
    

	# Drop na records
	df_efo = df_efo[~df_efo['FO MTD'].isna()]

	# Merge two dfs
	df_merged = df_efo.merge(df_ticker_info, on='Ticker', how='outer')


	# Drop na records
	df_merged = df_merged[~df_merged.isna().any(axis=1)]

	return df_merged