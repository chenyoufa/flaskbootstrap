from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,IntegerField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    # username = StringField('用户名', validators=[DataRequired(), Length(1, 64), ])
    # password = PasswordField('密码', validators=[DataRequired()])
    # rememberme = BooleanField('记住我')
    username=StringField('用户名', validators=[DataRequired("请输入用户名"), Length(1,8) ])
    password=StringField('密码', validators=[DataRequired("请输入密码"), Length(1,8) ])
    captchaCode=StringField('验证码', validators=[DataRequired("请输入验证码"), Length(1, 8), ])
    csrf_token=StringField('csrf')
   
    