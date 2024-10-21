from get_source_code import SourceCode
import re

class GFG(SourceCode):

    color_map = {
            'rgb(218, 226, 137)': 'green',  # Example: light green
            'rgb(156, 192, 105)': 'green',  # Example: medium green
        }

    def __init__(self, username):
        url = f'https://www.geeksforgeeks.org/user/{username}/'
        super.__init__(self, url)
    
    def extractDetails(self):
        pass
    
    def extractCalander(self):
        month_data = {}
        month_g = self.soup.find('svg', class_='ch-domain-container-animation-wrapper')
        
        for month_num in range(1, 13):  
            month_svg = month_g.find('svg', class_=f'ch-domain m_{month_num}')
            month_list = []

            if month_svg:
                days_svg = month_svg.find('svg', class_='ch-subdomain-container')
                
                if days_svg:
                    days_g = days_svg.find_all('rect')
                    for rect in days_g:
                        style = rect.get('style', '')
                        fill_color = re.search(r'fill:\s*([^;]+);', style)
                        fill_color = fill_color.group(1).strip() if fill_color else 'none'
                        day_info = self.color_map[fill_color]
                        month_list.append(day_info)
            month_data[f'month {month_num}'] = month_list
        
        return month_data
    

if __name__ == '__main__':
    username = 'khaleeque56'
    gfg = GFG(username)
    # print(gfg.extractCalander()) # For testing

