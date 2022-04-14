import psutil
from find_opt.parent import Parent

class MemInfo(Parent):
    info = {}
    template =""

    def get(self):
        self.virt_memt = psutil.virtual_memory()
        self.virtt_memt = round(self.virt_memt.total / (1024 ** 2), 2)
        self.info.update(virtt_mem=str(self.virtt_memt))
        self.virtu_memt = round(self.virt_memt.used / (1024 ** 2), 2)
        self.info.update(virtu_mem=str(self.virtu_memt))

        self.swp_memt = psutil.swap_memory()
        self.swpt_memt = round(self.swp_memt.total / (1024 ** 2), 2)
        self.info.update(swpt_memt=str(self.swpt_memt))

        self.swpu_memt = round(self.swp_memt.used / (1024 ** 2), 2)
        self.info.update(swpu_memt=str(self.swpu_memt))

    def prepare(self):
        self.template += "Virtual memory total "
        for index in range(len(self.info["virtt_mem"])):
            self.template += "{virtt_mem[" + str(index) + "]}"

        self.template += "\nVirtual memory used "
        for index in range(len(self.info["virtu_mem"])):
            self.template += "{virtu_mem[" + str(index) + "]}"
        #
        self.template += "\nSwap memory total "
        for index in range(len(self.info["swpt_memt"])):
            self.template += "{swpt_memt[" + str(index) + "]}"

        self.template += "\nSwap memory used "
        for index in range(len(self.info["swpu_memt"])):
            self.template += "{swpu_memt[" + str(index) + "]}"

        print("_" * 50)



if __name__ == "__main__":
    a = MemInfo()
    a.get()
    a.prepare()
    a.show()