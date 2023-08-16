from tkinter import *

wind = Tk()
wind.title("Calculator")
wind.geometry("300x400")
wind.configure(bg="#F2F3F4")

text = Entry(wind, font=("calibri", 16), bg="white", fg="#333")
text.pack(fill=X, padx=10, pady=10, ipadx=5, ipady=5)

def addToText(n):
    text.insert(END, n)

def calculate():
    result = eval(text.get())
    text.delete(0, END)
    text.insert(0, result)

frame = Frame(wind, bg="#F2F3F4")
frame.pack(side=TOP, anchor=NW)

rightFrame = Frame(frame, bg="#F2F3F4")
rightFrame.pack(side=RIGHT)

frame1 = Frame(frame, bg="#F2F3F4")
frame1.pack()


btn1 = Button(frame1, text="1", width=9, height=3, command=lambda: addToText("1"), bg="#AEB6BF", fg="#333")
btn1.pack(side=LEFT, padx=5, pady=5)
btn2 = Button(frame1, text="2", width=9, height=3, command=lambda: addToText("2"), bg="#AEB6BF", fg="#333")
btn2.pack(side=LEFT, padx=5, pady=5)
btn3 = Button(frame1, text="3", width=9, height=3, command=lambda: addToText("3"), bg="#AEB6BF", fg="#333")
btn3.pack(side=LEFT, padx=5, pady=5)

frame2 = Frame(frame, bg="#F2F3F4")
frame2.pack()


btn4 = Button(frame2, text="4", width=9, height=3, command=lambda: addToText("4"), bg="#AEB6BF", fg="#333")
btn4.pack(side=LEFT, padx=5, pady=5)
btn5 = Button(frame2, text="5", width=9, height=3, command=lambda: addToText("5"), bg="#AEB6BF", fg="#333")
btn5.pack(side=LEFT, padx=5, pady=5)
btn6 = Button(frame2, text="6", width=9, height=3, command=lambda: addToText("6"), bg="#AEB6BF", fg="#333")
btn6.pack(side=LEFT, padx=5, pady=5)

frame3 = Frame(frame, bg="#F2F3F4")
frame3.pack()


btn7 = Button(frame3, text="7", width=9, height=3, command=lambda: addToText("7"), bg="#AEB6BF", fg="#333")
btn7.pack(side=LEFT, padx=5, pady=5)
btn8 = Button(frame3, text="8", width=9, height=3, command=lambda: addToText("8"), bg="#AEB6BF", fg="#333")
btn8.pack(side=LEFT, padx=5, pady=5)
btn9 = Button(frame3, text="9", width=9, height=3, command=lambda: addToText("9"), bg="#AEB6BF", fg="#333")
btn9.pack(side=LEFT, padx=5, pady=5)

frame4 = Frame(frame, bg="#F2F3F4")
frame4.pack()


btnpoint = Button(frame4, text=".", width=9, height=3, command=lambda: addToText("."), bg="#AEB6BF", fg="#333")
btnpoint.pack(side=LEFT, padx=5, pady=5)
btnzero = Button(frame4, text="0", width=9, height=3, command=lambda: addToText("0"), bg="#AEB6BF", fg="#333")
btnzero.pack(side=LEFT, padx=5, pady=5)
btneq = Button(frame4, text="=", width=9, height=3, command=lambda: calculate(), bg="#2980B9", fg="white")
btneq.pack(side=LEFT, padx=5, pady=5)


btndiv = Button(rightFrame, text="/", width=9, height=3, command=lambda: addToText("/"), bg="#AEB6BF", fg="#333")
btndiv.pack(pady=5)
btnmul = Button(rightFrame, text="x", width=9, height=3, command=lambda: addToText("*"), bg="#AEB6BF", fg="#333")
btnmul.pack(pady=5)
btndif = Button(rightFrame, text="-", width=9, height=3, command=lambda: addToText("-"), bg="#AEB6BF", fg="#333")
btndif.pack(pady=5)
btnplus = Button(rightFrame, text="+", width=9, height=3, command=lambda: addToText("+"), bg="#AEB6BF", fg="#333")
btnplus.pack(pady=5)

wind.mainloop()

