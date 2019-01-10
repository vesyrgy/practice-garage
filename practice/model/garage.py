from google.appengine.ext import ndb
from google.appengine.api import memcache
from practice.system.base.model import BaseModel
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class Garage(BaseModel):
    name = ndb.StringProperty(required=True)
    brand = ndb.StringProperty()

    postal_country = ndb.StringProperty()
    
    # def cars(self):
    #     from practice.model.car import Car
    #     gkey = ndb.Key("Garage", int(self.id))
    #     q = Car.query(Car.garage == gkey).fetch()
    #     cars = [c for c in q]
    #     # logging.info("cars: %s " % cars)
    #     return cars
        

    #note = ndb.TextProperty(indexed=False)

    @classmethod
    def get(cls,key):
        logging.info("Getting Garage with key: %s" % key)
        return ndb.Key("Garage", int(key)).get()

    @classmethod
    def list(cls, name=None, brand=None, limit=20):
        if not name and not brand:
            """ example with caching
            """
            garages = memcache.get("garages")
            if not garages:
                q = Garage.query()
                garages = [x for x in q]
                memcache.set("garages", garages)
            if limit and len(garages) > limit:
                return garages[:limit]
            return garages

        """ example normal query with filter
        """
        q = Garage.query()
        if name:
            q = q.filter(Garage.name == name)
        elif brand:
            q = q.filter(Garage.brand == brand)
        if limit:
            return q.fetch(limit)
        return [x for x in q]

    def fill(self, props):
        if 'name' in props:
            self.name = props['name']
        if 'brand' in props:
            self.brand = props['brand']
        if 'postal_country' in props:
            self.postal_country = props['postal_country']

    def save(self):
        key = self.put()
        # i changed a garage so cache list incorrect
        memcache.delete("garages")
        return key

    @classmethod
    def add(cls, props):
        g = Garage()
        g.fill(props=props)
        new_g = g.save().get()
        logging.info("idnum: %s " % str(new_g.id))
        return new_g
        
        # adding garage changes list but handled in the save

    def delete(self):
        self.key.delete()
        # i removed a garages so cache list incorrect
        memcache.delete("garages")

    def to_dict(self):
        result = super(Garage, self).to_dict()
        result['id'] = self.id
        return result
        