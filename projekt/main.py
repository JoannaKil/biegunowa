import numpy as np
import pandas as pd
import matplotlib as plt
g = 9.81
ro = 1.225 # dla 0 m, w moim projekcie robilam dla 6 km
m_max = float(input("Podaj mase maksymalna samolotu = "))
m_min = float(input("Podaj mase minimalna samolotu = "))
m_sr = (m_min + m_max)/2
print('Masa srednia = ' + str(m_sr))
S = float(input('Podaj powierzchnie nosna = '))
Cz_max = float(input('Podaj maksymalny wspolczynnik sily nosnej = '))
V_max = float(input('Podaj predkosc maksymalna [m/s] = '))
Cz_n = "{:.4f}".format((2 * m_max * g)/(ro * S * (V_max ** 2)))
print(Cz_n)
Cx_0 = float(input('Podaj Cx0 = '))
Ae = float(input('Podaj wydluzenie efektywne = '))
b = "{:.4f}".format(1/(3.14 * Ae))
print('Biwgunowa analityczna dla samolotu: Cx = ' + str(Cx_0) + ' + ' + str(b) + ' * Cz^2')
