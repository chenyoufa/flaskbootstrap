# git 使用
1）全局配置用户信息
git config --global user.name "chenyoufa"
git config --global user.email 879756530@qq.com
查看配置信息命令：
git config --list
2) 创建SSH Key
ssh-keygen -t rsa -C 879756530@qq.com

把邮件地址换成你自己的邮件地址，然后一路回车，使用默值即可；一切顺利的话，命令面板会提示.ssh目录，根据提示找到.ssh目录，里面有id_rsa和id_rsa.pub两个文件；打开id_rsa.pub，复制内容备用；
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:chenyoufa/flaskbootstrap.git
git push -u origin main

原因是没有指定本地 master 分支和远程 origin/master 的连接，这里根据提示：
git branch --set-upstream-to=origin/master master
git pull origin main
#######################

# 1.创建迁移仓库
#  python manage.py  db init

# 2.读取类的内容, 生成版本文件, 并没有真正在数据库中添加或删除;
# python manage.py db migrate -m "test"

# 3.在数据库中增删改, 也就是将迁移应用于数据库;
#  python manage.py  db upgrade 

# 4 返回指定的版本状态;降级数据库,不指定版本则是最老版本
#  python manage.py  db downgrade base 

# python manage.py database recreate
# python manage.py database init_data

#######################
***
# 项目设计方案
├─ app 网站目录文件夹
│  ├─ forms 表单验证文件夹
│  ├─ managerUtil 数据命令封装文件夹
│  │  ├─ database.py 数据命令,数据初始化，迁移，更新等
│  ├─ static 静态文件 css js images
│  ├─ templates 模板文件夹
│  │  ├─ cms  后台管理模板文件夹
│  │  ├─ main 官网模板文件夹
│  │  ├─ share 公共模板文件夹
│  ├─ views 视图文件夹
│  │  ├─ cms_view.py 后台视图文件
│  │  ├─ api_view.py webapi视图文件
│  │  ├─ main_view.py 官网视图文件
│  ├─ models.py 数据库表设计文件
├─ migrations 数据库迁移文件夹(自动生成)
├─ utils 公共函数文件夹
│  ├─ ImageCode.py 生成验证码公共函数
├─ config.py 配置文件
├─ README.md 说明文档
├─ requirements.txt pip 安装基础包文件
s
