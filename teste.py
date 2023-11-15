import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, ln, lambdify

# Define a variável simbólica e a função h(x)
x = symbols('x')
h_x = 70.228 + 5.104*x + 9.222*ln(x)

# Calcula a derivada de h(x)
h_prime_x = diff(h_x, x)

# Converte a função simbólica e sua derivada para funções numéricas
h_x_func = lambdify(x, h_x, modules=['numpy'])
h_prime_x_func = lambdify(x, h_prime_x, modules=['numpy'])

# Define o intervalo para x de acordo com o domínio dado: 1/4 <= x <= 6
x_vals = np.linspace(1/4, 6, 400)
h_vals = h_x_func(x_vals)
h_prime_vals = h_prime_x_func(x_vals)

# Plota o gráfico de h(x)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x_vals, h_vals, label='h(x)')
plt.title('Gráfico da função h(x)')
plt.xlabel('Idade (anos)')
plt.ylabel('Altura (cm)')
plt.legend()

# Plota o gráfico da derivada de h(x)
plt.subplot(1, 2, 2)
plt.plot(x_vals, h_prime_vals, label="h'(x)", color='orange')
plt.title("Gráfico da derivada de h(x)")
plt.xlabel('Idade (anos)')
plt.ylabel('Taxa de crescimento (cm/ano)')
plt.legend()

# Mostra os gráficos
plt.tight_layout()
plt.show()
