import psutil

class Swp_mem:

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

if __name__ == '__main__':
    b = Swp_mem()
    b.showswp_mem()
    print(b.swp_mem())