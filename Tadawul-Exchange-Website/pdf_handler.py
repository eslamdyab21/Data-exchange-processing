import pandas as pd
import subprocess
import pdfplumber
import json
import os
from utils import parse_pdf_page_5, parse_pdf_page_6

def download_pdf(year, date, type):
    pdf_download_path = os.getcwd()+'/pdfs'

    if type == 'monthly':
        base_path = 'reports_urls_csvs/Monthly Trading By Nationality/'
        pdf_file_name = date + '-Monthly.pdf'
    
    elif type == 'weekly':
        base_path = 'reports_urls_csvs/Weekly Trading By Nationality/'
        pdf_file_name = date + '-Weekly.pdf'

    
    path = base_path + year + '.csv'
    df = pd.read_csv(path)

    pdf_url = df[df['date'] == date]['url'].values[0]

    if(pdf_file_name in os.listdir(pdf_download_path)):
        print(pdf_file_name + ' is downloaded before, skipping download step......')
    else:
        subprocess.check_call(["./wget.sh", pdf_url, pdf_download_path, pdf_file_name])

    return 'pdfs/' + pdf_file_name



def convert_pdf_to_csv(pdf_file_path): 
    with pdfplumber.open(pdf_file_path) as pdf:
        # page 5
        table_data = parse_pdf_page_5(pdf.pages[4])
        print(json.dumps(table_data, indent=1))

        # page 6
        table_data = parse_pdf_page_6(pdf.pages[5])
        print(json.dumps(table_data, indent=1))




def main():
    pdf_file_path = download_pdf(year = '2023', date = '31-07-2023', type = 'monthly')
    convert_pdf_to_csv(pdf_file_path)


main()