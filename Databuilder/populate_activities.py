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

def populate_activities():
    query = "insert into activity (activity) VALUES ('{0}')";
    with open('city_activity_mapping.txt','r') as fin:
        data = fin.readlines()
    count = 0
    for line in data:
        if not line or not line.strip(): continue
        activity = line.split(':')[0].strip()
        mysql.insert_query(query.format(activity))
        count += 1
    print count,'activities inserted in database.'

if __name__ == "__main__":
    populate_activities()

