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

def fetch_activities_from_db():
    activities = mysql.select_query('select activity from activity;')
    options = []
    for result in activities:
        activity, = result
        option = activity, activity
        options.append(option)
    return tuple(options)
