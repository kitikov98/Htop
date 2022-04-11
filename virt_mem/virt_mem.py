import psutil

class Virt_mem:

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
    b = Virt_mem()
    print(b.virt_mem())
    b.showvirt_mem()