import psutil

class DiskInf:
    info = {}
    template =""

    def get(self):
        self.disk = psutil.disk_usage('/')

        self.diskt = round(self.disk.total / (1024 ** 2), 2)
        self.info.update(diskt=str(self.diskt))

        self.disku = round(self.disk.used / (1024 ** 2), 2)
        self.info.update(disku=str(self.disku))

        self.diskf = round(self.disk.free / (1024 ** 2), 2)
        self.info.update(diskf=str(self.diskf))


    def prepare(self):
        self.template += "Disk total "
        for index in range(len(self.info["diskt"])):
            self.template += "{diskt[" + str(index) + "]}"

        self.template += "\nDisk used "
        for index in range(len(self.info["disku"])):
            self.template += "{disku[" + str(index) + "]}"

        self.template += "\nDisk free "
        for index in range(len(self.info["diskf"])):
            self.template += "{diskf[" + str(index) + "]}"
        print("_" * 50)

    def show(self):
        print(self.template.format(**self.info))


if __name__ == "__main__":
    a = DiskInf()
    a.get()
    a.prepare()
    a.show()