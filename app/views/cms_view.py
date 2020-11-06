# http://www.csdn.net/list/
# http://www.csdn.net/list/1/
# http://www.csdn.net/list/2/
from flask import render_template
from app import app
from app.models import User
import utils.ImageCode as ImageCodeHelper 
from flask import make_response,session
from io import BytesIO
from datetime import datetime
app.secret_key = 'please-generate-a-random-secret_key'

 
######################后台###################################

@app.route('/cms/login')
def login():
    """Renders the about page."""
    return render_template(
        'cms/login.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/cms/index')
def index():
    """Renders the about page."""
    return render_template(
        'cms/index.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
