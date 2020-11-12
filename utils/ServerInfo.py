import psutil,socket,re,requests,platform
class serverinfo():
    def get_cpu_info(self):
        size_cpu = psutil.cpu_count()
        used_cpu = psutil.cpu_percent(interval=1)

    def get_memory_info(self):
        v_virtual_memory = psutil.virtual_memory()
        size_memory = v_virtual_memory.total/1024/1024
        used_memory = v_virtual_memory.used/1024/1024

    def get_hostname_info(self):
        host_name = socket.gethostname()

    def get_ip_info(self):
        html_text = requests.get("https://ip.cn/").text
        ip_text = re.search(u"<p>您现在的 IP：<code>(.*?)</code></p>", html_text)
        out_ip = ip_text.group(1)
        in_ip = socket.gethostbyname(socket.gethostname())

    def get_system_info(self):
        System_version = platform.platform()


