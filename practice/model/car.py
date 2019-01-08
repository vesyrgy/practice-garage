from google.appengine.ext import ndb
from google.appengine.api import memcache
from practice.system.base.model import BaseModel
from practice.model.garage import Garage
import logging

class Car(BaseModel):
    name = ndb.StringProperty()
    brand = ndb.StringProperty()
    kenteken = ndb.StringProperty(required=True)
    color = ndb.StringProperty()
    garage = ndb.KeyProperty(kind=Garage, required=True)

    @classmethod
    def get(cls,key):
        logging.info("Getting Car with key: %s" % key)
        return ndb.Key("Car", int(key)).get()

    def getGarage(self):
        garage = self.garage.get()
        logging.info("Getting Garage with id: %s " % garage.id)
        return garage

    @classmethod
    def list(cls, name=None, brand=None, limit=20):
        if not name and not brand:
            """ example with caching
            """
            cars = memcache.get("cars")
            if not cars:
                q = Car.query()
                cars = [x for x in q]
                memcache.set("cars", cars)
            if limit and len(cars) > limit:
                return cars[:limit]
            return cars

        """ example normal query with filter
        """
        q = Car.query()
        if name:
            q = q.filter(Car.name == name)
        elif brand:
            q = q.filter(Car.brand == brand)
        if limit:
            return q.fetch(limit)
        return [x for x in q]

    def fill(self, props):
        if 'name' in props:
            self.name = props['name']
        if 'brand' in props:
            self.brand = props['brand']
        if 'kenteken' in props:
            self.kenteken = props['kenteken']
        if 'color' in props:
            self.color = props['color']
        if 'garageId' in props:
            self.garage = ndb.Key('Garage', int(props['garageId']))

    def save(self):
        self.put()
        # i changed a car so cache list incorrect
        memcache.delete("cars")

    @classmethod
    def add(cls, props):
        c = Car()
        c.fill(props=props)
        c.save()
        return c.id
        # adding car changes list but handled in the save

    def delete(self):
        self.key.delete()
        # i removed a car so cache list incorrect
        memcache.delete("cars")

    def to_dict(self):
        result = super(Car, self).to_dict()
        result['garage'] = self.garage.get().id
        result['id'] = self.id
        return result