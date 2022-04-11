from find_opt.find_opt import Disk_inf, Load_cpu, Load_proc, Netmb_inf, Netpack_inf, Virt_mem, Swp_mem


class Full_inf:
    full_atr = Disk_inf()
    loadcpu_atr = Load_cpu()
    loadproc_atr = Load_proc()
    netmb_atr = Netmb_inf()
    netpack_atr = Netpack_inf()
    swpmem_atr = Swp_mem()
    virtmem_atr = Virt_mem()

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
    b = Full_inf()
    print(b.full_info())
    b.showfull_info()
