import psutil

class DiskInf:
    info = {}
    template =""

    def get(self):
        self.info.update(disk=psutil.disk_usage('/'))

    def prepare(self):
        self.template += "Disk total "
        for index in range(1):
            self.template += "{disk[" + str(index) + "]} "

        self.template += "\nDisk used "
        for index in range(1, 2):
            self.template += "{disk[" + str(index) + "]} "

        self.template += "\nDisk free "
        for index in range(2, 3):
            self.template += "{disk[" + str(index) + "]} "


    def show(self):
        print(self.template.format(**self.info))


if __name__ == "__main__":
    a = DiskInf()
    a.get()
    a.prepare()
    a.show()