import psutil
class serverinfo():
    def get_cpu_info(self):
        size_cpu = psutil.cpu_count()
        used_cpu = psutil.cpu_percent(interval=1)

    def get_memory_info(self):
        v_virtual_memory = psutil.virtual_memory()
        size_memory = v_virtual_memory.total/1024/1024
        used_memory = v_virtual_memory.used/1024/1024
