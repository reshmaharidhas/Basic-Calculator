#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python Desktop application using Tkinter to perform basic mathematical calculations
Author: Reshma
"""

# Importing Tkinter
import tkinter as tk

class BasicCalculator:
    def __init__(self):
        # GUI creation
        self.window = tk.Tk()
        # Dimension of GUI window
        self.window.geometry("370x400")
        self.window.resizable(0, 0)
        # background color of master 'window' in GUI
        self.window.config(bg="#ffc6a5")
        # Title of the window
        self.window.title("Basic Calculator v1.0")
        self.expr = tk.StringVar(self.window)
        self.alertMessage = tk.StringVar(self.window)
        self.label1 = tk.Label(self.window, text="", font=("Consolas", 30), bg="black", fg="white", textvariable=self.expr,
                          relief=tk.RAISED, bd=10, width=15, anchor="e")
        self.label1.grid(row=0, column=0)
        self.alert = tk.Label(self.window, font=("Helvetica", 10), fg="red", textvariable=self.alertMessage, bg="#ffc6a5")
        self.alert.grid(row=1, column=0, pady=4)
        self.firstRow = tk.Frame()
        self.firstRow.config(bg="#ffc6a5")
        self.firstRow.grid(row=2)
        # Buttons in Calculator
        self.button1 = tk.Button(self.firstRow, text="1", font=("Helvetica", 24), command=self.btn1, bg="#7e0a2e", fg="white",
                            activebackground="#7e0a2e")
        self.button1.grid(row=1, column=0, padx=10, pady=5)
        self.button2 = tk.Button(self.firstRow, text="2", font=("Helvetica", 24), bg="#7e0a2e", fg="white", command=self.btn2,
                            activebackground="#7e0a2e")
        self.button2.grid(row=1, column=1, padx=10, pady=5)
        self.button3 = tk.Button(self.firstRow, text="3", font=("Helvetica", 24), bg="#7e0a2e", fg="white", command=self.btn3,
                            activebackground="#7e0a2e")
        self.button3.grid(row=1, column=2, padx=10, pady=5)
        # Button to remove the last clicked digit or operator from the input math expression
        self.buttonBackspace = tk.Button(self.firstRow, text="<---", font=("Helvetica",20),
                                    command=self.backspace, bg="#7e0a2e",fg="white")
        self.buttonBackspace.grid(row=1, column=4, padx=10, pady=5)
        # Button to clear the input expression
        self.buttonClear = tk.Button(self.firstRow, text="C", font=("Helvetica", 24), command=self.btnClear, bg="#7e0a2e", fg="white",
                                width=3, activebackground="#7e0a2e")
        self.buttonClear.grid(row=1, column=3, padx=10, pady=5)
        # Button to insert open bracket into the input expression
        self.buttonOpenB = tk.Button(self.firstRow, text="(", font=("Helvetica", 24), command=self.btnOpenBracket, bg="#7e0a2e",
                                fg="white", width=2, activebackground="#7e0a2e")
        self.buttonOpenB.grid(row=2, column=4, padx=10, pady=5)
        # Button to insert closed bracket into the input expression
        self.buttonCloseB = tk.Button(self.firstRow, text=")", font=("Helvetica", 24), command=self.btnCloseBracket, bg="#7e0a2e",
                                 fg="white", width=2, activebackground="#7e0a2e")
        self.buttonCloseB.grid(row=3, column=4, padx=10, pady=5)
        self.button4 = tk.Button(self.firstRow, text="4", font=("Helvetica", 24), command=self.btn4, bg="#7e0a2e", fg="white",
                            activebackground="#7e0a2e")
        self.button4.grid(row=2, column=0, padx=10, pady=5)
        self.button5 = tk.Button(self.firstRow, text="5", font=("Helvetica", 24), bg="#7e0a2e", fg="white", command=self.btn5,
                            activebackground="#7e0a2e")
        self.button5.grid(row=2, column=1, padx=10, pady=5)
        self.button6 = tk.Button(self.firstRow, text="6", font=("Helvetica", 24), bg="#7e0a2e", fg="white", command=self.btn6,
                            activebackground="#7e0a2e")
        self.button6.grid(row=2, column=2, padx=10, pady=5)
        self.button7 = tk.Button(self.firstRow, text="7", font=("Helvetica", 24), command=self.btn7, bg="#7e0a2e", fg="white",
                            activebackground="#7e0a2e")
        self.button7.grid(row=3, column=0, padx=10, pady=5)
        self.button8 = tk.Button(self.firstRow, text="8", font=("Helvetica", 24), bg="#7e0a2e", fg="white", command=self.btn8,
                            activebackground="#7e0a2e")
        self.button8.grid(row=3, column=1, padx=10, pady=5)
        self.button9 = tk.Button(self.firstRow, text="9", font=("Helvetica", 24), bg="#7e0a2e", fg="white", command=self.btn9,
                            activebackground="#7e0a2e")
        self.button9.grid(row=3, column=2, padx=10, pady=5)
        self.button0 = tk.Button(self.firstRow, text="0", font=("Helvetica", 24), bg="#7e0a2e", fg="white", command=self.btn0,
                            activebackground="#7e0a2e")
        self.button0.grid(row=4, column=0, padx=10, pady=5)
        # Button to include addition operator into the input
        self.buttonAdd = tk.Button(self.firstRow, text="+", font=("Helvetica", 24), bg="#7e0a2e", fg="white", command=self.btnAdd,
                              activebackground="#7e0a2e", width=2)
        self.buttonAdd.grid(row=4, column=1, padx=10, pady=5)
        # Button to include subtraction operator into the input
        self.buttonSubtract = tk.Button(self.firstRow, text="-", font=("Helvetica", 24), bg="#7e0a2e", fg="white",
                                   command=self.btnSubtract, activebackground="#7e0a2e", width=2)
        self.buttonSubtract.grid(row=4, column=2, padx=10, pady=5)
        # Button to include multiplication operator into the input
        self.buttonMultiply = tk.Button(self.firstRow, text="X", font=("Helvetica", 24), bg="#7e0a2e", fg="white",
                                   command=self.btnMultiply, activebackground="#7e0a2e", width=3)
        self.buttonMultiply.grid(row=2, column=3, padx=10, pady=5)
        # Button to include division operator into the input
        self.buttonDivide = tk.Button(self.firstRow, text="/", font=("Helvetica", 24), bg="#7e0a2e", fg="white",
                                 command=self.btnDivide, activebackground="#7e0a2e", width=3)
        self.buttonDivide.grid(row=3, column=3, padx=10, pady=5)
        # Button "=" to display the evaluation result of the expression
        self.buttonEqual = tk.Button(self.firstRow, text="=", font=("Helvetica", 24), bg="#7e0a2e", fg="white", command=self.btnTotal,
                                activebackground="#7e0a2e", width=7)
        self.buttonEqual.grid(row=4, column=3, columnspan=4, padx=10, pady=5)
        self.window.mainloop()
    hasError=False
    def btn1(self):
        self.expr.set(self.expr.get()+"1")
    def btn2(self):
        self.expr.set(self.expr.get()+"2")
    def btn3(self):
        self.expr.set(self.expr.get()+"3")
    def btn4(self):
        self.expr.set(self.expr.get()+"4")
    def btn5(self):
        self.expr.set(self.expr.get()+"5")
    def btn6(self):
        self.expr.set(self.expr.get()+"6")
    def btn7(self):
        self.expr.set(self.expr.get()+"7")
    def btn8(self):
        self.expr.set(self.expr.get()+"8")
    def btn9(self):
        self.expr.set(self.expr.get()+"9")
    def btn0(self):
        self.expr.set(self.expr.get()+"0")
    def btnAdd(self):
        self.expr.set(self.expr.get()+"+")
    def btnSubtract(self):
        self.expr.set(self.expr.get()+"-")
    def btnMultiply(self):
        self.expr.set(self.expr.get()+"x")
    def btnDivide(self):
        self.expr.set(self.expr.get()+"/")
    def btnOpenBracket(self):
        self.expr.set(self.expr.get()+"(")
    def btnCloseBracket(self):
        self.expr.set(self.expr.get()+")")
    def btnTotal(self):
        infix = self.expr.get()
        array = []
        topPtr = -1
        global hasError
        hasError = False
        # checking if the number of round brackets are equal
        if infix=="" or infix.count("(")!=infix.count(")") or infix.find("()")>=0 or infix.find(")(")>=0:
            hasError = True
        else:
            # Further checking if the given infix expression from user is balanced string or not.
            # If unbalanced infix expression, it shows 'Syntax ERROR'
            # If the infix expression is balanced, it returns the answer by evaluating the infix expression using calculate() function.
            pointer=0
            while pointer<len(infix):
                ch = infix[pointer]
                if topPtr==-1:
                    if ch in "+x/":
                        hasError = True
                        break
                    elif ch=="-":
                        array.append("-")
                        topPtr += 1
                    elif ch.isdigit() or ch=="(" or ch==")":
                        array.append(ch)
                        topPtr += 1
                else:
                    if ch=="(" or ch==")":
                        array.append(ch)
                        topPtr += 1
                    elif ch.isdigit():
                        if array[topPtr].isdigit():
                            array[topPtr] += ch
                        else:
                            array.append(ch)
                            topPtr += 1
                    elif ch=="+" or ch=="-" or ch=="x" or ch=="/":
                        if array[topPtr].isdigit():
                            array.append(ch)
                            topPtr += 1
                        elif infix[pointer-1]=="(":
                            array.append("-")
                            topPtr += 1
                        else:  # If two operators are next to each other in infix expression, it is UNBALANCED.
                            hasError=True
                            break
                pointer += 1
        if hasError==True or len(array)==0 or array[len(array)-1] in "+-x/":
            self.alertMessage.set("Syntax ERROR")
        else:
            self.alertMessage.set("")
            self.alert.config(bg="#ffc6a5")
            total = calculate(infix)
            if total=="Syntax Error--":
                self.alertMessage.set("Syntax ERROR")
            else:
                self.expr.set(total)
    # Function of button 'backspace' to remove the last clicked operand or operator from the input expression          
    def backspace(self):
        if len(self.expr.get())>0:
            self.expr.set(self.expr.get()[0:len(self.expr.get())-1])

    # Function to clear the input expression to empty. This function is connected with button 'buttonClear'
    def btnClear(self):
        hasError = False
        self.expr.set("")
        self.alertMessage.set("")
      
# Function to evaluate the given balanced INFIX expression by converting it to postfix expression
def calculate(s):
    global hasError
    arr = []
    topPtr = -1
    total = 0
    for ch in s:
        if topPtr == -1:
            arr.append(ch)
            topPtr += 1
        else:
            if ch in "+-x/()":
                arr.append(ch)
                topPtr += 1
            else:
                if arr[topPtr].isdigit() or (topPtr == 0 and arr[topPtr] == "-") or (
                            topPtr >= 0 and arr[topPtr] == "-" and arr[topPtr - 1] == "(") or (
                            "-" in arr[topPtr] and len(arr[topPtr]) > 1):
                    arr[topPtr] += ch
                else:
                    arr.append(ch)
                    topPtr += 1
    # converting to postfix
    postfix = []
    precMap = {"+": 1, "-": 1, "x": 2, "/": 2, "^": 3}
    stackArr = []
    topPtr = -1
    ptr = 0
    while ptr < len(arr):
        element = arr[ptr]
        if element not in "+-x/()":
            postfix.append(element)
        else:
            if topPtr == -1:
                stackArr.append(element)
                topPtr += 1
            else:
                if element == "(":
                    stackArr.append(element)
                    topPtr += 1
                elif element == ")":
                    while stackArr[topPtr] != "(":
                        postfix.append(stackArr.pop())
                        topPtr -= 1
                    stackArr.pop()
                    topPtr -= 1
                elif stackArr[topPtr] == "(" or precMap[stackArr[topPtr]] < precMap[element]:
                    if element == "-" and arr[ptr - 1] == "(":
                        stackArr.append("-n")
                    else:
                        stackArr.append(element)
                    topPtr += 1
                elif precMap[stackArr[topPtr]] > precMap[element]:
                    postfix.append(stackArr.pop())
                    topPtr -= 1
                    ptr = ptr - 1
                elif precMap[stackArr[topPtr]] == precMap[element]:
                    postfix.append(stackArr.pop())
                    topPtr -= 1
                    stackArr.append(element)
                    topPtr += 1
        ptr = ptr + 1
    while len(stackArr) > 0:
        postfix.append(stackArr.pop())
        topPtr -= 1
    # Evaluating Postfix expression
    stack2 = []
    for element in postfix:
        if element == "-n":
            num = stack2.pop()
            num = (-1) * num
            stack2.append(num)
        elif element not in "+-x/":
            stack2.append(int(element))
        else:
            y = stack2.pop()
            if len(stack2) == 0:
                if element == "-":
                    stack2.append((-1) * y)
            else:
                x = stack2.pop()
                total = 0
                if element == "+":
                    total = x + y
                elif element == "-":
                    total = x - y
                elif element == "x":
                    total = x * y
                elif element == "/":
                    if y != 0:
                        total = x // y
                stack2.append(total)
    if len(stack2)==0 or stack2[0]=="(" or stack2[0]==")" or hasError==True:
        return "Syntax ERROR"
    return stack2[0]
#object created for the class 'BasicCalculator'
BasicCalculator()
