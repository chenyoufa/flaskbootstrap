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
@app.route('/auth/imgCode')
def imgCode():
    return getImgCode()

@app.route('/list/')
@app.route('/list/<int:page>/')
def list(page=1):
    # 每页显示的数据
    per_page = 10
    # 返回的是 Pagination对象
    userPageObj = User.query.paginate(page=page, per_page=per_page)
     
    return render_template('index.html',
                           userPageObj=userPageObj
                           )

