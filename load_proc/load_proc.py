import psutil

class Load_proc:

    def load_proc(self):
        self.load_pr = psutil.getloadavg()
        return ('Load average', self.load_pr[0], self.load_pr[1], self.load_pr[2])

    def showload_proc(self):
        self.load_pr=psutil.getloadavg()
        print(f"{'Load average':<21}|{self.load_pr[0]:^6}{self.load_pr[1]:^6}{self.load_pr[2]:^6}")

if __name__ == '__main__':
    b=Load_proc()
    print(b.load_proc())
    b.showload_proc()