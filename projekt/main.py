# ten kod to nie jest jakis super, na razie jest tak zebym to ja rozumiala co sie tu dzieje
import numpy as np
import pandas as pd
import matplotlib as plt
g = 9.81
h = float(input('Podaj wysokosc [m] = '))
ro = 1.225 * ((1 - (h / 44300)) ** 4.256)
print('Gestosc na tej wysokosci wynosi = ' + str("{:.3f}".format(ro)) + ' [kg/m^3]')
m_max = float(input("Podaj mase maksymalna samolotu = "))
m_min = float(input("Podaj mase minimalna samolotu = "))
m_sr = (m_min + m_max)/2
print('Masa srednia = ' + str(m_sr) + ' [kg]')
S = float(input('Podaj powierzchnie nosna = '))
Cz_max = float(input('Podaj maksymalny wspolczynnik sily nosnej = '))
V_max = float(input('Podaj predkosc maksymalna [m/s] = '))
Cz_n = (2 * m_max * g)/(ro * S * (V_max ** 2))
print('Cz_n = ' + str("{:.4f}".format(Cz_n)))
Cx_0 = float(input('Podaj Cx0 = '))
Ae = float(input('Podaj wydluzenie efektywne = '))
b = 1/(3.14 * Ae)
print('Biegunowa analityczna dla samolotu: Cx = ' + str(Cx_0) + ' + ' + str("{:.4f}".format(b)) + ' * Cz^2')
z = list(np.arange(Cz_n, Cz_max, 0.01))
z.append(Cz_max)
x = []
Cx = 0
Vx = []
V_x = 0
Vn = []
V_n = 0
Vs = []
V_s = 0
wx = []
w_x = 0
wn = []
w_n = 0
ws = []
w_s = 0
gam = []
gamma = 0

for i in z:
    Cx = Cx_0 + b * (i ** 2)
    x.append(Cx)
    gamma = np.arctan(Cx / i)
    gam.append(gamma)
    V_x = ((2 * m_max * g)/((ro * S) * (((i ** 2) + (Cx ** 2)) ** 0.5))) ** 0.5
    Vx.append(V_x)
    V_n = ((2 * m_min * g) / ((ro * S) * (((i ** 2) + (Cx ** 2)) ** 0.5))) ** 0.5
    Vn.append(V_n)
    V_s = ((2 * m_sr * g) / ((ro * S) * (((i ** 2) + (Cx ** 2)) ** 0.5))) ** 0.5
    Vs.append(V_s)
    w_x = ((2 * m_max * g * (Cx ** 2))/(ro * S * (((i ** 2) + (Cx ** 2)) ** 1.5))) ** 0.5
    wx.append(w_x)
    w_n = ((2 * m_min * g * (Cx ** 2)) / (ro * S * (((i ** 2) + (Cx ** 2)) ** 1.5))) ** 0.5
    wn.append(w_n)
    w_s = ((2 * m_sr * g * (Cx ** 2)) / (ro * S * (((i ** 2) + (Cx ** 2)) ** 1.5))) ** 0.5
    ws.append(w_s)
print(Vs)
