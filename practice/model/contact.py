from google.appengine.ext import ndb
from google.appengine.api import memcache
from practice.system.base.model import BaseModel
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class Contact(BaseModel):
    naam = ndb.StringProperty(required=True)
    huisnummer = ndb.StringProperty(required=True)
    straat = ndb.StringProperty()
    postcode = ndb.StringProperty(required=True)
    plaats = ndb.StringProperty()

    @classmethod
    def get(cls, key):
        logging.info("Getting Contact with key: %s " % key)
        return ndb.Key("Contact", int(key)).get()
    
    def fill(self, props):
        if 'naam' in props:
            self.naam = props['naam']
        if 'huisnummer' in props:
            self.huisnummer = props['huisnummer']
        if 'straat' in props:
            self.straat = props['straat']
        if 'postcode' in props:
            self.postcode = props['postcode']
        if 'plaats' in props:
            self.plaats = props['plaats']
    
    def save(self):
        key = self.put()
        return key

    @classmethod 
    def add(cls, props):
        c = Contact()
        c.fill(props = props)
        new_c = c.save().get()
        return new_c

    def delete(self):
        self.key.delete()
        return 'Key deleted'


    
