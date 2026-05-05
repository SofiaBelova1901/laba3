import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("400x500")

        # Поле для ввода
        self.display = tk.Entry(root, font=("Arial", 20), justify="right", bd=10, relief=tk.SUNKEN)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Заглушка: кнопки будут добавлены позже
        label = tk.Label(root, text="Калькулятор в разработке", font=("Arial", 14))
        label.grid(row=1, column=0, columnspan=4, pady=50)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    calc.run()