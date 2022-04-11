import psutil

class Load_cpu:

    def load_cpu(self):
        return ('Load CPU (%)', psutil.cpu_percent(interval=1))

    def showload_cpu(self):
        print(f"{'Load CPU':<21}|{psutil.cpu_percent(interval=1):^6}%")

class Load_proc:

    def load_proc(self):
        self.load_pr = psutil.getloadavg()
        return ('Load average', self.load_pr[0], self.load_pr[1], self.load_pr[2])

    def showload_proc(self):
        self.load_pr=psutil.getloadavg()
        print(f"{'Load average':<21}|{self.load_pr[0]:^6}{self.load_pr[1]:^6}{self.load_pr[2]:^6}")

if __name__ == '__main__':
    a= Load_cpu()
    print(a.load_cpu())
    a.showload_cpu()