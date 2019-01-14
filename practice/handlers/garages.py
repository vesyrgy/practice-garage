from practice.handlers import BasicHandler
from practice.model.garage import Garage
from practice.model.car import Car
import json
import logging
import re

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class Garages(BasicHandler):
    """ Handler for Garage

        Supports up to 3 parameters
        key = always a garage id
        topic = what you want to do
        ident = Can be id of another class as child from Garage
    """

    def get(self, key="", topic="", ident=""):
        logging.warning("Garages.get() called with key: %s, topic: %s, and ident: %s", key, topic, ident)
        if not key:
            garages = Garage.query()
            garages = json.dumps([p.to_dict() for p in Garage.query().fetch()])
            self.render_json(garages)
            # logging.info('returning garages: %s' % garages)
        else:
            garage = Garage.get(key)
            logging.info("Got garage: %s " % garage.name)
            if not topic:
                self.render_json(json.dumps(garage.to_dict()))
            elif topic == 'cars': 
                logging.info('Getting the is of cars...')
                autos = json.dumps([c.to_dict() for c in Car.list(garage) ])
                logging.info(autos)
                self.render_json(autos)
            elif topic == 'car':
                if ident:
                    car = Car.get(ident)
                    logging.info('Got car with id: %s' % car.id)
                    self.render_json(json.dumps(car.to_dict()))
                pass

    def post(self, key="", topic="", ident=""):
        logging.info('Garages.post called with params: %s' % self.params.params)
        if not key:
            garage = Garage.add(self.params.params)
            logging.info("Garage with id %s created" % garage.id)
            self.render_json(json.dumps(garage.to_dict()))
        else:
            if not topic:
                logging.warning("No topic specified for Garage with key: %s" % key)
            elif topic == 'cars':
                logging.info("Garage key is: %s " % key)
                car = Car.add(self.params.params)
                logging.info("Car with id %s created" % car.id)
                self.render_json(json.dumps(car.to_dict()))
            else:
                logging.warning("Cannot complete post request for topic: %s" % topic)
                pass

    def put(self, key="", topic="", ident=""):
        logging.info('put called with params: %s' % self.params.params)
        if not key:
            logging.warning("Cannot update Garage without key.")
        else:
            if not topic:
                g = Garage.get(key)
                g.fill(self.params.params)
                g.save()
                self.render_json(json.dumps({"id": g.id}))
            elif topic == 'car':
                c = Car.get(ident)
                c.fill(self.params.params)
                c.save()
                self.render_json(json.dumps({"id": c.id}))
            pass


    def delete(self, key="", topic="", ident=""):
        if not topic:
            if key:
                logging.info('delete called with key: %s' % key)
                g = Garage.get(key)
                idnum = g.id
                g.delete()
                self.render_json(json.dumps({"id": idnum}))
        elif topic == 'car':
            if ident:
                c = Car.get(ident)
                idnum = c.id
                c.delete()
                self.render_json(json.dumps({"id": idnum}))
        else:
            logging.warning("Cannot delete Garage without key.")
            pass


