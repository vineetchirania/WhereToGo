import sys
import MySQLdb

class SQL:

    def __init__(self, host, username, password, db):
        self.HOST = host
        self.USERNAME = username
        self.PASSWORD = password
        self.DATABASE = db
        self.db = MySQLdb.connect(self.HOST, self.USERNAME, self.PASSWORD, self.DATABASE)

    def insert_query(self, query):
        try:
            cur = self.db.cursor()
            cur.execute(query)
            sql_id = cur.lastrowid
            self.db.commit()
        except MySQLdb.OperationalError:
            self.db = MySQLdb.connect(self.HOST, self.USERNAME, self.PASSWORD, self.DATABASE)
            return self.insert_query(query)
        except:
            self.db.rollback()
            print 'Rollbacked'
            print query
            raise
        return sql_id

    def delete_query(self, query):
        #print query
        try:
            cur = self.db.cursor()
            cur.execute(query)
            self.db.commit()
        except MySQLdb.OperationalError:
            self.db = MySQLdb.connect(self.HOST, self.USERNAME, self.PASSWORD, self.DATABASE)
            self.delete_query(query)
        except:
            self.db.rollback()
            print
            print query
            raise

    def select_query(self, query):
        try:
            #print query
            cur = self.db.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            return rows
        except MySQLdb.OperationalError:
            self.db = MySQLdb.connect(self.HOST, self.USERNAME, self.PASSWORD, self.DATABASE)
            return self.select_query(query)

    def update_query(self, query):
        #print query
        try:
            cur = self.db.cursor()
            cur.execute(query)
            self.db.commit()
        except MySQLdb.OperationalError:
            self.db = MySQLdb.connect(self.HOST, self.USERNAME, self.PASSWORD, self.DATABASE)
            self.update_query(query)
        except:
            self.db.rollback()
            print
            print query
            raise
