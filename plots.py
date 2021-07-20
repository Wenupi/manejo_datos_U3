import numpy as np
import matplotlib.pyplot as plt

# cambiar los órdenes si es necesario

secc1_volt = np.array([[0.0143, 0.0244, 0.0341],
                      [1.4587, 2.4774, 3.4492]])

secc2_volt1 = np.array([[2.11, 4.08, 5.9, 7.82, 9.66],
                       [0.0823, 0.1568, 0.89, 0.899, 0.9]])

secc2_volt2 = np.array([[2.115, 4.102, 5.954, 7.849, .834],
                       [0.89, 0.9, 0.9, 0.9, 0.9]])

secc1_current = secc1_volt[1]/(10**5)
secc2_current1 = secc2_volt1[0]/979.291
secc2_current2 = secc2_volt2[0]/979.291

plt.rcParams.update({"font.size": 9, "font.family": "serif"})
fig1, ax1 = plt.subplots(figsize=(3.5, 3.5))
ax1.plot(secc1_current, secc1_volt[0])
ax1.set_title('Curva I-V para la sección 1')
ax1.set_xlabel('Intensidad de corriente [A]')
ax1.set_ylabel('Diferencia de voltaje [V]')
ax1.grid()
fig1.tight_layout()
fig1.show()

fig2, ax2 = plt.subplots(figsize=(3.5, 3.5))
ax2.plot(secc2_current1, secc2_volt1[1])
ax2.set_title('Curva I-V para la sección 2.1')
ax2.set_xlabel('Intensidad de corriente [A]')
ax2.set_ylabel('Diferencia de voltaje [V]')
ax2.grid()
fig2.tight_layout()
fig2.show()

fig3, ax3 = plt.subplots(figsize=(3.5, 3.5))
ax3.plot(secc2_current2, secc2_volt2[1])
ax3.set_title('Curva I-V para la sección 2.2')
ax3.set_xlabel('Intensidad de corriente [A]')
ax3.set_ylabel('Diferencia de voltaje [V]')
ax3.grid()
fig3.tight_layout()
fig3.show()
