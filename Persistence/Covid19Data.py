import mysql.connector as msql
from mysql.connector import Error
import csv
from Model.Covid19Record import Covid19Record
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Covid19Data:
    """
    Represents Persistence layer of the Application
    Author : Darshilkumar Khunt
    """
    def __init__(self):
        self.FILE_NAME = "covid19.csv"
        self.CONN = ""

        self.connect()
        # initialize database
        self.initialize_database()

    # Create User with following credential in MySQL workbench before running this program
    # Username: cst8333 Password: cst8333
    def connect(self):
        """
        Method initializes CONN object with MySQL connection
        """
        try:
            self.CONN = msql.connect(host='localhost', user='cst8333', password='cst8333')
            if self.CONN.is_connected():
                cursor = self.CONN.cursor()
                cursor.execute("CREATE DATABASE IF NOT EXISTS covidDB")

        except Error as e:
            print("Error while connecting to MySQL", e)

    def connectDB(self):    
        try:
            self.CONN = msql.connect(host='localhost', database='coviddb', user='cst8333', password='cst8333')

        except Error as e:
            print("Error while connecting to MySQL", e)

    def persist(self):
        """
        Method commits changes made to database
        """
        self.CONN.commit()

    def disconnect(self):
        """
        Method closes sqlite3 connection
        """
        self.CONN.close()

    def initialize_database(self):
        """
        Method initializes database table
        """

        # connect to database
        self.connectDB()

        
        # make cursor object
        cursor = self.CONN.cursor()
        cursor.execute("use coviddb;")

        # query to execute
        query = """CREATE TABLE IF NOT EXISTS covid19data(
                RID INT PRIMARY KEY AUTO_INCREMENT,
                PR_UID VARCHAR(10) NOT NULL,
                PR_NAME VARCHAR(50),
                PR_NAME_FR VARCHAR(50),  
                DATE VARCHAR(20),
                NUM_CONF VARCHAR(10), 
                NUM_PROB VARCHAR(10),
                NUM_DEATHS VARCHAR(10),
                NUM_TOTAL VARCHAR(10),
                NUM_TODAY VARCHAR(10),
                RATE_TOTAL VARCHAR(10))
                """

        # execute query
        cursor.execute(query)

        # commit changes to database
        self.persist()

        # disconnect connection
        self.disconnect()

    def insert_record(self, pr_uid, pr_name, pr_name_fr, date, num_conf, num_prob, num_deaths, num_total, num_today, rate_total):
        """
        Method inserts new record to the database
        :param record: Covid19Record object
        :return:
        """
        try: 
            self.connectDB()
            cursor = self.CONN.cursor()

            query = '''
                INSERT INTO covid19data( PR_UID, PR_NAME, PR_NAME_FR, DATE, NUM_CONF, NUM_PROB, NUM_DEATHS, NUM_TOTAL, NUM_TODAY, RATE_TOTAL ) 
                VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )
                '''

            val = (pr_uid, pr_name, pr_name_fr, date, num_conf, num_prob, num_deaths, num_total, num_today, rate_total)
                    
            cursor.execute(query, val)

            self.persist()
            self.disconnect()

        except:
            self.CONN.rollback()

    def get_all_records(self):
        """
        Method fetches all the records from the database
        :return list of records
        """
        self.connectDB()
        cursor = self.CONN.cursor()

        query = '''
            SELECT * FROM covid19data
            '''

        cursor.execute(query)

        rows = cursor.fetchall()
        # print(rows)

        for row in rows :
            print(row[1],row[2],row[3],row[4],row[5],row[6], row[7], row[8], row[9], row[10])

        result = [list(i) for i in rows]

        self.persist()
        self.disconnect()

        return result

    def get_record_by_id(self, record_id):
        """
        Method lists a record from the database
        :param record_id: record id to fetch
        :return: list of records
        """
        self.connectDB()
        cursor = self.CONN.cursor()

        query = '''
            SELECT * FROM covid19data
            WHERE RID = {}
            '''.format(record_id)

        cursor.execute(query)

        rows = cursor.fetchall()
        print(rows)

        result = [list(i) for i in rows]

        self.persist()
        self.disconnect()

        return result

    def update_record(self, pr_uid, pr_name, pr_name_fr, date, num_conf, num_prob, num_deaths, num_total, num_today, rate_total, record_id):
        """
        Method updates a specified record with new value
        :param record: Covid19Record object
        :param rid: record id to update
        :return:
        """
        self.connectDB()
        cursor = self.CONN.cursor()

        query = '''
            UPDATE covid19data
            SET PR_UID = %s, PR_NAME = %s, PR_NAME_FR = %s, DATE = %s, NUM_CONF = %s, NUM_PROB = %s, NUM_DEATHS = %s, NUM_TOTAL = %s, NUM_TODAY = %s, RATE_TOTAL = %s
            WHERE RID = %s
            '''

        val = (pr_uid, pr_name, pr_name_fr, date, num_conf, num_prob, num_deaths, num_total, num_today, rate_total, record_id)

        cursor.execute(query, val)

        self.persist()
        self.disconnect()

    def delete_record(self, record_id):
        """
        Method deletes specified record from the database
        :param record_id: record id to delete
        :return:
        """
        self.connectDB()
        cursor = self.CONN.cursor()

        query = '''
            DELETE
            FROM covid19data
            WHERE RID = {}
            '''.format(record_id)

        cursor.execute(query)

        self.persist()
        self.disconnect() 

    def create_chart(self, id):
        """
        Method creates charts for specified record from the database
        :param id: id to create chart for
        """
        record = self.get_record_by_id(id)

        for index,tuple in enumerate(record):
            province = tuple[2]
            date = tuple[4]
            num_conf = tuple[5]
            num_prob = tuple[6]
            num_deaths = tuple[7]
            num_total = tuple[8]
            num_today = tuple[9]
            rate_total = tuple[10]
            # print(num_conf, num_prob, num_deaths, num_total, num_today, rate_total)        

        new_data = { 'p_name': ['num_conf','num_prob','num_deaths','num_total','num_today','rate_total'],
                    'value1': [float(num_conf), float(num_prob), float(num_deaths), float(num_total), float(num_today), float(rate_total)]}
        
        df = pd.DataFrame.from_dict(new_data); df
        fig = plt.figure(figsize=(8,5))
        ax1=plt.subplot(1,1,1)
        ax1.barh(df.p_name, df.value1)
        for Y,X in enumerate(df.value1):
            ax1.annotate("{:,}".format(float(X)), xy=(X,Y))
        ax1.set_xlim(0,int(df.value1.max()) * 1.5)
        ax1.xaxis.grid(linestyle='--',linewidth=0.5)
        ax1.set_axisbelow(True)
        ax1.set_title(province+' Covid data: '+date, fontsize = 18, weight ='bold')
        plt.show()


    def load_records(self):
        """
        Method loads record from file to the list
        """

        #covid19 record list
        data_list = []

        i=0;
        try:
            self.connectDB()

            with open(self.FILE_NAME, 'r', newline='') as data_file:
                reader = csv.reader(data_file)
                next(reader, None)  # Skip the header.

                for row in reader:
                    pr_uid = row[0]
                    pr_name = row[1]
                    pr_name_fr = row[2]
                    date = row[3]
                    num_conf = row[5]
                    num_prob = row[6]
                    num_deaths = row[7]
                    num_total = row[8]
                    num_today = row[13]
                    rate_total = row[15]

                    # make new covid19Record object
                    new_record = Covid19Record(pr_uid, pr_name, pr_name_fr, date, num_conf, num_prob, num_deaths, num_total, num_today, rate_total)

                    cursor = self.CONN.cursor()

                    query = '''
                        INSERT INTO covid19data( PR_UID, PR_NAME, PR_NAME_FR, DATE, NUM_CONF, NUM_PROB, NUM_DEATHS, NUM_TOTAL, NUM_TODAY, RATE_TOTAL ) 
                        VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )
                        '''

                    val = (pr_uid, pr_name, pr_name_fr, date, num_conf, num_prob, num_deaths, num_total, num_today, rate_total)
                            
                    cursor.execute(query, val)

                    self.persist()

                    # append covi19Record object to list
                    data_list.append(new_record)

                    i = i+1
                    if i > 100:
                         break # skip reading records

        except IOError:
            print("File not found. Path is incorrect")