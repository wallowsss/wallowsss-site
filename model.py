from google.appengine.ext import db

class Profile(db.Model):
    name = db.StringProperty(required=True)
    title = db.StringProperty()
    subtitle = db.StringProperty(multiline=True)
    description = db.StringProperty(multiline=True)
    
class Services(db.Model):
    service  = db.StringProperty(required=True)
    tumbnail = db.StringProperty()
    link     = db.StringProperty()


