import pandas as pd
import subprocess

def download_pdf(year, date, type):
    if type == 'monthly':
        base_path = 'reports_urls_csvs/Monthly Trading By Nationality/'
        pdf_file_name = date + '-Monthly.pdf'
    
    elif type == 'weekly':
        base_path = 'reports_urls_csvs/Weekly Trading By Nationality/'
        pdf_file_name = date + '-Weekly.pdf'


    path = base_path + year + '.csv'
    df = pd.read_csv(path)

    pdf_url = df[df['date'] == date]['url'].values[0]

    subprocess.check_call(["./wget.sh", pdf_url, pdf_file_name])






def main():
    download_pdf(year = '2023', date = '31-07-2023', type = 'monthly')


main()