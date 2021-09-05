from hcn import *
from co import *
class Banco:
    dk = 0
    nguoichoi = 1
    dai =30
    mx =10
    my = 50
    arr = []
    tb = 0 
    def __init__(self):
        dk = 0
        nguoichoi = 1
        for i in range(0,15):
            line = []
            for j in range (0,15):
                x =self.mx + self.dai * j
                y =self.my  + self.dai * i 
                line.append(Co(x,y,x + self.dai,y + self.dai))
            self.arr.append(line)
    def thongbao (self,cas):
        if self.tb:
            cas.delete(self.tb)
        str = "người chơi: "
        if self.nguoichoi == 1:
            ten = " x "
        else:
            ten = " o "
        str = str + ten
        self.tb = cas.create_text(100,10,fill="darkblue",font="Times 20 italic bold",text=str)
      
    def vehinh (self, cas):
        self.thongbao (cas)
        for i in range(0,15):
            for j in range(0,15):
                self.arr[i][j].vehinh(cas)
        
    def bamoco(self, cas, x, y):
        for i in range(0,15):
            for j in range (0,15):
                if self.arr[i][j].tronghinh(x,y) == 1:
                    self.arr[i][j].giatri = self.nguoichoi
                    self.nguoichoi = self.nguoichoi * -1
                    self.arr[i][j].vehinh(cas)
                    self.thongbao (cas)

    def kiemtrathang(self):
        return 0
    def kiemtrathangcheophai(self):
        return 0
    def kiemtrathangcheotrai (self):
        return 0
    def kiemtrathangdoc(self):
        return 0
    def kiemtrathangngang(self):
        return 0
    