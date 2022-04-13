import psutil

class Cpu:
    info = {}
    template =""

    def get(self):
        self.info.update(load=psutil.getloadavg())
        self.info.update(count=str(psutil.cpu_count()))
        self.info.update(freq=[freg.current for freg in psutil.cpu_freq(percpu=True)])
        self.info.update(percent=psutil.cpu_percent(interval=1, percpu=True))

    def prepare(self):
        self.template += "Load "
        for index in range(len(self.info["load"])):
            self.template += "{load[" + str(index) + "]} "

        self.template += "\nCount "
        for index in range(len(self.info["count"])):
            self.template += "{count[" + str(index) + "]}\n"

        self.template += "Freq "
        for index in range(len(self.info["freq"])):
            self.template += "{freq[" + str(index) + "]} "

        self.template += "\nPersent "
        for index in range(len(self.info["percent"])):
            self.template += "{percent[" + str(index) + "]} "

        print("_" * 50)

    def show(self):
        print(self.template.format(**self.info))


if __name__ == "__main__":
    a = Cpu()
    a.get()
    a.prepare()
    a.show()