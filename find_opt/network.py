import psutil


class NetworkInf:
    info = {}
    template =""


    def get(self):
        self.info.update(network=psutil.net_io_counters())

        self.bytes = psutil.net_io_counters()
        self.bytes_s = round(self.bytes.bytes_sent / (1024 ** 2),2)
        self.info.update(bytes_s=str(self.bytes_s))
        self.bytes_r = round(self.bytes.bytes_recv / (1024 ** 2),2)
        self.info.update(bytes_r=str(self.bytes_r))



    def prepare(self):
        self.template += "Bytes sent "
        for index in range(len(self.info["bytes_s"])):
            self.template += "{bytes_s[" + str(index) + "]}"

        self.template += "\nBytes recv "
        for index in range(len(self.info["bytes_r"])):
            self.template += "{bytes_r[" + str(index) + "]}"

        self.template += "\nPackets sent "
        for index in range(2, 3):
            self.template += "{network[" + str(index) + "]} "

        self.template += "\nPackets recv "
        for index in range(3, 4):
            self.template += "{network[" + str(index) + "]} "

        print("_" * 50)

    def show(self):
        print(self.template.format(**self.info))


if __name__ == "__main__":
    a = NetworkInf()
    a.get()
    a.prepare()
    a.show()