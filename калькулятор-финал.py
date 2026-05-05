import tkinter as tk
from tkinter import messagebox
import re


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор (вещественные числа + mod)")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.expression = ""

        # Поле для ввода
        self.display = tk.Entry(root, font=("Arial", 20), justify="right", bd=10, relief=tk.SUNKEN)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Кнопки (с mod)
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('mod', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('=', 5, 1)
        ]

        for btn_text, row, col in buttons:
            if btn_text:
                btn = tk.Button(root, text=btn_text, font=("Arial", 16),
                                command=lambda t=btn_text: self.on_button_click(t))
                btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        # Настройка веса строк и столбцов
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, value):
        if value == 'C':
            self.expression = ""
            self.update_display()
        elif value == '=':
            self.calculate()
        else:
            self.expression += value
            self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

    def calculate(self):
        try:
            if not self.expression.strip():
                messagebox.showerror("Ошибка", "Выражение не введено")
                return

            # Замена mod на %
            expr = self.expression.replace('mod', '%')

            # Проверка деления на ноль
            if '/0' in expr or '%0' in expr:
                messagebox.showerror("Ошибка", "Деление на ноль невозможно")
                return

            # Проверка на допустимые символы
            if not re.match(r'^[\d\.\+\-\*/%]+$', expr):
                messagebox.showerror("Ошибка", "Некорректное выражение")
                return

            # Вычисление
            result = eval(expr)

            # Форматирование результата
            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 10)

            self.expression = str(result)
            self.update_display()

        except ZeroDivisionError:
            messagebox.showerror("Ошибка", "Деление на ноль невозможно")
        except Exception:
            messagebox.showerror("Ошибка", "Некорректное выражение")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    calc.run()