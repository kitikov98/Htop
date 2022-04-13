from find_opt.cpu import Cpu
from find_opt.network import NetworkInf
from find_opt.disk import DiskInf
from find_opt.memory import MemInfo



if __name__ == '__main__':
    cpu = Cpu()
    cpu.get()
    cpu.prepare()
    cpu.show()

    net = NetworkInf()
    net.get()
    net.prepare()
    net.show()

    disk = DiskInf()
    disk.get()
    disk.prepare()
    disk.show()

    memory = MemInfo()
    memory.get()
    memory.prepare()
    memory.show()
