import psutil

class DiskInf:

    def disk_inf(self):
        self.disk_u = psutil.disk_usage('/')
        self.disk_u = round(self.disk_u.used / (1024 ** 2), 2)
        self.disk_t = psutil.disk_usage('/')
        self.disk_t = round(self.disk_t.total / (1024 ** 2), 2)
        self.disk_f = psutil.disk_usage('/')
        self.disk_f = round(self.disk_f.free / (1024 ** 2), 2)
        return ('Disk total/used/free (MB)', self.disk_t, self.disk_u, self.disk_f)

    def showdisk_inf(self):
        self.disk_u = psutil.disk_usage('/')
        self.disk_u = round(self.disk_u.used / (1024 ** 2), 2)
        self.disk_t = psutil.disk_usage('/')
        self.disk_t = round(self.disk_t.total / (1024 ** 2), 2)
        self.disk_f = psutil.disk_usage('/')
        self.disk_f = round(self.disk_f.free / (1024 ** 2), 2)
        print(f"{'Disk total/used/free':<21}|{self.disk_t:^10.2f}/{self.disk_u:^10.2f}/{self.disk_f:^8.2f} MB")

class LoadCpu:

    def load_cpu(self):
        return ('Load CPU (%)', psutil.cpu_percent(interval=1))

    def showload_cpu(self):
        print(f"{'Load CPU':<21}|{psutil.cpu_percent(interval=1):^6}%")

class LoadProc:

    def load_proc(self):
        self.load_pr = psutil.getloadavg()
        return ('Load average', self.load_pr[0], self.load_pr[1], self.load_pr[2])

    def showload_proc(self):
        self.load_pr=psutil.getloadavg()
        print(f"{'Load average':<21}|{self.load_pr[0]:^6}{self.load_pr[1]:^6}{self.load_pr[2]:^6}")

class VirtMem:

    def virt_mem(self):
        self.virt_memt = psutil.virtual_memory()
        self.virt_memt = round(self.virt_memt.total / (1024 ** 2), 2)
        self.virt_memu = psutil.virtual_memory()
        self.virt_memu = round(self.virt_memu.used / (1024 ** 2), 2)
        return ('Memory (MB)', self.virt_memu, self.virt_memt)

    def showvirt_mem(self):
        self.virt_memt = psutil.virtual_memory()
        self.virt_memt = round(self.virt_memt.total / (1024 ** 2), 2)
        self.virt_memu = psutil.virtual_memory()
        self.virt_memu = round(self.virt_memu.used / (1024 ** 2), 2)
        print(f"{'Memory':<21}|{self.virt_memu:^9.2f}/{self.virt_memt:^9.2f} MB")

class SwpMem:

    def swp_mem(self):
        self.sw_memt = psutil.swap_memory()
        self.sw_memt = round(self.sw_memt.total / (1024 ** 2), 2)
        self.sw_memu = psutil.swap_memory()
        self.sw_memu = round(self.sw_memu.used / (1024 ** 2), 2)
        return ('SWP Memory (MB)', self.sw_memu, self.sw_memt)

    def showswp_mem(self):
        self.sw_memt = psutil.swap_memory()
        self.sw_memt = round(self.sw_memt.total / (1024 ** 2), 2)
        self.sw_memu = psutil.swap_memory()
        self.sw_memu = round(self.sw_memu.used / (1024 ** 2), 2)
        print(f"{'SWP Memory':<21}|{self.sw_memu:^6.2f} / {self.sw_memt:.2f} MB")

class NetmbInf:

    def netmb_inf(self):
        self.bytes_s = psutil.net_io_counters()
        self.bytes_s = self.bytes_s.bytes_sent / (1024 ** 2)
        self.bytes_r = psutil.net_io_counters()
        self.bytes_r = self.bytes_r.bytes_recv / (1024 ** 2)
        return ('MB sent/rec (MB)', self.bytes_s, self.bytes_r)

    def shownetmb_inf(self):
        self.bytes_s = psutil.net_io_counters()
        self.bytes_s = self.bytes_s.bytes_sent / (1024 ** 2)
        self.bytes_r = psutil.net_io_counters()
        self.bytes_r = self.bytes_r.bytes_recv / (1024 ** 2)
        print(f"{'MB sent/rec':<21}|{self.bytes_s:^6.2f}/{self.bytes_r:.2f} MB")

class NetpackInf:

    def netpack_inf(self):
        self.pack_s = psutil.net_io_counters()
        self.pack_s = self.pack_s.packets_sent
        self.pack_r = psutil.net_io_counters()
        self.pack_r = self.pack_r.packets_recv
        return ('Packets sent/rec', self.pack_s, self.pack_r)

class HtopProc:

    def htop_proc(self):
        print(f"{'pid':16}{'username':^16}{'memory_percent':^16}{'cpu_percent':^16}{'cmdline'}")
        for self.proc in psutil.process_iter(['pid', 'cmdline', 'username', 'memory_percent', 'cpu_percent']):
            if self.proc.info['cmdline'] == []:
                continue
            else:
                print(
                    f"{self.proc.info['pid']:<16}{self.proc.info['username']:^16}{self.proc.info['memory_percent']:^16.2f}{self.proc.info['cpu_percent']:^16.2f}{self.proc.info['cmdline']}")

