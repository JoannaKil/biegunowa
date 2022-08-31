import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
g = 9.81
h = 6000
ro = 1.225 * ((1 - (h / 44300)) ** 4.256)
m_max = 2717
m_min = 1779
m_sr = (m_min + m_max)/2
S = 17.1
Cz_max = 1.52
V_max = 125.5
Cz_n = (1/3)*(2 * m_max * g)/(ro * S * (V_max ** 2))
Cx_0 = 0.03
Ae = 5.974
b = 1/(3.14 * Ae)

f_max = ((2 * m_max * g)/(ro * S)) ** 0.5
f_sr = ((2 * m_sr * g)/(ro * S)) ** 0.5
f_min = ((2 * m_min * g)/(ro * S)) ** 0.5

df = pd.DataFrame({})
df['Cz'] = np.arange(Cz_n, Cz_max+0.01, 0.01)
df['Cx'] = Cx_0 + b * (df['Cz'] ** 2)
df['i'] = (1 / (((df['Cz'] ** 2) + (df['Cx'] ** 2)) ** 0.5)) ** 0.5
df['j'] = ((df['Cx'] ** 2) / (((df['Cz'] ** 2) + (df['Cx'] ** 2)) ** 1.5)) ** 0.5
df['gamma'] = np.arctan(df['Cx'] / df['Cz'])
df['V_max'] = f_max * df['i']
df['V_sr'] = f_sr * df['i']
df['V_min'] = f_min * df['i']
df['w_max'] = f_max * df['j']
df['w_sr'] = f_sr * df['j']
df['w_min'] = f_min * df['j']

Vopt_max = f_max * ((1 / ((3.14 * Ae * Cx_0) ** 0.5)) ** 0.5)
Vopt_sr = f_sr * ((1 / ((3.14 * Ae * Cx_0) ** 0.5)) ** 0.5)
Vopt_min = f_min * ((1 / ((3.14 * Ae * Cx_0) ** 0.5)) ** 0.5)
wopt_max = f_max * (((4 * (Cx_0 ** 0.5)) / ((3.14 * Ae) ** 1.5)) ** 0.5)
wopt_sr = f_sr * (((4 * (Cx_0 ** 0.5)) / ((3.14 * Ae) ** 1.5)) ** 0.5)
wopt_min = f_min * (((4 * (Cx_0 ** 0.5)) / ((3.14 * Ae) ** 1.5)) ** 0.5)



Vek_max = f_max * ((1 / ((3 * 3.14 * Ae * Cx_0) ** 0.5)) ** 0.5)
Vek_sr = f_sr * ((1 / ((3 * 3.14 * Ae * Cx_0) ** 0.5)) ** 0.5)
Vek_min = f_min * ((1 / ((3 * 3.14 * Ae * Cx_0) ** 0.5)) ** 0.5)
wek_max = f_max * (((16 * (Cx_0 ** 0.5)) / ((3 * 3.14 * Ae) ** 1.5)) ** 0.5)
wek_sr = f_sr * (((16 * (Cx_0 ** 0.5)) / ((3 * 3.14 * Ae) ** 1.5)) ** 0.5)
wek_min = f_min * (((16 * (Cx_0 ** 0.5)) / ((3 * 3.14 * Ae) ** 1.5)) ** 0.5)

gamma_opt_max = np.arcsin(wopt_max / Vopt_max)
gamma_opt_sr = np.arcsin(wopt_sr / Vopt_sr)
gamma_opt_min = np.arcsin(wopt_min / Vopt_min)
K_max = 1 / np.tan(gamma_opt_max)
K_sr = 1 / np.tan(gamma_opt_sr)
K_min = 1 / np.tan(gamma_opt_min)

K = (K_max + K_sr + K_min) / 3

print(K)

file = open("dane.csv", "w")
df.to_csv('dane.csv')
file.close()

plt.gca().invert_yaxis()

plt.plot(df['V_max'], df['w_max'], label="masa maksymalna")
plt.plot(df['V_sr'], df['w_sr'], label="masa srednia")
plt.plot(df['V_min'], df['w_min'], label="masa minimalna")
plt.xlabel("V [m/s]")
plt.ylabel("w [m/s]")
plt.legend()

plt.show()
