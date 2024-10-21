from get_source_code import SourceCode

class Leetcode(SourceCode):
    def __init__(self, username):
        url = f'https://leetcode.com/u/{username}/'
        super.__init__(self, url)
    
    def extractDetails(self):
        pass
    
    def extractCalander(self):
        month_data = {}
        for month_num in range(1, 13): 
            month_class = f'month {month_num}'
            month_g = self.soup.find('g', class_=month_class)
            month_list = []

            if month_g:
                for week_num in range(1, 6): 
                    week_class = f'week {week_num}'
                    week_g = month_g.find('g', class_=week_class)

                    if week_g:
                        rects = week_g.find_all('rect', class_='cursor-pointer')
                        for rect in rects:
                            fill = rect.get('fill', '')
                            if 'green' in fill:
                                month_list.append(1)
                            elif fill == 'var(--fill-tertiary)':
                                month_list.append(0)
                            elif fill == 'transparent': #check
                                month_list.append(-1)
                            else:
                                month_list.append(-1)

            month_data[month_class] = month_list

        return month_data
    

if __name__ == '__main__':
    username = 'khaleeque56'
    leetcode = Leetcode(username)
    # print(leetcode.extractCalander()) # For testing

