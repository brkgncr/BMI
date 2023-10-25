import tkinter

window = tkinter.Tk()
window.title("BMI Calculater")
window.minsize(width=250, height=150)


def calculate():
    kg = float(my_kg_entry.get())
    cm = float(my_cm_entry.get()) / 100
    bmi = kg / (cm * cm)
    bmi_str = "{:.2f}".format(bmi)
    if bmi < 18.5:
        result_text = "Your BMI is " + bmi_str + ". You are underweight"
    elif 18.5 < bmi < 24.9:
        result_text = "Your BMI is " + bmi_str + ". You are normal weight"
    elif 25.0 < bmi < 29.9:
        result_text = "Your BMI is " + bmi_str + ". You are overweight"
    elif 30.0 < bmi < 34.9:
        result_text = "Your BMI is " + bmi_str + ". You are obesity class I"
    elif 35.0 < bmi < 39.9:
        result_text = "Your BMI is " + bmi_str + ". You are obesity class II"
    elif 40 < bmi:
        result_text = "Your BMI is " + bmi_str + ". You are obesity class III"
    my_calc_label.config(text=result_text)


my_kg_label = tkinter.Label(text="Enter Your Weight (kg)")
my_kg_label.pack()

my_kg_entry = tkinter.Entry(width=12)
my_kg_entry.pack()

my_cm_label = tkinter.Label(text="Enter Your Height (cm)")
my_cm_label.pack()

my_cm_entry = tkinter.Entry(width=12)
my_cm_entry.pack()

my_calc_button = tkinter.Button(text="Calculate", command=calculate)
my_calc_button.pack()

my_calc_label = tkinter.Label()
my_calc_label.pack()

window.mainloop()