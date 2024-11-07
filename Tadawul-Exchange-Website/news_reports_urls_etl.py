import json



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


                if year in reports_url_dict.keys():
                    if len(reports_url_dict[year]) > 0:
                        if date == reports_url_dict[year][-1]['date']:
                            pass
                        else:
                            reports_url_dict[year].append({'date':date, 'url':website_url+line.strip()})

                    else:
                        reports_url_dict[year].append({'date':date, 'url':website_url+line.strip()})

                else:
                    reports_url_dict[year] = []



def main():
    website_url = 'https://www.saudiexchange.sa'


    parse_temp(file_name='temp', filter_type='Monthly+Trading+and+Ownership+By+Nationality+Report', website_url=website_url)
    parse_temp(file_name='temp', filter_type='Weekly+Trading+and+Ownership+By+Nationality+Repor', website_url=website_url)
    

main()