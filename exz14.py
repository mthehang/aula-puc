import tkinter as tk


class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")
        self.root.title("Soma de Números")

        # Variável para armazenar a soma acumulada
        self.total = 0

        # Lista para armazenar os números inseridos
        self.number_list = []

        # Label para instrução
        self.label = tk.Label(root, text="Digite um número:")
        self.label.pack(pady=10)

        # Campo de entrada
        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        # Botão para adicionar
        self.add_button = tk.Button(root, text="Adicionar", command=self.add_number)
        self.add_button.pack(pady=10)

        # Botão para subtrair
        self.minus_button = tk.Button(root, text="Subtrair", command=self.minus_number)
        self.minus_button.pack(pady=10)

        # Botão para exibir o resultado
        self.result_button = tk.Button(root, text="Resultado", command=self.show_result)
        self.result_button.pack(pady=10)

        # Label para exibir a soma
        self.sum_label = tk.Label(root, text="")
        self.sum_label.pack(pady=20)

        # Label para exibir números
        self.numbers = tk.Label(root, text="Números: ")
        self.numbers.pack(pady=10)

    def add_number(self):
        try:
            # Obtendo o valor do campo de entrada e convertendo para float
            number = float(self.entry.get())
            # Adicionando ao total
            self.total += number
            # Adicionando à lista de números
            self.number_list.append(f"+{number:.2f}")
            self.show_numbers()
            # Limpando o campo de entrada
            self.entry.delete(0, tk.END)
        except ValueError:
            # Caso o usuário não insira um número válido
            self.sum_label.config(text="Por favor, insira um número válido.")

    def minus_number(self):
        try:
            # Obtendo o valor do campo de entrada e convertendo para float
            number = float(self.entry.get())
            # Subtraindo do total
            self.total -= number
            # Adicionando à lista de números
            self.number_list.append(f"-{number:.2f}")
            self.show_numbers()
            # Limpando o campo de entrada
            self.entry.delete(0, tk.END)
        except ValueError:
            # Caso o usuário não insira um número válido
            self.sum_label.config(text="Por favor, insira um número válido.")

    def show_result(self):
        self.sum_label.config(text=f"Soma total: {self.total:.2f}")

    def show_numbers(self):
        # Concatenando todos os números da lista para exibir
        numbers_text = " ".join(self.number_list)
        self.numbers.config(text=f"Números: {numbers_text}")


if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()
