from pastie import app
import logging
import models
from forms import * 
from flask import render_template,redirect, url_for
from flask import flash
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name


@app.route('/')
def root():
    return redirect(url_for('new_post'))

@app.route('/posts/new', methods = ['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        id=models.genID()
        lang=getLangByNo(form.lang.data)
        paste= models.Paste(id=id,content=form.code.data,lang=lang)
        paste.put()
        logging.debug("ID : %s"%id)
        return redirect(url_for('existing_post',post_id=id))   
    return render_template('new_post.html', form=form)


@app.route('/posts/<post_id>')
def existing_post(post_id):
    query= models.Paste.all()
    paste = query.filter('id =',post_id).get()
    logging.info("ID %s"%post_id)
    if paste:
        code=htmlFor(paste.content,paste.lang) 
        return render_template('existing_post.html',title=paste.id,code=code)  
    return "Some Error has happened for post id %s"%post_id       



def htmlFor(code, lang):
    lexer = get_lexer_by_name(lang.lower(), stripall=True)
    formatter = HtmlFormatter(linenos=True, cssclass="source",style='colorful',noclasses=True)
    result = highlight(code, lexer, formatter) 
    return result
