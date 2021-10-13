from Persistence.Covid19Data import Covid19Data

class Covid19Service:
    """
    Represents business logic(layer from MCV) for the Covid19Record. It will request persistence layer
    to perform CRUD operations for records
    Author : Darshilkumar Khunt
    """
    def __init__(self):
        self.data_store = Covid19Data()

    def load_records(self):
        return self.data_store.load_records()

    def get_all_records(self):
        return self.data_store.get_all_records()

    def get_one_record(self,rid):
        return self.data_store.get_record_by_id(rid)

    def create_chart(self, id):
        return self.data_store.create_chart(id)

    def insert_record(self,pr_uid, pr_name, pr_name_fr, date, num_conf, num_prob, num_deaths, num_total, num_today, rate_total):
        self.data_store.insert_record(pr_uid, pr_name, pr_name_fr, date, num_conf, num_prob, num_deaths, num_total, num_today, rate_total)
        print("Record inserted successfully...")

    def update_record(self,pr_uid, pr_name, pr_name_fr, date, num_conf, num_prob, num_deaths, num_total, num_today, rate_total,rid):
        self.data_store.update_record(pr_uid, pr_name, pr_name_fr, date, num_conf, num_prob, num_deaths, num_total, num_today, rate_total,rid)
        print("Record updated successfully...")

    def delete_record(self,record_id):
        self.data_store.delete_record(record_id)
        print("Record deleted successfully...")
