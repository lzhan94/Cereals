# Coding Challenge - Cereals


###1. Description: 
This is the solution to the coding challenge. 

The program, cereals.py, collects data by searching www.walmart.com, using the given search_terms and brands.
The search_terms and brands can be modified inside the code.

The program collects the *ranking, name, brand, search term, ratings, number of reviews*, and *date* for a given product that comes up in the results page when searching by *search term*. 

It takes a command line argument, filepath, for the desired location of cereals.csv.
If no filepath is given, the default is the directory of cereals.py.
If cereals.csv does not exist, it will be created. If it does, the new data will be appended to it.

###2. To run the program:
The program, cereals.py, requires Python 2.7 with the following packages:
  * os
  * sys
  * csv
  * urllib2
  * beautifulsoup4
  * datetime

Run the program with an argument for the location of cereals.csv
For instance, if the absolute path for cereals.csv is /home/username/tmp/cereals.csv, then the command line argument should be "/home/username/tmp", i.e.
  
    $python cereals.py /home/username/tmp
  

###3. To let it run every day:
On a Unix OS, in the shell session, type the following
  
    $crontab -e

This will open a file. Please insert the following line at the end of the file:
  
    * * */1 * * /usr/bin/python /absolute/path/to/cereals.py filepath
  
/absolute/path/to/cereals.py should be replaced by the actual absolute path to cereals.py. filepath should be replaced by the absolute path to the directory containing cereals.csv.


###4. Notes on implementation decisions:
The program only looks at the search result page to scrape the data instead of going into each product's page, which would be time inefficient. As a result, only the brands given in the list "brands" can be indicated in the data. If a product is not from one of the given brands, its brand will be marked as "Other". Similarly, a product's rating will be rounded to 0.5 steps.
There is a trade-off between time efficiency and accuracy. Considering the amount of time needed to run the other version (opening each product's page), I decided to choose time efficiency over accuracy.
