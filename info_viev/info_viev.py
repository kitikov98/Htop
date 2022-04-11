from full_inf.full_inf import Full_inf
from find_opt.find_opt import Htop_proc

class Info_viev:
    inf_atr= Full_inf()
    htopproc_atr=Htop_proc()


    def info_viev(self):

        self.info = self.inf_atr.full_info()
        for k in self.info.keys():
            i = self.info.get(k)
            print(f'{k:<30}|', end='')
            for j in i:
                print(f'{j:^10.2f}|', end='')
            print()
        print("-"*100)
        self.htopproc_atr.htop_proc()

if __name__ == '__main__':
    c= Info_viev()
    c.info_viev()