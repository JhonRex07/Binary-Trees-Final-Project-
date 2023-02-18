# PROJECT ON DATA STRUCTURES AND ALGORITHMS
# Programmed by JHON REX B. JUSAYAN

from tkinter import *

main_window = Tk()
main_window.title("Python Binary Tree")
main_window.geometry("400x275")

def number():
    numbers = entry1.get().split()
    label2.configure(text="NUMBERS: " + str(numbers))
    
if __name__ == '__main__':
    label1 = Label(main_window, text="ENTER NUMBERS:", font=('Bold', 12))
    label1.place(height=100, width=415)

    entry1 = Entry(main_window, font=('Bold', 12))
    entry1.place(height=35, width=300, x=50)

    result_button1 = Button(main_window, text="SHOW RESULTS", command=number)
    result_button1.place(height=25, width=225, x=80, y=70)

    label2 = Label(main_window, text="NUMBERS: ")
    label2.place(height=30, x=35, y=100)

    label3 = Label(main_window, text="MINIMUM: ")
    label3.place(height=25,  x=35, y=130)

    label4 = Label(main_window, text="MAXIMUM: ")
    label4.place(height=25, x=200, y=130)

    label5 = Label(main_window, text="IN-ORDER TRAVERSE: ")
    label5.place(height=30, x=35, y=160)

    label6 = Label(main_window, text="PRE-ORDER TRAVERSE: ")
    label6.place(height=30, x=35, y=190)

    label7 = Label(main_window, text="POST-ORDER TRAVERSE: ")
    label7.place(height=30, x=35, y=220)

mainloop