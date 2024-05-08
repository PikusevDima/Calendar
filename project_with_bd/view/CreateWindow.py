import tkinter as tk
from database.data.models.Car import Car


class CreateWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.submit_button = None
        self.new_car = None

        self.title("My Application")
        self.geometry("300x150")

        self.__model = tk.StringVar()
        self.__price = tk.StringVar(value="0")
        self.__mileage = tk.StringVar(value="0")

        self.create_widgets()
        self.load()

        self.grab_set()
        self.wait_window()

    def create_widgets(self):
        contanier = tk.Frame(self)
        contanier.pack(expand=True, fill=tk.BOTH, padx=10, pady=20)
        # model
        contanier_model = tk.Frame(contanier)
        contanier_model.pack(fill=tk.BOTH)

        label_model = tk.Label(contanier_model, text="Model")
        label_model.pack(side=tk.LEFT)

        entry_model = tk.Entry(contanier_model, textvariable=self.__model)
        entry_model.pack(side=tk.RIGHT, fill=tk.X)
        # model end

        # price
        contanier_price = tk.Frame(contanier)
        contanier_price.pack(fill=tk.BOTH)

        label_price = tk.Label(contanier_price, text="Price")
        label_price.pack(side=tk.LEFT)

        entry_price = tk.Entry(contanier_price, textvariable=self.__price)
        entry_price.pack(side=tk.RIGHT, fill=tk.X)
        # price end

        # mileage
        contanier_mileage = tk.Frame(contanier)
        contanier_mileage.pack(fill=tk.BOTH)

        label_mileage = tk.Label(contanier_mileage, text="Mileage")
        label_mileage.pack(side=tk.LEFT)

        entry_mileage = tk.Entry(contanier_mileage, textvariable=self.__mileage)
        entry_mileage.pack(side=tk.RIGHT, fill=tk.X)
        # mileage

        self.submit_button = tk.Button(contanier, text="Submit")
        self.submit_button['command'] = self.submit
        self.submit_button.pack(fill=tk.BOTH)

    def submit(self):
        if len(self.__model.get()) == 0:
            return

        try:
            self.new_car = Car(
                None,
                self.__model.get(),
                int(self.__price.get()),
                int(self.__mileage.get())
            )
            self.close()
        except Exception as e:
            print(e)

    def close(self):
        self.destroy()

    def load(self):
        ...
