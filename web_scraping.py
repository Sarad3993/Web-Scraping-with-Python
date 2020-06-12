# Scraping english premier league(EPL) 2019/2020 table using python with beautiful soup library:
# Here we use DataFrame of panda library to export it as csv:

import pandas as pd
import requests
from bs4 import BeautifulSoup


def premier_league():  # creating a user defined function

    url = 'https://www.skysports.com/premier-league-table'
    # ulr of the website we want to scrape data from

    page = requests.get(url)

    soup = BeautifulSoup(page.text,'html.parser')
    #print(soup)  # to check if our required text is parsed or not

    # to find the required table class from our whole html page source
    league_table = soup.find('table',class_='standing-table__table callfn')
    # print(league_table)
    # prints information about whole table class on console

    league_list =[] #creating empty list (later used for appending data from dictionary)

    # searching for tbody inside table class
    for teams in league_table.find_all('tbody'):
        # loops through every teams in the body section
        rows = teams.find_all('tr')
        # searching for table row class inside tbody

        for row in rows:
            epl_club = row.find('td',class_='standing-table__cell standing-table__cell--name').text.strip()
            # strip() removes the spaces in between
            # .txt is used convert the scraped data into text format...if not done so data is returned in html format

            epl_games_played = row.find_all('td',class_='standing-table__cell')[2].text.strip()
            # for indexing simply open page source of that webpage first
            # and carefully analyze the suitable index in each case for that table data
            # Note: index always starts from 0

            epl_games_won = row.find_all('td',class_='standing-table__cell is-hidden--bp35')[0].text.strip()
            # here indexing is different i.e it has started from 0 again cuz class name is different...look carefully

            epl_games_draw = row.find_all('td', class_='standing-table__cell is-hidden--bp35')[1].text.strip()

            epl_games_lost = row.find_all('td', class_='standing-table__cell is-hidden--bp35')[2].text.strip()

            epl_goals_for = row.find_all('td', class_='standing-table__cell is-hidden--bp35')[3].text.strip()

            epl_goals_against = row.find_all('td', class_='standing-table__cell is-hidden--bp35')[4].text.strip()

            epl_goal_diff= row.find_all('td', class_='standing-table__cell')[8].text.strip()

            epl_total_points = row.find_all('td', class_='standing-table__cell')[9].text.strip()

            # no need to create an index or serial no for above data as pandas's DataFrame does that by default 

            league_data = {
                'Clubs' : epl_club,
                'Games Played' : epl_games_played,
                'Games Won': epl_games_won,
                'Games Draw': epl_games_draw,
                'Games Lost': epl_games_lost,
                'Goal For': epl_goals_for,
                'Goal Against': epl_goals_against,
                'Goal Difference': epl_goal_diff,
                'Total Points': epl_total_points
            }  #creating dictionary of scraped data

            league_list.append(league_data) # coverting above dictionary into list by appending the data one by one as loop runs

        data_frame = pd.DataFrame(league_list) # using pandas DataFrame to export above data in csv format
        print(data_frame) # prints scraped data on console


        data_frame.to_csv('premierleague.csv') # for creating csv file of above scraped data

print("The scraped data of premier league 2019/2020 is shown below:")
premier_league() # invoking the function
