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
    update = ""
    num_conf = ""
    num_prob = ""
    num_deaths = ""
    num_total = ""
    num_tested = ""
    num_recover = ""
    percent_recover = ""
    rate_tested = ""
    num_today = ""
    percent_today = ""
    rate_total = ""
    rate_deaths = ""
    num_deaths_today = ""
    percent_death = ""
    num_tested_today = ""
    num_recovered_today = ""
    percent_active = ""
    num_active = ""
    rate_active = ""
    num_total_last14 = ""
    rate_total_last14 = ""
    num_deaths_last14 = ""
    rate_deaths_last14 = ""
    num_total_last7 = ""
    rate_total_last7 = ""
    num_deaths_last7 = ""
    rate_deaths_last7 = ""
    avg_total_last7 = ""
    avg_incidence_last7 = ""
    avg_deaths_last7 = ""
    avg_rate_deaths_last7 = ""



    def __init__(self, pr_uid, pr_name, pr_name_fr, date, update, num_conf, num_prob, num_deaths, num_total, num_tested,
                num_recover, percent_recover, rate_tested, num_today, percent_today, rate_total, rate_deaths, num_deaths_today, 
                percent_death, num_tested_today, num_recovered_today, percent_active, num_active, rate_active, num_total_last14, 
                rate_total_last14, num_deaths_last14, rate_deaths_last14, num_total_last7, rate_total_last7, num_deaths_last7, 
                rate_deaths_last7, avg_total_last7, avg_incidence_last7, avg_deaths_last7, avg_rate_deaths_last7) :

            '''
            String-based constructor, to facilitate reading string values from csv file.
            The strings are cleaned, and converted to the appropriate type where needed, 
            additionally empty strings are converted to null references.
            :param pr_uid 
            :param pr_name 
            :param pr_name_fr 
            :param date 
            :param update 
            :param num_conf 
            :param num_prob 
            :param num_deaths 
            :param num_total 
            :param num_tested 
            :param num_recover 
            :param percent_recover 
            :param rate_tested 
            :param num_today 
            :param percent_today 
            :param rate_total 
            :param rate_deaths 
            :param num_deaths_today 
            :param percent_death 
            :param num_tested_today 
            :param num_recovered_today 
            :param percent_active 
            :param num_active 
            :param rate_active 
            :param num_total_last14 
            :param rate_total_last14 
            :param num_deaths_last14 
            :param rate_deaths_last14 
            :param num_total_last7 
            :param rate_total_last7 
            :param num_deaths_last7 
            :param rate_deaths_last7 
            :param avg_total_last7 
            :param avg_incidence_last7 
            :param avg_deaths_last7 
            :param avg_rate_deaths_last7 
            '''
            self.pr_uid = self.convert_float(pr_uid)
            self.pr_name = pr_name
            self.pr_name_fr = pr_name_fr
            self.date = self.convert_date(date)
            self.update = self.convert_float(update)
            self.num_conf = self.convert_float(num_conf)
            self.num_prob = self.convert_float(num_prob)
            self.num_deaths = self.convert_float(num_deaths)
            self.num_total = self.convert_float(num_total)
            self.num_tested = self.convert_float(num_tested)
            self.num_recover = self.convert_float(num_recover)
            self.percent_recover = self.convert_float(percent_recover)
            self.rate_tested = self.convert_float(rate_tested)
            self.num_today = self.convert_float(num_today)
            self.percent_today = self.convert_float(percent_today)
            self.rate_total = self.convert_float(rate_total)
            self.rate_deaths = self.convert_float(rate_deaths)
            self.num_deaths_today = self.convert_float(num_deaths_today)
            self.percent_death = self.convert_float(percent_death)
            self.num_tested_today = self.convert_float(num_tested_today)
            self.num_recovered_today = self.convert_float(num_recovered_today)
            self.percent_active = self.convert_float(percent_active)
            self.num_active = self.convert_float(num_active)
            self.rate_active = self.convert_float(rate_active)
            self.num_total_last14 = self.convert_float(num_total_last14)
            self.rate_total_last14 = self.convert_float(rate_total_last14)
            self.num_deaths_last14 = self.convert_float(num_deaths_last14)
            self.rate_deaths_last14 = self.convert_float(rate_deaths_last14)
            self.num_total_last7 = self.convert_float(num_total_last7)
            self.rate_total_last7 = self.convert_float(rate_total_last7)
            self.num_deaths_last7 = self.convert_float(num_deaths_last7)
            self.rate_deaths_last7 = self.convert_float(rate_deaths_last7)
            self.avg_total_last7 = self.convert_float(avg_total_last7)
            self.avg_incidence_last7 = self.convert_float(avg_incidence_last7)
            self.avg_deaths_last7 = self.convert_float(avg_deaths_last7)
            self.avg_rate_deaths_last7 = self.convert_float(avg_rate_deaths_last7)

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

    # Mutator for update
    def set_update(self, update):
        self.update = update

    # Accessor for update    
    def get_update(self):
        return self.update

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

    # Mutator for num_tested
    def set_num_tested(self, num_tested):
        self.num_tested = num_tested

    # Accessor for num_tested    
    def get_num_tested(self):
        return self.num_tested

    # Mutator for num_recover
    def set_num_recover(self, num_recover):
        self.num_recover = num_recover

    # Accessor for num_recover    
    def get_num_recover(self):
        return self.num_recover

    # Mutator for percent_recover
    def set_percent_recover(self, percent_recover):
        self.percent_recover = percent_recover
 
    # Accessor for percent_recover   
    def get_percent_recover(self):
        return self.percent_recover

    # Mutator for rate_tested
    def set_rate_tested(self, rate_tested):
        self.rate_tested = rate_tested

    # Accessor for rate_tested  
    def get_rate_tested(self):
        return self.rate_tested

    # Mutator for num_today
    def set_num_today(self, num_today):
        self.num_today = num_today

    # Accessor for num_today  
    def get_num_today(self):
        return self.num_today

    # Mutator for percent_today
    def set_percent_today(self, percent_today):
        self.percent_today = percent_today

    # Accessor for percent_today  
    def get_percent_today(self):
        return self.percent_today

    # Mutator for rate_total
    def set_rate_total(self, rate_total):
        self.rate_total = rate_total

    # Accessor for rate_total  
    def get_rate_total(self):
        return self.rate_total

    # Mutator for rate_deaths
    def set_rate_deaths(self, rate_deaths):
        self.rate_deaths = rate_deaths

    # Accessor for rate_deaths  
    def get_rate_deaths(self):
        return self.rate_deaths

    # Mutator for num_deaths_today
    def set_num_deaths_today(self, num_deaths_today):
        self.num_deaths_today = num_deaths_today

    # Accessor for num_deaths_today  
    def get_num_deaths_today(self):
        return self.num_deaths_today

    # Mutator for percent_death
    def set_percent_death(self, percent_death):
        self.percent_death = percent_death

    # Accessor for percent_death  
    def get_percent_death(self):
        return self.percent_death

    # Mutator for num_tested_today
    def set_num_tested_today(self, num_tested_today):
        self.num_tested_today = num_tested_today

    # Accessor for num_tested_today  
    def get_num_tested_today(self):
        return self.num_tested_today

    # Mutator for num_recovered_today
    def set_num_recovered_today(self, num_recovered_today):
        self.num_recovered_today = num_recovered_today

    # Accessor for num_recovered_today  
    def get_num_recovered_today(self):
        return self.num_recovered_today

    # Mutator for percent_active
    def set_percent_active(self, percent_active):
        self.percent_active = percent_active

    # Accessor for percent_active  
    def get_percent_active(self):
        return self.percent_active

    # Mutator for num_active
    def set_num_active(self, num_active):
        self.num_active = num_active

    # Accessor for num_active 
    def get_num_active(self):
        return self.num_active

    # Mutator for rate_active
    def set_rate_active(self, rate_active):
        self.rate_active = rate_active

    # Accessor for rate_active  
    def get_rate_active(self):
        return self.rate_active

    # Mutator for num_total_last14
    def set_num_total_last14(self, num_total_last14):
        self.num_total_last14 = num_total_last14

    # Accessor for num_total_last14  
    def get_num_total_last14(self):
        return self.num_total_last14

    # Mutator for rate_total_last14
    def set_rate_total_last14(self, rate_total_last14):
        self.rate_total_last14 = rate_total_last14

    # Accessor for rate_total_last14  
    def get_rate_total_last14(self):
        return self.rate_total_last14

    # Mutator for num_deaths_last14
    def set_num_deaths_last14(self, num_deaths_last14):
        self.num_deaths_last14 = num_deaths_last14

    # Accessor for num_deaths_last14  
    def get_num_deaths_last14(self):
        return self.num_deaths_last14

    # Mutator for rate_deaths_last14
    def set_rate_deaths_last14(self, rate_deaths_last14):
        self.rate_deaths_last14 = rate_deaths_last14

    # Accessor for rate_deaths_last14  
    def get_rate_deaths_last14(self):
        return self.rate_deaths_last14

    # Mutator for num_total_last7
    def set_num_total_last7(self, num_total_last7):
        self.num_total_last7 = num_total_last7

    # Accessor for num_total_last7  
    def get_num_total_last7(self):
        return self.num_total_last7

    # Mutator for rate_total_last7
    def set_rate_total_last7(self, rate_total_last7):
        self.rate_total_last7 = rate_total_last7

    # Accessor for rate_total_last7  
    def get_rate_total_last7(self):
        return self.rate_total_last7

    # Mutator for num_deaths_last7
    def set_num_deaths_last7(self, num_deaths_last7):
        self.num_deaths_last7 = num_deaths_last7

    # Accessor for num_deaths_last7  
    def get_num_deaths_last7(self):
        return self.num_deaths_last7

    # Mutator for rate_deaths_last7
    def set_rate_deaths_last7(self, rate_deaths_last7):
        self.rate_deaths_last7 = rate_deaths_last7

    # Accessor for rate_deaths_last7   
    def get_rate_deaths_last7(self):
        return self.rate_deaths_last7

    # Mutator for avg_total_last7
    def set_avg_total_last7(self, avg_total_last7):
        self.avg_total_last7 = avg_total_last7

    # Accessor for avg_total_last7  
    def get_avg_total_last7(self):
        return self.avg_total_last7

    # Mutator for avg_incidence_last7
    def set_avg_incidence_last7(self, avg_incidence_last7):
        self.avg_incidence_last7 = avg_incidence_last7

    # Accessor for avg_incidence_last7  
    def get_avg_incidence_last7(self):
        return self.avg_incidence_last7

    # Mutator for avg_deaths_last7
    def set_avg_deaths_last7(self, avg_deaths_last7):
        self.avg_deaths_last7 = avg_deaths_last7

    # Accessor for avg_deaths_last7 
    def get_avg_deaths_last7(self):
        return self.avg_deaths_last7

    # Mutator for avg_rate_deaths_last7
    def set_avg_rate_deaths_last7(self, avg_rate_deaths_last7):
        self.avg_rate_deaths_last7 = avg_rate_deaths_last7

    # Accessor for avg_rate_deaths_last7  
    def get_avg_rate_deaths_last7(self):
        return self.avg_rate_deaths_last7


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
            
   
    def __str__(self):
        '''
        Method prints Covid object as a string
        '''
        txt = "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}\n"
        return txt.format(self.pr_uid, self.pr_name, self.pr_name_fr, self.date, self.update, self.num_conf, self.num_prob, self.num_deaths, self.num_total, self.num_tested, self.num_recover, self.percent_recover, self.rate_tested, self.num_today, self.percent_today, self.rate_total, self.rate_deaths, self.num_deaths_today, self.percent_death, self.num_tested_today, self.num_recovered_today, self.percent_active, self.num_active, self.rate_active, self.num_total_last14, self.rate_total_last14, self.num_deaths_last14, self.rate_deaths_last14, self.num_total_last7, self.rate_total_last7, self.num_deaths_last7, self.rate_deaths_last7, self.avg_total_last7, self.avg_incidence_last7, self.avg_deaths_last7, self.avg_rate_deaths_last7)
        # return self.pr_uid + " " + self.pr_name + " " + self.pr_name_fr + " " + self.date + " " + self.update + " " + self.num_conf + " " + self.num_prob + " " + self.num_deaths + " " + self.num_total + " " + self.num_tested + " " + self.num_recover + " " + self.percent_recover + " " + self.rate_tested + " " + self.num_today + " " + self.percent_today + " " + self.rate_total + " " + self.rate_deaths + " " + self.num_deaths_today + " " + self.percent_death + " " + self.num_tested_today + " " + self.num_recovered_today + " " + self.percent_active + " " + self.num_active + " " + self.rate_active + " " + self.num_total_last14 + " " + self.rate_total_last14 + " " + self.num_deaths_last14 + " " + self.rate_deaths_last14 + " " + self.num_total_last7 + " " + self.rate_total_last7 + " " + self.num_deaths_last7 + " " + self.rate_deaths_last7 + " " + self.avg_total_last7 + " " + self.avg_incidence_last7 + " " + self.avg_deaths_last7 + " " + self.avg_rate_deaths_last7
