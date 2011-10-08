from google.appengine.ext import db
import random
import string
class Paste(db.Model):
    id = db.StringProperty(required = True)
    content = db.TextProperty()
    when = db.DateTimeProperty(auto_now_add = True)
    lang = db.StringProperty(required = True ) 


def randomID():
    return ''.join(random.choice(string.ascii_lowercase+ string.digits) for x in range(5))
    
def idExists(id):
    q = Paste.all()
    q.filter("id =",id)
    results = q.fetch(1)
    if results : 
        return True 
    else :
        return False

def genID():
    a =  randomID()
    while  idExists(a):
        a = randomID()
    return a
