import sys,os
import re
import MySQLdb

# Add Project home directory to the sys path
PROJECT_PATH = os.path.abspath(os.curdir)
if 'WhereToGo' in PROJECT_PATH:
    PROJECT_PATH = re.sub('(.*?WhereToGo).*',r'\1',PROJECT_PATH)
sys.path.append(PROJECT_PATH)
from Utilities.sql_utils import SQL

mysql = SQL('localhost','root','harry123','tourism')

def populate_indian_cities():
    query = "insert into city (name,state,country) VALUES ('{0}','{1}','{2}');"
    with open('indian_cities','r') as city:
        city_data = city.readlines()
    country = 'India'
    count = 0
    for line in city_data:
        if not line or not line.strip(): continue
        names = [word.strip() for word in line.split(',')]
        cities, state = names[:-1], names[-1].strip('\n')
        # Remove extra spaces beween words
        state = ' '.join(state.split())
        for city in cities: 
            city = ' '.join(city.split())
            mysql.insert_query(query.format(city,state,country))
            count += 1
    print count,'domestic cities inserted in database.'

def populate_foreign_cities():
    query = "insert into city (name,country) VALUES ('{0}','{1}');"
    with open('foreign_cities','r') as city:
        city_data = city.readlines()
    count = 0
    for line in city_data:
        if not line or not line.strip(): continue
        names = [word.strip() for word in line.split(',')]
        city, country = names
        mysql.insert_query(query.format(city,country))
        count += 1
    print count,'foreign cities inserted in database.'

if __name__ == "__main__":
    populate_indian_cities()
    populate_foreign_cities()

