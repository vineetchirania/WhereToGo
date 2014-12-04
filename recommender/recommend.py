import sys,os
import re
import operator
from collections import defaultdict
import MySQLdb

# Add Project home directory to the sys path
PROJECT_PATH = os.path.abspath(os.curdir)
if 'WhereToGo' in PROJECT_PATH:
    PROJECT_PATH = re.sub('(.*?WhereToGo).*',r'\1',PROJECT_PATH)
sys.path.append(PROJECT_PATH)
from Utilities.sql_utils import SQL

mysql = SQL('localhost','root','harry123','tourism')

query = "select c.name,rating from activity a, city c, activity_mapping am where a.id=am.activity_id and c.id=am.city_id and a.activity in ({0});"

def find_destination(activity_list):
    activity_csv = "'" +  "','".join(activity_list) + "'"
    result = mysql.select_query(query.format(activity_csv))
    city_map = defaultdict(int)
    for city,rating in result:
        try:
            city = city.strip()
            rating = int(rating)
            city_map[city] += rating
        except:
            print 'Exception for:',city,rating
    # Sort on reverse rating
    recommended_cities = sorted(city_map.items(), key=operator.itemgetter(1),reverse=True)
    print 'Following cities recommended for',activity_csv
    for city,rating in recommended_cities:
        print city,rating

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        activity_list = ['beach','offbeat','church']
    else:
        activity_list = args[1:]
    find_destination(activity_list)
