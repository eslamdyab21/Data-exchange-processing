skip_lines = [
        "Monthly Report - Main Market",
        "Value Traded (by Nationality and Investor Type)",
        "Main Market Value Traded Breakdown - By Nationality and Investor Type",
        "Buy Sell Net Value Traded",
        "Nationality Investor Type",
        "SAR Difference",
        "SAR % of Total Buys SAR % of Total Sells",
        "(Buy - Sell) (% Buy - % Sell)",
        "Value Traded (by Investor Classification)",
        "Main Market Value Traded Breakdown - By Investor Classification"
    ]


def parse_pdf_page_5(page):
    table_data = []
    current_section = None

    
    for line in page.extract_text().split('\n'):
        line = line.strip()
        
        if line in skip_lines:
            continue

        if line == 'Individuals:':
            current_section = 'Individuals'
            nationality = 'Saudi'
        
        elif line == 'Saudi Institutions:':
            current_section = 'Institutions'
            nationality = 'Saudi'

        elif line == 'Total Saudi Investors':
            current_section = 'Total Saudi Investors'
            nationality = 'Saudi'

        elif line.split()[0] == 'Individuals':
            current_section = None
            nationality = 'GCC'

        elif 'SWAP Holders' in line:
            current_section = None
            nationality = 'Foreign'

            
        elif 'Grand Total' in line:
            current_section = 'Grand Total'
            nationality = 'Grand Total'


        if len(line.split()) > 2 and current_section != 'Grand Total':
            splitted_table_data = line.split()

            if ',' in splitted_table_data[1]:
                investor_type = splitted_table_data[0]
            elif ',' in splitted_table_data[2]:
                investor_type = ' '.join(splitted_table_data[0:2])
                del splitted_table_data[1]
            elif ',' in splitted_table_data[3]:
                investor_type = ' '.join(splitted_table_data[0:3])
                del splitted_table_data[1:3]
            elif ',' in splitted_table_data[4]:
                investor_type = ' '.join(splitted_table_data[0:4])
                del splitted_table_data[1:4]
    

            buy_sar = splitted_table_data[1]
            buy_of_total_buys = splitted_table_data[2]
            sel_sar = splitted_table_data[3]
            sel_of_total_buys = splitted_table_data[4]
            net_value_traded_sar = splitted_table_data[5]
            net_value_traded_difference = splitted_table_data[6]

            if current_section == None:
                investor_type_string = investor_type
            else:
                investor_type_string = current_section + '-' + investor_type

            table_data.append({ 'Nationality': nationality,
                                'Investor Type': investor_type_string, 
                                'Buy SAR':buy_sar, 
                                'Buy % of Total Buys':buy_of_total_buys,
                                'Sell SAR': sel_sar,
                                'Sel % of Total Buys':sel_of_total_buys,
                                'Net Value Traded SAR (Buy - Sell)':net_value_traded_sar,
                                'Net Value Traded Difference (% Buy - % Sell)':net_value_traded_difference})



        elif current_section == 'Grand Total' and len(line.split()) > 2:
            splitted_table_data = line.split()

            buy_sar = splitted_table_data[0]
            buy_of_total_buys = splitted_table_data[1]
            sel_sar = splitted_table_data[2]
            sel_of_total_buys = splitted_table_data[3]


            table_data.append({ 'Nationality': nationality,
                                'Investor Type': None,
                                'Buy SAR':buy_sar, 
                                'Buy % of Total Buys':buy_of_total_buys,
                                'Sell SAR': sel_sar,
                                'Sel % of Total Buys':sel_of_total_buys,
                                'Net Value Traded SAR (Buy - Sell)':None,
                                'Net Value Traded Difference (% Buy - % Sell)':None})
            

    return table_data




def parse_pdf_page_6(page):
    table_data = []
    current_section = None

    
    for line in page.extract_text().split('\n'):
        line = line.strip()
        
        if line in skip_lines:
            continue

        if line in 'Definitions':
            break
            
        if 'Grand Total' in line:
            current_section = 'Grand Total'


        if len(line.split()) > 2 and current_section != 'Grand Total':
            splitted_table_data = line.split()

            investor_classification = splitted_table_data[0]
            buy_sar = splitted_table_data[1]
            buy_of_total_buys = splitted_table_data[2]
            sel_sar = splitted_table_data[3]
            sel_of_total_buys = splitted_table_data[4]
            net_value_traded_sar = splitted_table_data[5]
            net_value_traded_difference = splitted_table_data[6]


            table_data.append({ 'Investor Classification': investor_classification,
                                'Buy SAR':buy_sar, 
                                'Buy % of Total Buys':buy_of_total_buys,
                                'Sell SAR': sel_sar,
                                'Sel % of Total Buys':sel_of_total_buys,
                                'Net Value Traded SAR (Buy - Sell)':net_value_traded_sar,
                                'Net Value Traded Difference (% Buy - % Sell)':net_value_traded_difference})




        elif current_section == 'Grand Total' and len(line.split()) > 2:
            splitted_table_data = line.split()

            buy_sar = splitted_table_data[0]
            buy_of_total_buys = splitted_table_data[1]
            sel_sar = splitted_table_data[2]
            sel_of_total_buys = splitted_table_data[3]

            table_data.append({ 'Investor Classification': current_section,
                                'Buy SAR':buy_sar, 
                                'Buy % of Total Buys':buy_of_total_buys,
                                'Sell SAR': sel_sar,
                                'Sel % of Total Buys':sel_of_total_buys,
                                'Net Value Traded SAR (Buy - Sell)':None,
                                'Net Value Traded Difference (% Buy - % Sell)':None})
            

    return table_data