from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,IntegerField
from wtforms.validators import DataRequired, Length


class MenuForm(FlaskForm):
   
    ParentId=IntegerField('上级菜单',default=0)
    MenuType=IntegerField('菜单类型')
    MenuName=StringField('菜单名称', validators=[DataRequired(), Length(1, 64), ])
    Authorize=StringField('权限标识', validators=[DataRequired(), Length(1, 64), ])
    MenuUrl=StringField('请求地址')
    MenuSort=IntegerField(default=1)
    MenuIcon=StringField('图标')
    MenuStatus=IntegerField(default=1)
    # submit = SubmitField('提交')
    

# WTFroms 支持的HTML标准字段:
# 字段类型      说　　明
# StringField 文本字段
# TextAreaField 多行文本字段
# PasswordField 密码文本字段
# HiddenField 隐藏文本字段
# DateField 文本字段，值为 datetime.date 格式
# DateTimeField 文本字段，值为 datetime.datetime 格式
# IntegerField 文本字段，值为整数
# DecimalField 文本字段，值为 decimal.Decimal
# FloatField 文本字段，值为浮点数
# BooleanField 复选框，值为 True 和 False
# RadioField 一组单选框
# SelectField 下拉列表
# SelectMultipleField 下拉列表，可选择多个值
# FileField 文件上传字段
# SubmitField 表单提交按钮