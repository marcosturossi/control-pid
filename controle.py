import control as ctl
import matplotlib.pyplot as plt

"""Exemplo de utilização da Python Control System Library"""

# Modelo Matemático (Sistema Massa Mola Amortecedor)
# TF (1/ms^2 + bs + k)

m = 280  # massa
b = 30 # Conficiente de Amortecimento
k = 17  # Constante da Mola

sys = (ctl.tf([1], [m, b, k]))  # Systema em Malha Aberta

# PID Usar Ziegle Nichols para projetar o controlador
kp = 5  # Ganho Proporcional
kd = 0.5 # Ganho Derivativo
ki = 1  # Ganho Integral


def pid(kp, ki, kd):
    """Retorna a função de transferência do controlador """
    return ctl.tf([kd, kp, ki], [1,0])


sys_c = ctl.series(pid(kp, ki, kd), sys)  # Colocando o Controlador PID em serie com a planta
sys_mf = ctl.feedback(sys*pid(kp, ki, kd), 1)  # Fechando a Malha

print(pid(kp,ki,kd))
x, y = ctl.step_response(sys)
x1, y1 = ctl.step_response(sys_mf)
plt.plot(x, y)
plt.plot(x1,y1, color='red')
plt.show()

print(sys_mf)


