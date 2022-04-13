import psutil

class NetworkInf:
    info = {}
    template =""

    def get(self):
        self.info.update(network=psutil.net_io_counters())


    def prepare(self):
        self.template += "Bytes sent "
        for index in range(1):
            self.template += "{network[" + str(index) + "]} "

        self.template += "\nBytes recv "
        for index in range(1,2):
            self.template += "{network[" + str(index) + "]} "

        self.template += "\nPackets sent "
        for index in range(2, 3):
            self.template += "{network[" + str(index) + "]} "

        self.template += "\nPackets recv "
        for index in range(3, 4):
            self.template += "{network[" + str(index) + "]} "


    def show(self):
        print(self.template.format(**self.info))


if __name__ == "__main__":
    a = NetworkInf()
    a.get()
    a.prepare()
    a.show()
    print(a.info)