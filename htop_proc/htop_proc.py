import psutil

class Htop_proc:

    def htop_proc(self):
        print(f"{'pid':16}{'username':^16}{'memory_percent':^16}{'cpu_percent':^16}{'cmdline'}")
        for self.proc in psutil.process_iter(['pid', 'cmdline', 'username', 'memory_percent', 'cpu_percent']):
            if self.proc.info['cmdline'] == []:
                continue
            else:
                print(
                    f"{self.proc.info['pid']:<16}{self.proc.info['username']:^16}{self.proc.info['memory_percent']:^16.2f}{self.proc.info['cpu_percent']:^16.2f}{self.proc.info['cmdline']}")

if __name__ == '__main__':
    b = Htop_proc()
    b.htop_proc()