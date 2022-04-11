from disk_inf.disk_inf import Disk_inf
from load_cpu.load_cpu import Load_cpu, Load_proc
from netmb_inf.netmb_inf import Netmb_inf, Netpack_inf
from virt_mem.virt_mem import Virt_mem, Swp_mem

class Full_inf:
    full_atr = Disk_inf()
    loadcpu_atr = Load_cpu()
    loadproc_atr=Load_proc()
    netmb_atr=Netmb_inf()
    netpack_atr=Netpack_inf()
    runpid_atr=Run_pid()
    swpmem_atr=Swp_mem()
    virtmem_atr=Virt_mem()

    def full_info(self):
        title_s={self.full_atr.disk_inf()[0]:self.full_atr.disk_inf()[1:],
                self.netpack_atr.netpack_inf()[0]:self.netpack_atr.netpack_inf()[1:],
                self.netmb_atr.netmb_inf()[0]:self.netmb_atr.netmb_inf()[1:],
                self.runpid_atr.run_pid()[0]:self.runpid_atr.run_pid()[1:],
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
                   self.runpid_atr.run_pid()[0]:self.runpid_atr.run_pid()[1:],
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
