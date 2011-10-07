from pastie import app
from models import Paste 
from forms import PostForm
from flask import render_template
from flask import flash
@app.route('/random')
def random():
    return render_template('test.html',name="RANGO") 

@app.route('/rango')
def random():
    return render_template('test.html',name="GO RANGO") 

@app.route('/posts/new', methods = ['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        #post = Post(title = form.title.data,
        #            content = form.content.data,
        #            author = users.get_current_user())
        #post.put()
        flash('Post saved on database.')
        return "DONE"
    return render_template('new_post.html', form=form)
