import psutil

class Run_pid:

    def run_pid(self):
        return ('running PID', len(psutil.pids()))

    def showrun_pid(self):
        print(f"{'running PID':<21}|{len(psutil.pids()):^6}")

if __name__ == '__main__':
    b = Run_pid()
    b.showrun_pid()
    print(b.run_pid())