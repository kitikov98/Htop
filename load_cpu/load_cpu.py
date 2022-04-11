import psutil

class Load_cpu:

    def load_cpu(self):
        return ('Load CPU (%)', psutil.cpu_percent(interval=1))

    def showload_cpu(self):
        print(f"{'Load CPU':<21}|{psutil.cpu_percent(interval=1):^6}%")

if __name__ == '__main__':
    a= Load_cpu()
    print(a.load_cpu())
    a.showload_cpu()