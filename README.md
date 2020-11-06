# flaskbootstrap
flaskbootstrap
1）全局配置用户信息
git config --global user.name "chenyoufa"
git config --global user.email 879756530@qq.com
查看配置信息命令：
git config --list
2) 创建SSH Key
ssh-keygen -t rsa -C 879756530@qq.com
把邮件地址换成你自己的邮件地址，然后一路回车，使用默值即可；一切顺利的话，命令面板会提示.ssh目录，根据提示找到.ssh目录，里面有id_rsa和id_rsa.pub两个文件；打开id_rsa.pub，复制内容备用；
