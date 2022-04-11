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

if __name__ == '__main__':
    b = Virt_mem()
    print(b.virt_mem())
    b.showvirt_mem()