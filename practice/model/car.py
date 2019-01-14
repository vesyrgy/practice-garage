from google.appengine.ext import ndb
from google.appengine.api import memcache
from practice.system.base.model import BaseModel
from practice.model.garage import Garage
from practice.model.contact import Contact
import logging

class Car(BaseModel):
    name = ndb.StringProperty()
    brand = ndb.StringProperty()
    kenteken = ndb.StringProperty(required=True)
    color = ndb.StringProperty()
    garage = ndb.KeyProperty(kind=Garage, required=True)
    contact = ndb.KeyProperty(kind=Contact)

    @classmethod
    def get(cls,key):
        logging.info("Getting Car with key: %s" % key)
        return ndb.Key("Car", int(key)).get()

    def getGarage(self):
        garage = self.garage.get()
        logging.info("Getting Garage with id: %s " % garage.id)
        return garage

    @classmethod
    def list(cls, garage=None, contact=None, limit=20):
        if garage == None and contact == None:
            raise
        elif garage:
            q = Car.query(Car.garage == garage.key)
        elif contact:
            q = Car.query(Car.contact == contact.key)

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
        key = self.put()
        # i changed a car so cache list incorrect
        return key

    @classmethod
    def add(cls, props):
        c = Car()
        c.fill(props=props)
        new_c = c.save().get()
        return new_c
        # adding car changes list but handled in the save

    def delete(self):
        self.key.delete()
        # i removed a car so cache list incorrect
        memcache.delete("cars")