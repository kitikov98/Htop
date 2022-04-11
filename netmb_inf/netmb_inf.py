import psutil

class Netmb_inf:

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

if __name__ == '__main__':
   ffd= Netmb_inf()
   ffd.shownetmb_inf()
   print(ffd.netmb_inf())
