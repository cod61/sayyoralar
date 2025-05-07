#def kalkulyator():
  #  print("Oddiy kalkulyator")
  #  print("Amallar: +, -, *, /")
    
    #a = float(input("Birinchi sonni kiriting: "))
    #amal = input("Amalni tanlang (+, -, *, /): ")
    #b = float(input("Ikkinchi sonni kiriting: "))

   # if amal == '+':
   #     print(f"Natija: {a + b}")
   # elif amal == '-':
   #     print(f"Natija: {a - b}")
   # elif amal == '*':
   #     print(f"Natija: {a * b}")
   # elif amal == '/':
     #   if b != 0:
     #       print(f"Natija: {a / b}")
    #    else:
   #         print("Nolga bo‘lish mumkin emas!")
  #  else:
 #       print("Noto‘g‘ri amal kiritildi!")

#kalkulyator()




#import tkinter as tk

#def bosing(tugma):
   # if tugma == "=":
          #  try:
     #       natija = str(eval(kiritma.get()))
    #         kiritma.delete(0, tk.END)
    # #        kiritma.insert(tk.END, natija)
   #     except:
   #         kiritma.delete(0, tk.END)
   #         kiritma.insert(tk.END, "Xato!")
   # elif tugma == "C":
  #      kiritma.delete(0, tk.END)
   # else:
 #       kiritma.insert(tk.END, tugma)

# Oyna yaratamiz
#oyna = tk.Tk()
#oyna.title("Kalkulyator")

# Kiritma maydoni
#kiritma = tk.Entry(oyna, width=25, borderwidth=5, font=('Arial', 18))
#kiritma.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Tugmalar ro'yxati
#tugmalar = [
 #   '7', '8', '9', '/',
#    '4', '5', '6', '*',
#    '1', '2', '3', '-',
#    '0', '.', '=', '+',
#    'C'
#]

# Tugmalarni yaratish
#sat = 1
#ust = 0
#for tugma in tugmalar:
   # action = lambda x=tugma: bosing(x)
   # tk.Button(oyna, text=tugma, padx=20, pady=20, font=('Arial', 14), command=action).grid(row=sat, column=ust)

   # ust += 1
  #  if ust > 3:
 #       ust = 0
 #       sat += 1
#
# Oynani ko'rsatish
#oyna.mainloop()

import tkinter as tk

# Kalkulator funksiyalari
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)  # Hozirgi qiymatni o'chirish
    entry.insert(0, current + value)  # Yangi qiymatni qo'shish

def button_clear():
    entry.delete(0, tk.END)  # Barcha qiymatlarni o'chirish

def button_equal():
    try:
        result = eval(entry.get())  # Arifmetik ifodani hisoblash
        entry.delete(0, tk.END)
        entry.insert(0, str(result))  # Natijani ekranga chiqarish
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Xato")

# Asosiy oynani yaratish
root = tk.Tk()
root.title("Kalkulator")
root.geometry("400x500")

# Kirish maydoni
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Tugmalar
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0, 4)  # 'C' - Clear (barchasini o'chirish)
]

# Tugmalarni yaratish va joylashtirish
for (text, row, col, *rest) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=button_equal)
    elif text == "C":
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=button_clear)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda value=text: button_click(value))

    btn.grid(row=row, column=col, padx=5, pady=5)

# Kalkulatorni ishga tushirish
root.mainloop()

