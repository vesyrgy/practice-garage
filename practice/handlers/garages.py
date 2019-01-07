from practice.handlers import BasicHandler
from practice.model.garage import Garage
import json
import logging

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
        if not key:
            garages = Garage.query()
            # garages = json.dumps([p.to_dict() for p in Garage.query().fetch()])
            garages = json.dumps([ { "id": p.id, "name": p.name } for p in Garage.query().fetch()])
            self.render_json(garages)
            logging.info('returning garages: %s' % garages)
        else:
            garage = Garage.get(key)
            logging.warning("Got garage " + garage.name)
            self.render_json(json.dumps(garage.to_dict()))
            pass

    def post(self, key="", topic="", ident=""):
        if not key:
            idnum =  Garage.add(self.params.params)
            logging.info("Garage with id %s created" % idnum)
            self.render_json(json.dumps({"id": idnum}))
        else:
            # edit garage
            pass

    def put(self, key="", topic=""):
        logging.info('put called with params: %s' % self.params.params)
        if key:
            g = Garage.get(key)
            g.fill(self.params.params)
            g.save()
            self.render_json(json.dumps({"id": g.id}))
        else:
            logging.warning("Cannot update Garage without key.")
            pass


    def delete(self, key=""):
        if key:
            logging.info('delete called with key: %s' % key)
            g = Garage.get(key)
            idnum = g.id
            g.delete()
            self.render_json(json.dumps({"id": idnum}))
        else:
            logging.warning("Cannot delete Garage without key.")
            pass


