import tkinter as tk

calculator = tk.Tk()
calculator.geometry("380x410")
#calculator.geometry("380x345")
calculator.resizable(False, False)
calculator.title("Custom Calculator")


def calculation():
    try:
        dispbx.insert(tk.END, "=")
        exp = dispbx.get()
        if "=" in exp:
            new_exp = exp.replace("=", "")

        if "÷" in new_exp:
            new_exp = new_exp.replace("÷", "/")

        if "x" in new_exp:
            new_exp = new_exp.replace("x", "*")

        result = eval(new_exp)
        dispbx.insert(tk.END, "".join([str(result)]))
    except Exception:
        dispbx.delete(0, tk.END)
        dispbx.insert(tk.END, "Error")



def btn_1_click():
    dispbx.insert(tk.END, "1")

def btn_2_click():
    dispbx.insert(tk.END,"2")

def btn_3_click():
    dispbx.insert(tk.END,"3")

def btn_4_click():
    dispbx.insert(tk.END,"4")

def btn_5_click():
    dispbx.insert(tk.END,"5")

def btn_6_click():
    dispbx.insert(tk.END,"6")

def btn_7_click():
    dispbx.insert(tk.END,"7")

def btn_8_click():
    dispbx.insert(tk.END,"8")

def btn_9_click():
    dispbx.insert(tk.END,"9")

def btn_modulo_click():
    dispbx.insert(tk.END, "%")

def btn_division_click():
    dispbx.insert(tk.END, "÷")

def btn_multiply_click():
    dispbx.insert(tk.END, "x")

def btn_subtract_click():
    dispbx.insert(tk.END, "-")

def btn_addition_click():
    dispbx.insert(tk.END, "+")

def btn_point_click():
    dispbx.insert(tk.END, ".")

def btn_0_click():
    dispbx.insert(tk.END, "0")

def btn_clear_click():
    dispbx.delete(0, tk.END)

def btn_paren_click():
    op = ["+", "-", "*", "/", "%"]
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    exp = dispbx.get()
    if exp == "":
        dispbx.insert(tk.END, "(")
        return
    open_bracket = exp.count("(")
    close_bracket = exp.count(")")
    index = exp.rfind("(")
    substring_after_index = exp[index + 1:]
    last_char = exp[-1]
    if last_char == "(":
        dispbx.insert(tk.END, "(")
        return
    if last_char in op:
        dispbx.insert(tk.END, "(")
    elif (last_char in num or last_char == ")") and open_bracket > close_bracket:
        dispbx.insert(tk.END, ")")
    elif open_bracket == close_bracket:
        dispbx.insert(tk.END, "*(")


def back_btn_click():
    exp = dispbx.get()
    del_char = exp[:-1]
    dispbx.delete(0, tk.END)
    dispbx.insert(tk.END, del_char)




    
# Display box 
dispbx = tk.Entry(calculator,  
                 width=22, 
                 font=("Helvetica", 20)
                 )
dispbx.grid(row=0, column=0, columnspan=4, padx=3, pady=3, sticky="ew")


#Frame for buttons 
frame = tk.Frame(calculator, bg="grey", width=395, height=200)
frame.grid(row=1, column=0, sticky="nsew")
frame.grid_propagate(False)  # Prevent the frame from shrinking

#Allow frame to expand nicely
calculator.rowconfigure(1, weight=1)

# Back Button 
btn_clear = tk.Button(frame, text="⌫", height=1, width=4, font=("Arial", 20, "bold"), relief="raised", bd=6, command=back_btn_click)
btn_clear.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

# Parenthesis Button
btn_paren = tk.Button(frame, text="()", height=1, width=4, font=("Arial", 20, "bold"), relief="raised", bd=6, command=btn_paren_click)
btn_paren.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Modulo Button
mod_btn = tk.Button(frame, text="%", height=1, width=4, font=("Arial", 20, "bold"), relief="raised", bd=6, command=btn_modulo_click)
mod_btn.grid(row=0, column=2, padx=5, pady=5)

# Divide Button
divide_btn = tk.Button(frame, text="÷", height=1, width=4, font=("Arial", 20, "bold"), relief="raised", bd=6, command=btn_division_click)
divide_btn.grid(row=0, column=3, padx=5, pady=5)

# Number 7
btn_7 = tk.Button(frame, text="7", height=1, width=4, font=("Arial", 20, "bold"), relief="raised", bd=6, command=btn_7_click)
btn_7.grid(row=1, column=0, padx=5, pady=5)

# Number 8
btn_8 = tk.Button(frame, text="8", height=1, width=4, font=("Arial", 20, "bold"), relief="raised", bd=6, command=btn_8_click)
btn_8.grid(row=1, column=1, padx=5, pady=5)

# Number 9
btn_9 = tk.Button(frame, text="9", height=1, width=4, font=("Arial", 20, "bold"), relief="raised", bd=6, command=btn_9_click)
btn_9.grid(row=1, column=2, padx=5, pady=5)

# Multiply Button
btn_multiply = tk.Button(frame, text="x", height=1, width=4, font=("Arial", 20, "bold"), relief="raised", bd=6, command=btn_multiply_click)
btn_multiply.grid(row=1, column=3, padx=5, pady=5)

# Number 4
btn_4 = tk.Button(frame, text="4", height=1, width=4, font=("Arial", 20, "bold"), relief="raised", bd=6, command=btn_4_click)
btn_4.grid(row=2, column=0, padx=5, pady=5)

# Number 5
btn_5 = tk.Button(frame, text="5", height=1, width=4, font=("Arial", 20, "bold"), relief="raised", bd=6, command=btn_5_click)
btn_5.grid(row=2, column=1, padx=5, pady=5)

# Number 6
btn_6 = tk.Button(frame, text="6", height=1, width=4, font=("Arial", 20, "bold"), relief="raised", bd=6, command=btn_6_click)
btn_6.grid(row=2, column=2, padx=5, pady=5)

# Subtract
btn_subtract = tk.Button(frame, text="-", height=1, width=4, font=("Arial", 20, "bold"), relief="raised", bd=6, command=btn_subtract_click)
btn_subtract.grid(row=2, column=3, padx=5, pady=5)

# Number 1
btn_1 = tk.Button(frame, text="1", height=1, width=4, font=("Arial", 20, "bold"), relief="raised", bd=6, command=btn_1_click)
btn_1.grid(row=3, column=0, padx=5, pady=5)

# Number 2
btn_2 = tk.Button(frame, text="2", height=1, width=4, font=("Arial", 20, "bold"), relief="raised", bd=6, command=btn_2_click)
btn_2.grid(row=3, column=1, padx=5, pady=5)

# Number 3
btn_3 = tk.Button(frame, text="3", height=1, width=4, font=("Arial", 20, "bold"), relief="raised", bd=6, command=btn_3_click)
btn_3.grid(row=3, column=2, padx=5, pady=5)

# Addition
btn_addition = tk.Button(frame, text="+", height=1, width=4, font=("Arial", 20, "bold"), relief="raised", bd=6, command=btn_addition_click)
btn_addition.grid(row=3, column=3, padx=5, pady=5)

# Clear Button
btn_negative = tk.Button(frame, text="C", height=1, width=4, font=("Arial", 20, "bold"), relief="raised", bd=6, command=btn_clear_click)
btn_negative.grid(row=4, column=0, padx=0, pady=5)

# Zero Button
btn_zero = tk.Button(frame, text="0", height=1, width=4, font=("Arial", 20, "bold"), relief="raised", bd=6, command=btn_0_click)
btn_zero.grid(row=4, column=1, padx=5, pady=5)

# Decimal Point
btn_decimal = tk.Button(frame, text=".", height=1, width=4, font=("Arial", 20, "bold"), relief="raised", bd=6, command=btn_point_click)
btn_decimal.grid(row=4, column=2, padx=5, pady=5)

# Equals Button
btn_equals = tk.Button(frame, text="=", height=1, width=4, font=("Arial", 20, "bold"), relief="raised", bd=6, command=calculation)
btn_equals.grid(row=4, column=3, padx=5, pady=5)



calculator.mainloop()

 