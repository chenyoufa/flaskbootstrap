# http://www.csdn.net/list/
# http://www.csdn.net/list/1/
# http://www.csdn.net/list/2/
from flask import render_template
from app import curre_app
from app.models import User
import utils.ImageCode as ImageCodeHelper 
from flask import make_response,session
from io import BytesIO
from datetime import datetime
curre_app.secret_key = 'please-generate-a-random-secret_key'

#####################网站页面################################
@curre_app.route('/')
@curre_app.route('/main/home')
def home():
    """Renders the home page."""
    return render_template(
        'main/index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@curre_app.route('/main/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'main/contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@curre_app.route('/main/about')
def about():
    """Renders the about page."""
    return render_template(
        'main/about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
 