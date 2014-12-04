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

def insert_mapping():
    with open('city_activity_mapping.txt','r') as fin:
        lines = fin.readlines()

        # Get city name to id map
        city_name_to_id_map = {}
        result = mysql.select_query('select id,name from city;')
        for cid,name in result: 
            if name: city_name_to_id_map[name.lower().strip()] = cid

        # Get activity to id map
        activity_to_id_map = {}
        result = mysql.select_query('select id,activity from activity;')
        for aid,activity in result: 
            if activity: activity_to_id_map[activity.lower().strip()] = aid

    mappings_inserted = 0
    for line in lines:
        line = line.strip()
        if not line: continue
        activity, cityString = line.split(':')
        activity = activity.strip()
        cities = cityString.split(',')

        for city in cities:
            city,rating = [a.strip() for a in city.split('|')]
            if not city: continue
            try:
                rating = int(rating)
            except ValueError:
                print 'Rating has invalid value',rating,'for city',city
                continue
            try:
                city_id = city_name_to_id_map[city.lower()]
            except KeyError:
                print 'City not found in db:',city
                query = "insert into city (name) VALUES ('{0}');".format(city)
                city_id = mysql.insert_query(query)
                city_name_to_id_map[city.lower()] = city_id
                print 'Created city, cityid is',city_id
            try:
                activity_id = activity_to_id_map[activity.lower()]
            except KeyError:
                print 'Activity not found in db:',activity
                activity_id = mysql.insert_query("insert into activity (activity) VALUES ('{0}');".format(activity))
                activity_to_id_map[activity.lower()] = activity_id
                print 'Created activity, activity_id is',activity_id

            mysql.insert_query('insert into activity_mapping (activity_id,city_id,rating) VALUES ({0},{1},{2});'.format(activity_id, city_id, rating))
            mappings_inserted += 1

    print 'Total mappings inserted:',mappings_inserted

if __name__ == "__main__":
    insert_mapping()
