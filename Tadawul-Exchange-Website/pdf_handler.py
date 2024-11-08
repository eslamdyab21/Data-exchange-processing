import pandas as pd
import subprocess
import pdfplumber
import json
import os
import csv
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



def save_file(table_data, pdf_file_path, page):
    base_dir = 'final_reports_csvs/' 
    
    print('saving..... ', pdf_file_path.split('/')[-1].split('.')[0] + page + '.csv')

    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    keys = table_data[0].keys()

    
    with open(base_dir + pdf_file_path.split('/')[-1].split('.')[0] + page + '.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(table_data)
          

def convert_pdf_to_csv(pdf_file_path): 
    with pdfplumber.open(pdf_file_path) as pdf:
        # page 5
        table_data = parse_pdf_page_5(pdf.pages[4])
        save_file(table_data, pdf_file_path, page='-page-5')

        # page 6
        table_data = parse_pdf_page_6(pdf.pages[5])
        save_file(table_data, pdf_file_path, page='-page-6')




def main():
    pdf_file_path = download_pdf(year = '2023', date = '31-07-2023', type = 'monthly')
    convert_pdf_to_csv(pdf_file_path)


main()