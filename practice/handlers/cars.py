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

#     def get(self, key="", topic="", ident=""):
#         if not key:
#             cars = Car.query()
#             # cars = json.dumps([p.to_dict() for p in Car.query().fetch()])
#             cars = json.dumps([ { "id": c.id, "kenteken": c.kenteken } for c in Car.query().fetch()])
#             self.render_json(cars)
#             logging.info('returning cars: %s' % cars)
#         else:
#             car = Car.get(key)
#             logging.warning("Got car " + car.kenteken)
#             self.render_json(json.dumps(car.to_dict()))
#             pass

#     def post(self, key="", topic="", ident=""):
#         logging.info('Cars.post called with params: %s ' % self.params.params)
#         if not key:
#             idnum =  Car.add(self.params.params)
#             logging.info("Car with id %s created" % idnum)
#             self.render_json(json.dumps({"id": idnum}))
#         else:
#             # edit car
#             pass

    def put(self, key="", topic=""):
        logging.info('put called with params: %s' % self.params.params)
        if key:
            c = Car.get(key)
            c.fill(self.params.params)
            c.save()
            self.render_json(json.dumps({"id": c.id}))
        else:
            logging.warning("Cannot update Car without key.")
            pass


    def delete(self, key=""):
        if key:
            logging.info('delete called with key: %s' % key)
            c = Car.get(key)
            idnum = c.id
            c.delete()
            self.render_json(json.dumps({"id": idnum}))
        else:
            logging.warning("Cannot delete Car without key.")
            pass