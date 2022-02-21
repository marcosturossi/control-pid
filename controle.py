import control as ctl
import matplotlib.pyplot as plt

"""Exemplo de utilização da Python Control System Library"""

# Modelo Matemático (Sistema Massa Mola Amortecedor)
# TF (1/ms^2 + bs + k)

m = 100  # massa
b = 20  # Conficiente de Amortecimento
k = 17  # Constante da Mola

sys = (ctl.tf([1], [m, b, k]))  # Systema em Malha Aberta

# PID Usar Ziegle Nichols para projetar o controlador
kp = 5  # Ganho Proporcional
kd = 5  # Ganho Derivativo
ki = 10  # Ganho Integral


def pid(kp, ki, kd):
    """Retorna a função de transferência do controlador """
    return ctl.tf([kd, kp, ki], [1])


sys_c = ctl.series(pid(kp, ki, kd), sys)  # Colocando o Controlador PID em serie com a planta
sys_mf = ctl.feedback(sys_c, 1)  # Fechando a Malha

x, y = ctl.step_response(sys_mf)
plt.plot(x, y)
plt.show()


