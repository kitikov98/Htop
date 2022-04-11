from find_opt.find_opt import DiskInf, LoadCpu, LoadProc, NetmbInf, NetpackInf, VirtMem, SwpMem


class FullInf:
    full_atr = DiskInf()
    loadcpu_atr = LoadCpu()
    loadproc_atr = LoadProc()
    netmb_atr = NetmbInf()
    netpack_atr = NetpackInf()
    swpmem_atr = SwpMem()
    virtmem_atr = VirtMem()

    def full_info(self):
        title_s={self.full_atr.disk_inf()[0]:self.full_atr.disk_inf()[1:],
                self.netpack_atr.netpack_inf()[0]:self.netpack_atr.netpack_inf()[1:],
                self.netmb_atr.netmb_inf()[0]:self.netmb_atr.netmb_inf()[1:],
                self.swpmem_atr.swp_mem()[0]:self.swpmem_atr.swp_mem()[1:],
                self.virtmem_atr.virt_mem()[0]: self.virtmem_atr.virt_mem()[1:],
                self.loadproc_atr.load_proc()[0]: self.loadproc_atr.load_proc()[1:],
                self.loadcpu_atr.load_cpu()[0]: self.loadcpu_atr.load_cpu()[1:],
                }
        return title_s

    def showfull_info(self):
        title_s = {self.full_atr.disk_inf()[0]: self.full_atr.disk_inf()[1:],
                   self.netpack_atr.netpack_inf()[0]:self.netpack_atr.netpack_inf()[1:],
                   self.netmb_atr.netmb_inf()[0]: self.netmb_atr.netmb_inf()[1:],
                   self.swpmem_atr.swp_mem()[0]:self.swpmem_atr.swp_mem()[1:],
                   self.virtmem_atr.virt_mem()[0]: self.virtmem_atr.virt_mem()[1:],
                   self.loadproc_atr.load_proc()[0]: self.loadproc_atr.load_proc()[1:],
                   self.loadcpu_atr.load_cpu()[0]: self.loadcpu_atr.load_cpu()[1:],
                   }
        print(title_s)

if __name__ == '__main__':
    b = FullInf()
    print(b.full_info())
    b.showfull_info()
