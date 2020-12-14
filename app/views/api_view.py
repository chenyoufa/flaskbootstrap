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

############################# api #################################
def getImgCode():
    
    image, code = ImageCodeHelper.imageCode().getVerifyCode()
    # 图片以二进制形式写入
    buf = BytesIO()
    image.save(buf, 'jpeg')
    buf_str = buf.getvalue()
    # 把buf_str作为response返回前端，并设置首部字段
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/gif'
    # 将验证码字符串储存在session中
    session['imageCode'] = code
    return response
#验证码
from flask import   request 
@curre_app.route('/auth/imgCode')
def imgCode():
 
    return getImgCode()


