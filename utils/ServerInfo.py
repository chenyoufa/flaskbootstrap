import psutil,socket,platform,datetime
from urllib.request import urlopen
class serverinfo():
    def get_cpu_info(self):
        #获取cpu核数
        size_cpu = psutil.cpu_count()
        #获取CPU的使用情况
        used_cpu = psutil.cpu_percent(interval=1)
        return size_cpu,used_cpu

    def get_memory_info(self):
        #获取内存情况
        v_virtual_memory = psutil.virtual_memory()
        #获取内存大小，单位为G
        size_memory = "%.2f" %(v_virtual_memory.total/1024/1024/1024)
        #获取内存使用百分比
        used_memory = "%.2f" %((v_virtual_memory.used/v_virtual_memory.total)*100)
        return size_memory,used_memory

    def get_hostname_info(self):
        #获取主机名
        host_name = socket.gethostname()
        return host_name

    def get_ip_info(self):
        #获取外网ip
        out_ip = urlopen('http://ip.42.pl/raw').read().decode()
        #获取内网ip
        in_ip = socket.gethostbyname(socket.gethostname())
        return out_ip,in_ip

    def get_system_info(self):
        #获取系统平台
        System_version = platform.platform()
        #获取系统架构
        system_framework = platform.architecture()[0]
        return System_version,system_framework

    def get_system_runtime(self):
        #获取当前时间
        now_time = datetime.datetime.now()
        #获取开机时间戳
        boot_time = psutil.boot_time()
        #获取开机时间
        boot_time_obj = datetime.datetime.fromtimestamp(boot_time)
        #获取系统运行时间
        run_time = str(now_time - boot_time_obj).split('.')[0]
        return run_time



