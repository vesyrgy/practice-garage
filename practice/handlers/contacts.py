from practice.handlers import BasicHandler
from practice.model.car import Car
from practice.model.contact import Contact
import json
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class Contacts(BasicHandler):
    """ Handler for Car

        Supports up to 3 parameters
        key = always a contact id
        topic = what you want to do
        ident = Can be id of another class as child from Garage
    """
    def put(self, key=""):
        

        