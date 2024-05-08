import tkinter as tk
from database.data.models.Car import Car


class CarView(tk.Frame):
    def __init__(self, parent, car: Car):
        # self.__background = "blue"

        super().__init__(parent,
                         borderwidth=1,
                         highlightthickness=1,
                         highlightbackground="red",
                         padx=10,
                         pady=10)

        self.__car = car

        self.__on_delete = None

        self.label_mileage = None
        self.label_price = None
        self.label_model = None
        self.button = None

        self.create_widgets()

    def set_event(self, event):
        self.__on_delete = event

    def create_widgets(self):
        self.label_model = tk.Label(self, text="Model: " + self.__car.model)
        self.label_model.pack(fill=tk.BOTH, expand=True)
        self.label_price = tk.Label(self, text=str(self.__car.price))
        self.label_price.pack()
        self.label_mileage = tk.Label(self, text=str(self.__car.mileage))
        self.label_mileage.pack()

        self.button = tk.Button(self, text="Delete")
        self.button['command'] = self.__delete
        self.button.pack()

    def __delete(self):
        self.__on_delete(self.__car.id)
