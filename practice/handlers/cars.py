from practice.handlers import BasicHandler
from practice.model.car import Car
import json
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class Cars(BasicHandler):
    """ Handler for Car

        Supports up to 3 parameters
        key = always a car id
        topic = what you want to do
        ident = Can be id of another class as child from Car
    """

    def put(self, key="", topic=""):
        logging.info('put called with params: %s' % self.params.params)
        if not key:
            logging.warning("PUT request cannot be completed without key.")
        else:
            c = Car.get(key)
            c.fill(self.params.params)
            c.save()
            self.render_json(json.dumps({"id": c.id}))

    def delete(self, key=""):
        if not key:
            logging.warning("Cannot delete Car without key.")
        else:
            logging.info('delete called with key: %s' % key)
            c = Car.get(key)
            idnum = c.id
            c.delete()
            self.render_json(json.dumps({"id": idnum}))

            pass