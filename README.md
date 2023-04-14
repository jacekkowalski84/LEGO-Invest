# LEGO-Invest
 This project involves analyzing a dataset of LEGO sets and their catalogue prices using Python and its packages. The analysis includes comparing the prices to current market values and assessing which LEGO themes are potentially profitable for investment.

# Dataset Description
The dataset can be found in the 'data/lego_population.csv' subfolder and includes information on 1300 LEGO sets, such as their ID number, theme, year of release, catalogue price, and Amazon price.

# How it Works
1.The program reads the CSV file containing the data and saves it to a dataframe variable.

2.The program updates the 'Amazon price' values by scraping the current price from the Amazon website.

3.The program calculates the average price increase (percentage-wise) per year for each LEGO set by comparing the price difference between the release year and the current year. 

For example, if a LEGO set released in 2020 costs $10 and in 2023 it costs $16, the average price increase per year would be calculated as follows:

[(16-10)/(2023-2020)]/10 * 100% = (6/3)/10 * 100% = 20%

This means that the price of this LEGO set on average increases by 20% each year.

4. Finally, the program calculates the arithmetic mean of the price increase for LEGO sets with the same theme and creates a graphical dashboard that enables users to make informed decisions about investing in future LEGO sets.

Please note that the program requires an internet connection to update the Amazon prices through web scraping.

# Code and Resources Used
Python Version: 3.10.7

Modules: datetime, pandas, selenium, urllib.parse
