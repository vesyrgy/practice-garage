from practice.handlers import BasicHandler
from practice.model.garage import Garage
from practice.model.car import Car
import json
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class Cars(BasicHandler):
    """ Handler for Car

        Supports up to 3 parameters
        key = always a contact id
        topic = what you want to do
        ident = Can be id of another class as child from Garage
    """