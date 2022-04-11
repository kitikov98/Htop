import psutil

class Netpack_inf:

    def netpack_inf(self):
        self.pack_s = psutil.net_io_counters()
        self.pack_s = self.pack_s.packets_sent
        self.pack_r = psutil.net_io_counters()
        self.pack_r = self.pack_r.packets_recv
        return ('Packets sent/rec', self.pack_s, self.pack_r)

    def shownetpack_inf(self):
        self.pack_s = psutil.net_io_counters()
        self.pack_s = self.pack_s.packets_sent
        self.pack_r = psutil.net_io_counters()
        self.pack_r = self.pack_r.packets_recv
        print(f"{'Packets sent/rec':<21}|{self.pack_s:^6}|{self.pack_r}")

if __name__ == '__main__':
    b = Netpack_inf()
    print(b.netpack_inf())
    b.shownetpack_inf()