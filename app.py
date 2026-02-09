import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("SIP Calculator")
root.geometry("400x370")
root.resizable(False, False)


def format_indian(number):
    s = f"{number:.2f}"
    before_decimal, after_decimal = s.split(".")

    if len(before_decimal) > 3:
        last3 = before_decimal[-3:]
        remaining = before_decimal[:-3]
        remaining = ",".join([remaining[max(i - 2, 0):i]
                              for i in range(len(remaining), 0, -2)][::-1])
        formatted = remaining + "," + last3
    else:
        formatted = before_decimal

    return formatted + "." + after_decimal


def calculate_sip():
    try:
        P = float(entry_amount.get())
        annual_rate = float(entry_rate.get())
        years = float(entry_years.get())

        r = annual_rate / 12 / 100
        n = years * 12

        FV = P * (((1 + r) ** n - 1) / r) * (1 + r)

        result_label.config(text=f"Future Value: ₹{format_indian(FV)}")


    except:
        messagebox.showerror("Error", "Please enter valid numbers!")


title = tk.Label(root, text="📈 SIP Calculator", font=("Arial", 20, "bold"))
title.pack(pady=15)

tk.Label(root, text="Monthly Investment (₹)", font=("Arial", 12)).pack()
entry_amount = tk.Entry(root)
entry_amount.pack(pady=5)

tk.Label(root, text="Expected Annual Return (%)", font=("Arial", 12)).pack()
tk.Label(root, text="Upto 30% is realistic, but not regularly!", font=("Arial", 10)).pack()
entry_rate = tk.Entry(root)
entry_rate.pack(pady=5)

tk.Label(root, text="Time Period (Years)", font=("Arial", 12)).pack()
entry_years = tk.Entry(root)
entry_years.pack(pady=5)

tk.Button(root, text="Calculate", command=calculate_sip,font=("Arial", 12, "bold")).pack(pady=15)

result_label = tk.Label(root, text="Future Value: ₹0.00",font=("Arial", 14, "bold"))
result_label.pack(pady=10)

root.mainloop()
