from testcases import BasicTestCase
from src.models.garage import Garage
import logging


""" Very simple example how to use the BasicTestCase
"""
class GarageTestCase(BasicTestCase):
    
    def setUP(self):
        ''' This method can be used to import or set up some data needed for every testcase
            
            no need to call super
        '''
        pass
    
    def test_datastore(self):
        ''' start with test_ to get function started
        '''
        g = Garage()
        g.name = "test2222"
        g.brande = "Volvo"
        g.note = """ Testing note
        for multi line
        hueaah"""
        
        g.put()

        for g2 in Garage.query():
            print g2.name
            logging.warning(g2.note)
        self.assertEqual(1, Garage.query().count()) # yay success
        
    def tearDown(self):
        """ tearDown will be called after a testcase
        """
        pass