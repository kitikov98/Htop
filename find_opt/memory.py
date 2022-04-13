import psutil

class MemInfo:
    info = {}
    template =""

    def get(self):
        self.info.update(vmem=psutil.virtual_memory())
        self.info.update(swp_mem=psutil.swap_memory())

    def prepare(self):
        self.template += "Virtual memory total "
        for index in range(1):
            self.template += "{vmem[" + str(index) + "]} "

        self.template += "\nVirtual memory used "
        for index in range(3,4):
            self.template += "{vmem[" + str(index) + "]} "

        self.template += "\nSwap memory total "
        for index in range(1):
            self.template += "{swp_mem[" + str(index) + "]} "

        self.template += "\nSwap memory used "
        for index in range(1,2):
            self.template += "{swp_mem[" + str(index) + "]} "

    def show(self):
        print(self.template.format(**self.info))


if __name__ == "__main__":
    a = MemInfo()
    a.get()
    a.prepare()
    a.show()