from practice.handlers import BasicHandler
from practice.model.car import Car
from practice.model.contact import Contact
import json
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class Contacts(BasicHandler):
    """ Handler for Car
        Supports up to 2 parameters
        key = always a contact id
        carkey = always a car id
    """
    def post(self, key="", carkey=""):
        logging.info("POST called on Contacts with key: %s, carkey: %s, and params: %s", key, carkey, self.params.params)
        if not key:
            contact = Contact.add(self.params.params)
            logging.info("Created New Contact with id %s" % contact.id)
            try:
                car = Car.get(carkey)
                # TODO: use fill instead of setContact
                car.setContact(contact.key)
                logging.info("Car with id %s now has contact set to %s", car.id, contact.id)
            except:
                logging.warning("No carkey was recognized")
            self.render_json(json.dumps(self.to_dict(contact)))
        else: 
            try:
                contact = Contact.get(key)
                logging.warning("Contact with key %s already exists" % key)
            except:
                logging.warning("'%s' is not a valid Contact Key." % key) 
            
            

    def get(self, key=""):
        if not key:
            logging.warning("Cannot get Contact without key")
            raise
        else:
            if not Contact.get(key):
                car = Car.get(key)
                if not car:
                    logging.warning("The key provided does not match a Car or a Contact")
                    raise
                else: 
                    contact = car.get(key).contact.get()
                    self.render_json(json.dumps(self.to_dict(contact)))
            else: 
                contact = Contact.get(key)
                self.render_json(json.dumps(self.to_dict(contact)))
                
            

    def to_dict(self,obj):
        result = obj.to_dict()
        result['id'] = obj.id
        return result 
                
            





        
        

        