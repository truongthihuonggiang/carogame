from hcn import *
class Co(Hcn):
    giatri = 0
   
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2= 0, maunen = "white", duongvien = "black"):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.duongvien = duongvien
        self.maunen = maunen
        giatri = 0
    def vehinh (self, cas):
        self.hinh= super().vehinh(cas)
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1
        dx = dx /4
        dy = dy/4
        if self.giatri == 1:
           
            self.hinhgt= cas.create_line(self.x1 + dx ,self.y1 + dy ,self.x2 - dx,self.y2 - dy )
            self.hinhgt= cas.create_line(self.x2 - dx ,self.y1 + dy,self.x1 + dx,self.y2 - dy)
            print (dx)
            print (dy)
        if self.giatri == -1:
            self.hinhgt= cas.create_oval(self.x1 + dx ,self.y1 + dy ,self.x2 - dx,self.y2 - dy);
   
    def xoahinh(self,cas):
        if self.hinh:
            cas.delete(self.hinh)
            cas.delete(self.hinhgt)

  