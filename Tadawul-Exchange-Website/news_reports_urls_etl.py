import json
import csv
import os

def save_file(reports_urls_arr, year, type):
	base_dir = 'reports_urls_csvs/' + type + '/'
	
	if not os.path.exists(base_dir):
		os.makedirs(base_dir)

	keys = reports_urls_arr[0].keys()

	with open(base_dir + year + '.csv', 'w', newline='') as output_file:
		dict_writer = csv.DictWriter(output_file, keys)
		dict_writer.writeheader()
		dict_writer.writerows(reports_urls_arr)
          


def parse_temp(file_name, filter_type, website_url):
    reports_url_dict = {}

    with open(file_name, 'r') as file:
        for line in file:
            if filter_type in line:
                date = line.strip().split('.pdf')[-2].split('Report+')[-1]

                
                if '-' in date:
                    year = date.split('-')[-1]
                elif '_' in date:
                    year = date.split('_')[-1]

                if '+' in year or '_' in year:
                    continue

                if year in reports_url_dict.keys():
                    if len(reports_url_dict[year]) > 0:
                        if date == reports_url_dict[year][-1]['date']:
                            continue
                        else:
                            reports_url_dict[year].append({'date':date, 'url':website_url+line.strip()})

                    else:
                        reports_url_dict[year].append({'date':date, 'url':website_url+line.strip()})

                else:
                    reports_url_dict[year] = []

    return reports_url_dict


def main():
    website_url = 'https://www.saudiexchange.sa'


    reports_url_dict = parse_temp(file_name='temp', filter_type='Monthly+Trading+and+Ownership+By+Nationality+Report', 
                                  website_url=website_url)
    for year in reports_url_dict.keys():
        save_file(reports_urls_arr = reports_url_dict[year], year = year, type = 'Monthly Trading By Nationality')



    reports_url_dict = parse_temp(file_name='temp', filter_type='Weekly+Trading+and+Ownership+By+Nationality+Repor',
                                   website_url=website_url)
    for year in reports_url_dict.keys():
        save_file(reports_urls_arr = reports_url_dict[year], year = year, type = 'Weekly Trading By Nationality')



main()