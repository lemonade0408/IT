
import requests
import tkinter as tk
from tkinter import messagebox


class CurrencyConverter:
    def __init__(self, rate):
        self.rate = rate

    def convert(self, uah):
        return uah / self.rate


url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangeNew?json&valcode=USD"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    rate = data[0]["rate"]
    date = data[0]["exchangedate"]

    converter = CurrencyConverter(rate)

except (requests.RequestException, ValueError, KeyError, IndexError, TypeError):
    print("Не удалось получить курс НБУ!")
    raise SystemExit


window = tk.Tk()
window.title("Конвертер валют")
window.geometry("420x320")
window.resizable(False, False)

title = tk.Label(
    window,
    text="Конвертер гривны в доллары",
    font=("Arial", 16, "bold")
)
title.pack(pady=20)

rate_label = tk.Label(
    window,
    text=f"Курс НБУ: 1 USD = {rate} UAH\nДата: {date}",
    font=("Arial", 11)
)
rate_label.pack(pady=10)

input_label = tk.Label(
    window,
    text="Введите сумму в гривнах:",
    font=("Arial", 12)
)
input_label.pack()

money_entry = tk.Entry(window, font=("Arial", 14), justify="center")
money_entry.pack(pady=10)


def convert_money():
    try:
        money = float(money_entry.get().replace(",", "."))

        if money < 0:
            messagebox.showerror("Ошибка", "Сумма не может быть отрицательной.")
            return

        result = converter.convert(money)

        result_label.config(
            text=f"{money:.2f} UAH = {result:.2f} USD"
        )

    except ValueError:
        messagebox.showerror("Ошибка", "Введите правильное число!")


button = tk.Button(
    window,
    text="Конвертировать",
    font=("Arial", 12),
    command=convert_money
)
button.pack(pady=15)

result_label = tk.Label(
    window,
    text="Результат появится здесь",
    font=("Arial", 14, "bold")
)
result_label.pack(pady=10)


window.mainloop()
