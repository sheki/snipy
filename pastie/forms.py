from flaskext import wtf
from flaskext.wtf import validators

class PostForm(wtf.Form):
    title = wtf.TextField('Snippet Name', validators=[validators.Required()],)
    content = wtf.TextAreaField('code', validators=[validators.Required()])
