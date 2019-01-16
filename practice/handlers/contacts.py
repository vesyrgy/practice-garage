from practice.handlers import BasicHandler
from practice.model.car import Car
from practice.model.contact import Contact
import json
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class Contacts(BasicHandler):
    """ Handler for Car
        Supports up to 2 parameter:
        key = always a contact id
        carkey = always a car id
    """
    # TODO: gebruik Garages handler met "contact" als topic
    def post(self, carkey=""):
        logging.info("POST called on Contacts with carkey: %s, and params: %s", carkey, self.params.params)
        contact = Contact.add(self.params.params)
        logging.info("Created New Contact with id %s" % contact.id)
        
        if not carkey:
            logging.warning("No carkey found")
        else:
            car = Car.get(carkey)
            if not car:
                logging.warning("%s is not a valid carkey")
            else:
                # TODO: use fill instead of setContact
                car.setContact(contact.key)
                logging.info("Car with id %s now has contact set to %s", car.id, contact.id)
            
            self.render_json(json.dumps(self.to_dict(contact)))
   
            
    def get(self, key):
        logging.info("GET called on Contacts with key: %s", key)
        contact = Contact.get(key)
        self.render_json(json.dumps(self.to_dict(contact)))

    def put(self, key):
        logging.info("PUT called on Contacts with key: %s, and params: %s", key, self.params.params)
        contact = Contact.get(key)
        contact.fill(self.params.params)
        contact.save()
        self.render_json(json.dumps(self.to_dict(contact)))
        
    
    def delete(self, key):
        logging.info("DELETE called on Contacts with key: %s and params: %s", key, self.params.params)
        if not key:
            logging.warning("Cannot delete contact without key")
        if key == 'undefined':
            logging.warning("Cannot delete contact with key: %s", key)
        else:
            contact = Contact.get(key)
            for c in Car.list(None,contact):
                c.delete()
            contact.delete()
            self.render_json({"status" : "success"})


    def to_dict(self,obj):
        result = obj.to_dict()
        result['id'] = obj.id
        return result 
                
            





        
        

        