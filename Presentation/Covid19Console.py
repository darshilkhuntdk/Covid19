from Business.Covid19Service import Covid19Service
from Model.Covid19Record import Covid19Record

class Covid19Console:
    """"
    This is a simple console based view for user interaction with the program
    Author: Darshilkumar Khunt
    """
    def __init__(self):
        self.service = Covid19Service()

    def main(self):
        # show user choice menu
        self.menu()

        # read user choice
        choice = input("Enter choice -> ")

        while choice != "e":
            """
            Perform operations based on user choice
            """
            if choice == "l":
                # load data from file
                print("Loading data from file to database...")
                self.load_records_from_file_to_db()

            elif choice == "a":
                # list all records
                print("Listing all record...")
                self.print_list_all()

            elif choice == "c":
                # list all records
                print("Selecting record by id...")
                self.select_record_by_id()

            elif choice == "i":
                print("Enter new values for the record...")
                # insert new record
                self.insert()
            
            elif choice == "u":
                print("Update values for the record...")
                # update existing record
                self.update(id)

            elif choice == "d":
                print("delete specific record...")
                # delete record
                self.delete(id)  

            elif choice == "h":
                print("creating horizontal bar chart...")
                # create bar chart 
                self.create_chart(id)  

            else:
                print("Invalid option")

            self.menu()
            choice = input("Enter choice -> ")

    def menu(self):
        self.personal_info()
        print("*************** Covid19 Record Program *****************")
        print("Covid19Record Menu : "
            "\n 'l' : Load records from file to database"
            "\n 'a' : List all Covid19 Records"
            "\n 'c' : List selected Covid19 Record"
            "\n 'i' : Insert new Covid19 Record"
            "\n 'u' : Update Covid19 Record"
            "\n 'd' : Delete Covid19 Record"
            "\n 'h' : Create Horizontal Bar Chart" 
            "\n 'e' : Exit the program")

    def load_records_from_file_to_db(self):
        """
        Method load all records from csv file to database table
        """
        self.service.load_records()

    def print_list_all(self):
        """
        Method prints list of records to console
        """
        self.service.get_all_records()

    def select_record_by_id(self):
        """
        Method prints selected record
        """
        rid = input("Enter Id of Record you want to select: ")
        self.service.get_one_record(rid)

    def insert(self):
        """
        Method inserts new records by requesting user inputs
        """
        pr_uid = input("Enter pr_uid : ")
        pr_name = input("Enter pr_name : ")
        pr_name_fr = input("Enter pr_name_fr : ")
        date = input("Enter Date : ")
        num_conf = input("Enter num_conf : ")
        num_prob = input("Enter num_prob : ")
        num_deaths = input("Enter num_deaths : ")
        num_total = input("Enter num_total : ")
        num_today = input("Enter num_today : ")
        rate_total = input("Enter rate_total : ")
        self.service.insert_record(pr_uid, pr_name, pr_name_fr, date, num_conf, num_prob, num_deaths, num_total, num_today, rate_total)

    def update(self, id):
        """
        Method updates existing records by requesting user inputs
        """
        id = input("Enter Id of record you want to update: ")

        pr_uid = input("Enter new pr_uid : ")
        pr_name = input("Enter new pr_name : ")
        pr_name_fr = input("Enter new pr_name_fr : ")
        date = input("Enter new Date : ")
        num_conf = input("Enter new num_conf : ")
        num_prob = input("Enter new num_prob : ")
        num_deaths = input("Enter new num_deaths : ")
        num_total = input("Enter new num_total : ")
        num_today = input("Enter new num_today : ")
        rate_total = input("Enter new rate_total : ")
        self.service.update_record(pr_uid, pr_name, pr_name_fr, date, num_conf, num_prob, num_deaths, num_total, num_today, rate_total, id)


    def delete(self, id):
        """
        Method deletes records specified by id
        :param id: id to delete
        """
        id = input("Enter Id of record you want to delete: ")
        self.service.delete_record(id) 

    def create_chart(self, id):
        """
        Method creates horizontal bar chart for specified id
        :param id: id to create bar chart
        """
        id = input("Enter Id of record you want to create chart: ")
        self.service.create_chart(id)

    def personal_info(self):
        # Method prints personal infoemation
        first_name, last_name = "Darshilkumar", "Khunt"
        print("\nName: {} {}".format(first_name, last_name))