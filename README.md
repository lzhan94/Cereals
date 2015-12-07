# Coding Challenge - Cereals


###1. Description: 
This is the solution to the L2 coding challenge. 

The program, cereals.py, collects data by searching www.walmart.com, using the given *search_terms* and *brands*.
The *search_terms* and *brands* can be modified inside the code.

The program collects the *ranking, name, brand, search term, ratings, number of reviews*, and *date* for a given product that comes up in the results page when searching by *search term*. 

It takes a command line argument, filepath, as the absolute path to the csv file.
If no filepath is given, the file will be called cereals.csv and it will be stored in the same directory as cereals.py by default.
If the csv file does not exist, it will be created. If it does exist, the new data will be appended to the existing file.

###2. Running the Program:
The program, cereals.py, requires Python 2.7 with the following packages:
  * os
  * sys
  * csv
  * urllib2
  * beautifulsoup4
  * datetime

Run the program with the filepath of the csv.
For instance, if the absolute path for the csv is /home/username/tmp/cereals.csv, then the command line argument should be "/home/username/tmp/cereals.csv", i.e.
  
    $python cereals.py /home/username/tmp/cereals.csv
  

###3. Scheduling to run it every day:
On a Unix OS, in the shell session, type the following
  
    $crontab -e

This will open a file. Please insert the following line at the end of the file:
  
    * * */1 * * /usr/bin/python /absolute/path/to/cereals.py /home/username/tmp/cereals.csv
  
/absolute/path/to/cereals.py should be replaced by the actual absolute path to cereals.py. /home/username/tmp/cereals.csv should be replaced by the absolute path to the csv file.

This will set the program to run at midnight every day.

Optional: cron will automatically print the output of the file to another log file. If you want to customize this and specify the file that contains outputs, use
  
    * * */1 * * /usr/bin/python /absolute/path/to/cereals.py /home/username/tmp/cereals.csv >> /absolute/path/to/cron.log 2>&1
  

###4. Notes on Implementation Choices:
The program only looks at the search result page to scrape the data instead of going into each product's page, which would be time inefficient. As a result, only the brands given in the list "brands" can be indicated in the data. If a product is not from one of the given brands, its brand will be marked as "Other". Similarly, a product's rating will be rounded to nearest multiple of .5.
There is a trade-off between time efficiency and accuracy. Considering the amount of time needed to run the other version (opening each product's page), I decided to prioritize time efficiency over accuracy.
