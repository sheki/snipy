from flaskext import wtf
from flaskext.wtf import validators

class PostForm(wtf.Form):
    languages = ['Java','Python','C','C++','Perl','HTML']
    langTuples = [ (str(i),languages[i])for i in range(0,len(languages)) ]
    name = wtf.TextField('name', validators=[validators.Required()],)
    code = wtf.TextAreaField('code', validators=[validators.Required()])
    lang  = wtf.SelectField('language',choices=langTuples)

