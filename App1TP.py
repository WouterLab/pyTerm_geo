
from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageGrab
import sys


x = []
y = []

file = open("file.txt", "w")
file.write('Введённые координаты вершин многоугольника: \n')

def get_all():  
    file = open("file.txt", "a")
    
    try:
        valuex = float(xname.get())
    except ValueError:
        message=messagebox.showerror(("Ошибка"), ("Введите число"))
    x.append(valuex)
    

    try:
        valuey = float(yname.get())
    except ValueError:
        message=messagebox.showerror(("Ошибка"), ("Введите число"))
    y.append(valuey)
    
    fieldx.insert(0.0, f'{valuex, valuey}')
    file.write(f'{valuex, valuey}\n')

def del_array():#отчистка массивов, содержащих внутри себя данные, введённых точек; отчистка холста
    file = open("file.txt", "w")
    file.write('Введённые координаты вершин многоугольника: \n')
    x.clear()
    y.clear()
    canvas.delete("all")
    fieldx.delete(1.0, "end")
    
    for i in range(10):
        canvas.create_line(i*50, 0, i*50, 500, fill= "grey") #вертикальные линии
        canvas.create_text(i*50, 10, text= i )
        canvas.create_line(0, i*50, 500, i*50, fill= "grey") #горизонтальные линии
        canvas.create_text(10, i*50, text=i)
    canvas.create_line(2, 2, 500, 2, fill= "red", arrow=LAST)
    canvas.create_line(2, 2, 2, 500, fill= "red", arrow=LAST)
    canvas.create_line(2, 500, 500, 500, fill= "red")
    canvas.create_line(500, 500, 500, 2, fill= "red")
    canvas.grid(row =16, rowspan = 6, column=0, columnspan=6, sticky="w")
    canvas.create_text(10,10, text="0,0")

def draw_function():#построение линий на графике
    global x, y
    cornersnumb = len(x)
    if (cornersnumb < 3):
        message=messagebox.showerror(("Ошибка"), ("Многоугольник не может содержать менее 3 углов"))
    else:
        try:
            tolsh=int(tol.get())
        except ValueError:
            message=messagebox.showerror(("Ошибка"), ("Введите целое число"))
        for i in range (cornersnumb):
            canvas.create_line((x[i-1]*50), (y[i-1]*50), (x[i]*50), (y[i]*50), width = tolsh, fill="red")

def S_function():#подсчёт площади
    file = open("file.txt", "a")
    global x, y
    cornersnumb= len(x)
    S1 = 0 
    for i in range (cornersnumb):
        Sum=x[i-1]*y[i]-x[i]*y[i-1]
        S1+=Sum
    S = float()
    S = abs(0.5 * S1)
    file.write('Площадь полученного многоугольника: ')
    S = str(S)
    file.write(S)
    text = Label(win, text = str(S), width=25, background="#E6E6FA").grid(row=19, column=4, stick ="w")
    
def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        win.destroy()

def vyp_function():#определение выпуклости
    
    file = open("file.txt", "a")
    file.write(' \n')
    
    global x, y
    cornersnumb= len(x)
    PosAngle = False
    NegAngle = False
    for i in range(cornersnumb):
        x1 = x[i]
        y1 = y[i]
        x2 = x[(i+1) % cornersnumb]
        y2 = y[(i+1) % cornersnumb]
        x3 = x[(i+2) % cornersnumb]
        y3 = y[(i+1) % cornersnumb]
        d = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)
        if d > 0:
            PosAngle = True
        elif d < 0:
            NegAngle = True
    if PosAngle and NegAngle:
        res = 'Многоугольник не выпуклый'
        file.write(res)
        text = Label(win, text = str(res), width=25, background="#E6E6FA").grid(row=21, column=4)
    else:
        res = 'Многоугольник выпуклый'
        file.write(res)
        text = Label(win, text = str(res), width=25, background="#E6E6FA").grid(row=21, column=4)
    
def about_programm():
    message=messagebox.showinfo(("О программе"), ("Данная программа предназначена для подсчёта площади и определения выпуклости произвольного многоугольника. \n \n Для начала работы Вам необходимо ввести координаты многоугольника. \n Нужно помнить что вводить координаты важно по часовой стрелке или в обратном направлении. \n\n Ввод координат происходит по одной координате, как только будут введены x и y, нажмите кнопку 'Записать координату'. Она покажется в окошке справа.\n \n Когда все координаты будут введены, введите желаемую толщину линий на графике и нажмите кнопку 'Построить график'. Вы увидете построенную фигуру. \n\n Если Вы допустили ошибку при вводе координа, нажмите кнопку 'Очистить координаты' и повторите ввод заново. \n Как только Вы убедитесь в правильности построенной фигуры, нажмите кнопки 'Посчитать площадь' и 'Определить выпуклость'. На экране покажутся расчёты площади и определение выпуклости многоугольника. \n\n Нажмите кнопку 'Сохранить значения' для сохранения данных на компьютер. "))

def save():
    x=win.winfo_rootx()+canvas.winfo_x()+8
    y=win.winfo_rooty()+canvas.winfo_y()+80
    x1=x+canvas.winfo_width()+120
    y1=y+canvas.winfo_height()+110    
    ImageGrab.grab().crop((x,y,x1,y1)).save("D:\Polly\proramming\TP/file.png") 

win = Tk()# создаём окно
win["bg"]= "#E6E6FA"
win.protocol("WM_DELETE_WINDOW", on_closing) 
win.title("Подсчёт площади и определение выпуклости многоугольника")
win.geometry('900x800+5+5') #размеры окна и отступы от левого верхнего угла
win.resizable(0,0) #нельзя изменить размер
#win.image = PhotoImage(file='cow.png')
#bg_logo=Label(win, image=win.image)
#bg_logo.grid(row = 0, rowspan=9999, column = 0, columnspan =100)

glavname=Canvas(win, width=1000, height=90, background="#FFFFE0")
glavname.grid(row=0, rowspan=4,column=0, columnspan= 8)

glavname.create_text(450,20, text="Определение выпуклости", fill="#4B0082", font=('Helvetica', 20))
glavname.create_text(450,45, text="и нахождение площади", fill="#4B0082", font=('Helvetica', 20))
glavname.create_text(450,70, text="произвольного многоугольника", fill="#4B0082", font=('Helvetica', 20))

Button(win, text="?", command= about_programm, font=('Helvetica', 10, "bold"), fg="#4B0082").grid(row=0, column=4, stick="e")

Zagolovokkoor=Label(win, text="Введите координаты: ", font=('Helvetica', 10, "bold"), fg="#4B0082", background="#E6E6FA" ).grid(row=5, column=0)
Zagolovokvved=Label(win, text="Введенные координаты: ", font=('Helvetica', 10, "bold"), fg="#4B0082",  background="#E6E6FA" ).grid(row=5, column=4)

Zagolovokx = Label(win, text = "Введите координату x:", background="#E6E6FA").grid(row=7, column =0)
xname = Entry(win)
xname.grid(row=7, column =1)

Button(win, text="Записать координату", command=get_all, font=('Helvetica', 8, "bold"), fg="#4B0082").grid(row=8, column = 2)

fieldx = Text( win, width=35, height=1)
fieldx.grid (row=8, column=4)

Zagolovoky = Label(win, text = "Введите координату y:", background="#E6E6FA").grid(row=9, column =0)
yname = Entry(win)
yname.grid(row=9, column =1)

Button(win, text="Очистить координаты", command= del_array, font=('Helvetica', 8, "bold"), fg="#4B0082").grid(row=9, column=4)

otstuptodraw=Canvas(win, width=1000, height=30, background="#FFFFE0")
otstuptodraw.grid(row=10, rowspan= 3, column = 0, columnspan=8)

Button(win, text="Построить график", command= draw_function, font=('Helvetica', 8, "bold"), fg="#4B0082").grid(row=15, column=2)

otstuptodrawtwo=Canvas(win, width=1000, height=30, background="#E6E6FA")
otstuptodrawtwo.grid(row=16, rowspan= 3, column = 0, columnspan=8)

canvas = Canvas(win, height=500, width=500, background="#FFF8DC")

for i in range(10):
    canvas.create_line(i*50, 0, i*50, 500, fill= "grey") #вертикальные линии
    canvas.create_text(i*50, 10, text= i )
    canvas.create_line(0, i*50, 500, i*50, fill= "grey") #горизонтальные линии
    canvas.create_text(10, i*50, text=i)
canvas.create_line(2, 2, 500, 2, fill= "red", arrow=LAST)
canvas.create_line(2, 2, 2, 500, fill= "red", arrow=LAST)
canvas.create_line(2, 500, 500, 500, fill= "red")
canvas.create_line(500, 500, 500, 2, fill= "red")
canvas.grid(row =17, rowspan = 6, column=0, columnspan=6, sticky="w")
canvas.create_text(10,10, text="0,0")

Zagolovoktol = Label(win, text = "Введите толщину линии графика:", background="#E6E6FA").grid(row=15, column =0)
tol = Entry(win)
tol.grid(row=15, column =1)

Button(win, text="Поcчитать площадь", command= S_function, font=('Helvetica', 8, "bold"), fg="#4B0082").grid(row=18, column=4, stick = "w")

Button(win, text="Определить выпуклость", command= vyp_function, font=('Helvetica', 8, "bold"), fg="#4B0082").grid(row=20, column=4, stick = "w")

Button(win, text="Сохранить значения", command= save, font=('Helvetica', 8, "bold"), fg="#4B0082").grid(row=22, column=4, stick = "e")

file.close()

win.mainloop()
sys.exit()