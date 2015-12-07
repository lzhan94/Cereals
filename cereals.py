# -*- coding: utf-8 -*-
"""
@author: Lusa Zhan
cereals.py

This is the solution to the coding challenge. 
This program collects data by searching www.walmart.com, using the given search_terms and brands.
The search_terms and brands can be modified inside the code.
The data collected is on the reanking, name, brand, search term, ratings, number of reviews, 
and date for a given product that comes up in the results page when searching the search term. 


"""

#website, brands and search terms
brands = ['Cheerios', 'Kashi','Kellogg\'s','Post']
search_terms=['cereal','cold cereal']          

#put into csv file, data is a list of lists. 
#Each entry in data corresponds to a row in the csv file
def csv_append(data, filepath):
    import csv
    import os
    with open (filepath+'/cereals.csv','ab') as f:
        writer = csv.writer(f)        
        if os.stat('cereals.csv').st_size == 0:
            writer.writerow(['rank', 'title','brand','search_term','rating','no_of_reviews', 'year','month','day','hour','minute'])
        writer.writerows(data)

#collect the data according to the search_terms(list) and brands(list)
#puts it into cereals.csv file found in filepath
def collect(search_terms, brands, filepath):
    import urllib2   
    from bs4 import BeautifulSoup
    import datetime
    now = datetime.datetime.now()
    data = []
    print("Running:" + str(now))
    
    #go through each search item
    for search_term in search_terms:
        rank = 0
        page_counter = 1
        term = search_term.replace(" ", "%20")
        url = "http://www.walmart.com/search/?query=" + term
        end = False
        
        #while there is a next page
        while(not end):
            
            page_counter = page_counter+1
            html = urllib2.urlopen(url)
            
            soup = BeautifulSoup(html, from_encoding="utf-8")
            product_soup = soup.findAll('div', class_='js-tile js-tile-landscape tile-landscape')
            
            #iterate through each product
            for product in product_soup:
                
                #find name
                rank = rank + 1
                title_html = product.find('a', class_='js-product-title')
                title = title_html.text
                title = title
                
                #set default values
                b = "Other"
                rating = 0
                no_of_reviews = 0
                for brand in brands:
                    if brand in title:
                        b = brand
                reviews = product.find('span', class_='js-reviews')
                if reviews is not None:
                    ratings = reviews.find('span', class_='visuallyhidden').text.split(" ")
                    ratings = float(ratings[0])
                    no_of_reviews = reviews.find('span',class_='stars-reviews').text.split(" ")
                    no_of_reviews = int(no_of_reviews[0][1:-1])
                #put the results into the csv
                result = [rank, title.encode('utf-8'), b.encode('utf-8'), search_term.encode('utf-8'), ratings, no_of_reviews, now.year, now.month, now.day, now.hour, now.minute]                   
                data.append(result)
            
            #save href for next page if there is one
            nextpage = soup.find('a', class_='paginator-btn paginator-btn-next')
            if nextpage is None:
                end = True
            else:
                url = "http://www.walmart.com/search/" + nextpage['href']
    csv_append(data, filepath)
    print("data collection done")            


#main
def main(filepath):
	collect(search_terms, brands, filepath)

if __name__=='__main__':
	import sys
	import os
	if len(sys.argv)<2:
		filepath = sys.path[0]
	else:
		filepath = sys.argv[1]
	main(filepath)
