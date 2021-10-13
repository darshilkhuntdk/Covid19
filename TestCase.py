import unittest
from Business.Covid19Service import Covid19Service


class TestCase(unittest.TestCase):
    """
    Performs Unit Test for the load file data into the Covid19Record object
    Author: Darshilkumar Khunt
    """

   # Returns True or False.
    def test_delete_record(self):
        """"
        Checks if record deleted from the database or not
        """
        # make service object
        service = Covid19Service()
        
        # load data from file
        service.get_one_record(1)

        # delete a record with id = 1 from database
        service.delete_record(1)

        # fetch deleted record from the database
        result = service.get_one_record(1)

        # find length of result list
        length = len(result)

        # check fro length is 0 or not
        self.assertEqual(length,0)


if __name__=='__main__':
    unittest.main()
