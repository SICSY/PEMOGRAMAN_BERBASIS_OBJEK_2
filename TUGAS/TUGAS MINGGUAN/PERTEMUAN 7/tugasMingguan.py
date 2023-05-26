import tkinter as tk

class BMIApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Kalkulator BMI")
        self.geometry("400x200")

        self.label_weight = tk.Label(self, text="Berat (kg):")
        self.label_weight.pack()
        self.entry_weight = tk.Entry(self)
        self.entry_weight.pack()

        self.label_height = tk.Label(self, text="Tinggi (cm):")
        self.label_height.pack()
        self.entry_height = tk.Entry(self)
        self.entry_height.pack()

        self.button_calculate = tk.Button(self, text="Hitung", command=self.calculate_bmi)
        self.button_calculate.pack()

        self.label_result = tk.Label(self, text="Hasil BMI:")
        self.label_result.pack()
        self.label_bmi = tk.Label(self, text="")
        self.label_bmi.pack()

    def calculate_bmi(self):
        weight = float(self.entry_weight.get())
        height = float(self.entry_height.get()) / 100

        bmi = weight / (height ** 2)
        self.label_bmi.config(text="{:.2f}".format(bmi))
        self.display_result(bmi)

    def display_result(self, bmi):
        if bmi < 18.5:
            result = "Kurus"
        elif 18.5 <= bmi < 24.9:
            result = "Normal"
        elif 24.9 <= bmi < 29.9:
            result = "Gemuk"
        else:
            result = "Obesitas"

        self.label_result.config(text="Hasil BMI:")
        self.label_bmi.config(text=result)


if __name__ == "__main__":
    app = BMIApp()
    app.mainloop()
