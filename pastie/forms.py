from flaskext import wtf
from flaskext.wtf import validators

def langTuples():
    languages = ['Java','Python','C','C++','Perl','HTML']   
    langTuples = [ (str(i) ,languages[i])for i in range(0,len(languages)) ]
    return langTuples

def getLangByNo( no):
    languages = ['Java','Python','C','C++','Perl','HTML']   
    return languages[int(no)]

class PostForm(wtf.Form):
    name = wtf.TextField('name', validators=[validators.Required()],)
    code = wtf.TextAreaField('code', validators=[validators.Required()])
    lang  = wtf.SelectField('language',choices=langTuples())


