from google.appengine.ext import db

class Paste(db.Model):
    id = db.StringProperty(required = True)
    content = db.TextProperty()
    when = db.DateTimeProperty(auto_now_add = True)
    lang = db.StringProperty(required = True ) 

