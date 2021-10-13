import datetime

class Covid19Record:
    '''
    Represents a Covid19 record from a CSV file
    Author : Darshilkumar Khunt
    '''

    pr_uid = ""
    pr_name = ""
    pr_name_fr = ""
    date = ""
    num_conf = ""
    num_prob = ""
    num_deaths = ""
    num_total = ""
    num_today = ""
    rate_total = ""


    def __init__(self, pr_uid, pr_name, pr_name_fr, date, num_conf, num_prob, num_deaths, num_total, num_today, rate_total) :
            self.pr_uid = pr_uid
            self.pr_name = pr_name
            self.pr_name_fr = pr_name_fr
            self.date = date
            self.num_conf = num_conf
            self.num_prob = num_prob
            self.num_deaths = num_deaths
            self.num_total = num_total
            self.num_today = num_today
            self.rate_total = rate_total

    # Mutator for pr_uid
    def set_pr_uid(self, pr_uid):
        self.pr_uid = pr_uid

    # Accessor for pr_uid
    def get_pr_uid(self):
        return self.pr_uid

    # Mutator for pr_name
    def set_pr_name(self, pr_name):
        self.pr_name = pr_name

    # Accessor for pr_name  
    def get_pr_name(self):
        return self.pr_name

    # Mutator for pr_name_fr
    def set_pr_name_fr(self, pr_name_fr):
        self.pr_name_fr = pr_name_fr

    # Accessor for pr_name_fr  
    def get_pr_name_fr(self):
        return self.pr_name_fr

    # Mutator for date
    def set_date(self, date):
        self.date = date

    # Accessor for date 
    def get_date(self):
        return self.date

    # Mutator for num_conf
    def set_num_conf(self, num_conf):
        self.num_conf = num_conf

    # Accessor for num_conf   
    def get_num_conf(self):
        return self.num_conf

    # Mutator for num_prob
    def set_num_prob(self, num_prob):
        self.num_prob = num_prob

    # Accessor for num_prob    
    def get_num_prob(self):
        return self.num_prob

    # Mutator for num_deaths
    def set_num_deaths(self, num_deaths):
        self.num_deaths = num_deaths

    # Accessor for num_deaths  
    def get_num_deaths(self):
        return self.num_deaths

    # Mutator for num_total
    def set_num_total(self, num_total):
        self.num_total = num_total

    # Accessor for num_total    
    def get_num_total(self):
        return self.num_total

    # Mutator for num_today
    def set_num_today(self, num_today):
        self.num_today = num_today

    # Accessor for num_today  
    def get_num_today(self):
        return self.num_today

    # Mutator for rate_total
    def set_rate_total(self, rate_total):
        self.rate_total = rate_total

    # Accessor for rate_total  
    def get_rate_total(self):
        return self.rate_total

    def convert_float(self,value):
        '''
        Method converts string to float
        '''
        if(value == None):
            return "None"
        else:
            try:
                return float(value)
            except:
                return "None"


    def convert_date(self,value):
        '''
        Method converts string to date object
        '''
        try:
            return datetime.datetime.strptime(str(value), '%Y-%m-%d')     
        except:
            return None

    def to_string(self):
        """"
        Method prints Covid19Record object as string
        """
        txt = "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}"
        return txt.format(self.pr_uid, self.pr_name, self.pr_name_fr, self.date, self.num_conf, self.num_prob, self.num_deaths, self.num_total, self.num_today, self.rate_total)