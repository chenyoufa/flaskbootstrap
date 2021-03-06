from flask import render_template
from app import curre_app
from utils import ServerInfo,AllDecorator


curre_app.secret_key = 'please-generate-a-random-secret_key'

 
######################后台###################################

@AllDecorator.is_login
@curre_app.route('/cms/ServerInfo/',methods=['GET'])
def GetServerInfo():
    size_cpu,used_cpu  = ServerInfo.serverinfo().get_cpu_info()
    size_memory,used_memory  = ServerInfo.serverinfo().get_memory_info()
    host_name  = ServerInfo.serverinfo().get_hostname_info()
    System_version,system_framework  = ServerInfo.serverinfo().get_system_info()
    out_ip,in_ip  = ServerInfo.serverinfo().get_ip_info()
    run_time  = ServerInfo.serverinfo().get_system_runtime()
    web_starttime,web_runtime = ServerInfo.serverinfo().get_web_runtime()
    flask_version,web_path,flask_env,python_version = ServerInfo.serverinfo().get_flask_info()
    context = {
        "size_cpu":size_cpu,
        "used_cpu":used_cpu,
        "size_memory":size_memory,
        "used_memory":used_memory,
        "host_name":host_name,
        "System_version":System_version,
        "out_ip":out_ip,
        "in_ip":in_ip,
        "run_time":run_time,
        "system_framework":system_framework,
        "web_runtime":web_runtime,
        "web_starttime":web_starttime,
        "flask_version":flask_version,
        "web_path":web_path,
        "flask_env":flask_env,
        "python_version":python_version

    }
    return render_template("cms/ServerIndex.html",**context)