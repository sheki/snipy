from flask import Flask
import settings

app = Flask('pastie')
app.config.from_object('pastie.settings')

import views
