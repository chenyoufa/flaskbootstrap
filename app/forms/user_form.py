from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,IntegerField
from wtforms.validators import DataRequired, Length


class UserForm(FlaskForm):
    Id=IntegerField()
    UserName=StringField('登录名称', validators=[DataRequired(), Length(1, 30), ])
    PassWord=StringField('登录密码', validators=[DataRequired(), Length(1, 150), ])
    RealName=StringField('真实姓名', validators=[DataRequired(), Length(1, 20), ])
    Gender=IntegerField("性别",default=2)
    Email=StringField('邮箱')
    Mobile=StringField('电话')
    DepartmentId=IntegerField("部门",validators=[DataRequired(), ])
    PositionId=StringField('岗位名称', validators=[DataRequired(), Length(1, 10), ])
    RoleId = IntegerField("角色")
    Status = IntegerField("状态",default=1)
    Remark=StringField('备注')
    

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