import psutil

class Disk_inf:

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

if __name__ == '__main__':
    a = Disk_inf()
    a.showdisk_inf()
    print(a.disk_t)




